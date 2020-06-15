from flask import render_template
from flask_mail import Message
from .extensions import mail

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_new_contact_form_email(contact_form):
    send_email('[Astrix] New Contact Form Submission',
               sender='john@johnlopez.org',
               recipients=['john@johnlopez.org'],
               text_body=render_template('emails/contact_form.txt',
                                         form=contact_form),
               html_body=render_template('emails/contact_form.html',
                                         form=contact_form))
