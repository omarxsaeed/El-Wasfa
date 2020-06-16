import secrets
import os
from PIL import Image
from flask import render_template, current_app
from flask_mail import Message
from elwasfa import mail
import boto3

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = "profile" + random_hex + f_ext
    s3 = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket('elwasfa-bucket').put_object(ACL='public-read', Key='profile/'+picture_fn, Body=form_picture)
    image_url = "https://elwasfa-bucket.s3.eu-central-1.amazonaws.com/profile/" + picture_fn
    return image_url

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('[El-Wasfa] Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.html = render_template("reset_mail.html", token=token)
    mail.send(msg)
