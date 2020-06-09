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
    return "123"
