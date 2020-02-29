# Copyright 2020, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC. All Rights Reserved.
from app import app, emergency_processing
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
# configuration
DEBUG = True
em = emergency_processing.EmergencyMessage()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

MESSAGES = []

@app.route('/v1/messages', methods=['GET','POST'])
def all_messages():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        ## Shitty delete route ******
        reset = post_data.get('reset') == 'true'
        if reset is True:
            MESSAGES.clear()
        else:
            is_emergency = em.check_emergency_message(post_data.get('message'))
            response_object['message'] = post_data.get('message')
            response_object['emergency'] = str(is_emergency)
            if is_emergency is False:
                MESSAGES.append({
                'message': post_data.get('message'),
                'emergency': str(is_emergency),
                'time': datetime.datetime.today()
                })
    else:
        response_object['messages'] = MESSAGES
    return jsonify(response_object)

@app.route('/v1/nonemergency', methods=['GET','POST'])
def non_emergency_messages():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        if 'emergency' in post_data:
            emergency = post_data.get('emergency')
        else:
            emergency = str(False)
        MESSAGES.append({
            'message': post_data.get('message'),
            'emergency': emergency,
            'time': datetime.datetime.today()
        })
    else:
        response_object['messages'] = MESSAGES
    return jsonify(response_object)

@app.route('/status', methods=['GET'])
def status():
    """
    Perform a basic health check.
    :returns: HTTP 200 if okay
    """
    return ('', 200)
