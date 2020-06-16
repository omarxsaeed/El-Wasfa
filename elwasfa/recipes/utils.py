import os
import secrets
from flask import current_app
from PIL import Image
import boto3

def save_recipe_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = "recipe" + random_hex + f_ext
    s3 = boto3.client('s3', aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'))
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket('elwasfa-bucket').put_object(ACL='public-read', Key='recipe/'+picture_fn, Body=form_picture)
    image_url = "https://elwasfa-bucket.s3.eu-central-1.amazonaws.com/recipe/" + picture_fn
    return image_url

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True

