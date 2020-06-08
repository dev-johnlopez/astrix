import logging
import requests
import json
from flask import Blueprint, current_app, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
from .util import detect_intent_texts

blueprint = Blueprint('bot', __name__, url_prefix='/bot')

#logging.getLogger('flask_assistant').setLevel(logging.DEBUG)

@blueprint.route('/twilio', methods=['POST'])
def twilio():
    resp = twiml.Response()
    resp.message('Hello, you said: nothing')
    return str(resp)
    #print("=======")
    #print("=======")
    #print("=======")
    #print("=======")
    #print("=======")
    #incoming_msg = request.values.get('Body', '').lower()
    #print("=======")
    #print(str(request.values))
    #print("=======")
    #resp = MessagingResponse()
    #msg = resp.message()
    #responded = False
    #intent = detect_intent_texts(project_id="autumn-wkhetw",
    #                               session_id="123",
    #                               texts=[incoming_msg],
    #                               language_code="en-US")
    #msg.body(intent.query_result.fulfillment_text)
    #responded = True
    #return str(resp)
