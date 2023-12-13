import os

class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'any secret key'

    # MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment'}