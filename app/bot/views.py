import logging
import json
from flask import Blueprint, current_app, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from .util import detect_intent_texts, detect_intent_knowledge
from app.extensions import csrf_protect

blueprint = Blueprint('bot', __name__, url_prefix='/bot')


# logging.getLogger('flask_assistant').setLevel(logging.DEBUG)


@blueprint.route('/twilio', methods=['POST'])
@csrf_protect.exempt
def twilio():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    intent = detect_intent_knowledge(project_id="astrix",
                                 session_id="123",
                                 texts=[incoming_msg],
                                 language_code="en-US")
    msg.body(intent.query_result.fulfillment_text)
    responded = True
    return str(resp)

@blueprint.route('/web', methods=['POST'])
@csrf_protect.exempt
def web():
    incoming_msg = request.values.get('msg')
    print(incoming_msg)
    intent = detect_intent_texts(project_id="astrix",
                                 session_id="123",
                                 texts=[incoming_msg],
                                 language_code="en-US")
    return intent.query_result.fulfillment_text

@blueprint.route('/twilio_old', methods=['POST'])
@csrf_protect.exempt
def twilio_old():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)

@blueprint.route('/new_lead', methods=['POST'])
@csrf_protect.exempt
def new_lead():
    incoming_msg = request.values.get('Body', '').lower()
    print(request)
    return
