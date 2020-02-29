<template>
  <div class="chat container">
    <h1 style="font-size: 32pt">Welcome to the Duke Health Safety Chat</h1>
    
    <br>
    
    <div style="font-size: 24pt">
      
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="fieldset-1"
          description="Please do not submit emergencies, this is only monitored every 1-3 days."
          label="What can we help you with?"
          label-for="textarea"
        >
        <b-form-textarea
          id="textarea"
          v-model="messageForm.message"
          placeholder="Click to start typing..."
          rows="5"
          size="lg"
          font-size= 24pt;
        >
        </b-form-textarea>

        </b-form-group>
        <b-button v-if="!checkEmergency" type="reset" variant="primary" size="lg" style="margin: 30px; font-size: 18pt;">Reset Messages</b-button>
      
        <b-button v-if="!checkEmergency" type="submit" variant="outline-primary" size="lg" style="margin: 30px; font-size: 18pt;" >Send</b-button>
      </b-form>
      <b-button v-if="checkEmergency" v-on:click="cancelMessage" variant="primary" size="lg" style="margin: 30px; font-size: 18pt;">Cancel Message, I will call 9-1-1.</b-button>
      
      <b-button v-if="checkEmergency" v-on:click="onConfirm" variant="outline-primary" size="lg" style="margin: 30px; font-size: 18pt;">I confirm not an emergency, send message.</b-button>
      </div>
    <div>
      <h2>{{ resultMessage }}</h2>
    </div>

    <div>
    <table id="message-table">
      <thead>
        <tr>
          <th>Message</th>
          <th>Emergency</th>
          <th>Time Sent</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(message, index) in messages" :key="index">
          <td>{{message.message}}</td>
          <td>{{message.emergency}}</td>
          <td>{{message.time}}</td>
        </tr>
      </tbody>
    </table>
  </div>
  </div>
  
</template>

<script>
export default {
  name: 'Chat',
  props: {
    
  }
}
</script>
<script>
import axios from 'axios';
const api = axios.create({
    baseURL: process.env.VUE_APP_ROOT_API,
    timeout: 300000,
    withCredentials: false,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
});

export default {
  data() {
  return {
    messageForm: {
      message: '',
      isEmergency: false
    }, 
    messages: [], 
    resultMessage: '', 
    checkEmergency: false,
    prevMessage: ''
  }
},
  methods: {
    getMessages() {
      const path = '/v1/messages';
      console.log("Getting Messages")
      api.get(path)
        .then((res) => {
          this.messages = res.data.messages;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error("error");
        });
    },
  confirmMessage(payload) {
      const path = '/v1/nonemergency';
      api.post(path, payload)
        .then((response) => {
          this.getMessages();
          this.resultMessage = 'Sent!';
          this.checkEmergency = false;
          this.prevMessage = '';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMessages();
        });
  },
  cancelMessage() {
    this.resultMessage = 'Message Cancelled.';
    this.checkEmergency = false;
    this.prevMessage = '';
    this.initForm();
  },
  addMessage(payload) {
      
      const path = '/v1/messages';
      api.post(path, payload)
        .then((response) => {
          console.log(response.data.emergency);
          const emergency = response.data.emergency == 'True';
          if(emergency == true) {
            this.resultMessage = 'Is this an Emergency?';
            this.checkEmergency = true;
            this.prevMessage = response.data.message;
            this.messageForm.message = response.data.message + '\n \n Your message appears to need urgent attention.'+
            ' Please call the Nurse Triage Line at (919) - 999 - 9999 or call 9-1-1. If you believe you can wait for up'+
            ' to 3 days to receive a response, please continue.';
          } else {
            this.resultMessage = 'Sent!';
            this.checkEmergency = false;
          }
          this.getMessages();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMessages();
        });
    },
    initForm() {
      this.messageForm.message = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        message: this.messageForm.message
      };
      this.addMessage(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
      const path = '/v1/messages';
      const payload = {
        reset: 'true'
      };
      api.post(path, payload)
        .then((response) => {
          console.log(response);
          this.getMessages();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMessages();
        });
    },
    onConfirm(evt) {
      evt.preventDefault();
      const payload = {
        message: this.prevMessage,
        emergency: true,
        reset: 'false'
      };
      this.confirmMessage(payload);
      this.initForm();
    }
  },
  created() {
    this.getMessages();
  },
};

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

#message-table {
  font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 70%;
  margin-left: 15%;
  margin-right: 15%
}

#message-table td, #message-table th {
  border: 1px solid #ddd;
  padding: 8px;
}

#message-table tr:nth-child(even){background-color: #f2f2f2;}

#message-table tr:hover {background-color: #ddd;}

#message-table th {
  font-size: 20pt;
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #007bff;
  color: white;
}
#message-table tr {
  font-size: 16pt;
}
</style>
