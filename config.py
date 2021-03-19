import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x9a\x88\xb3\x18\xd7a\xe4\xa4\xd9\x8d\x8a.\xee\xde\\\xfe'
    
    MONGODB_SETTINGS = {'db' : 'UTA_Enrollment'}
