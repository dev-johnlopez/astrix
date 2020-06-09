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
