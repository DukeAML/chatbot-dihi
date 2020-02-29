# Copyright 2020, Duke Institute for Health Innovation (DIHI), Duke University School of Medicine, Durham NC. All Rights Reserved.

from flask import Flask
import logging

app = Flask(__name__, instance_relative_config=True)


# http://patorjk.com/software/taag/#p=display&f=Ogre&t=chatbot

app.logger.info("      _           _   _           _   ")
app.logger.info("  ___| |__   __ _| |_| |__   ___ | |_ ")
app.logger.info(" / __| '_ \\ / _` | __| '_ \\ / _ \\| __|")
app.logger.info("| (__| | | | (_| | |_| |_) | (_) | |_ ")
app.logger.info(" \\___|_| |_|\\__,_|\\__|_.__/ \\___/ \\__|")
app.logger.info('')                                      


#
# Import views - these MUST be imported after the app is configured
#

from .views import views  # noqa: F401,E402
