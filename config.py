import os

class Config(object):
   SECRET_KEY = os.environ.get("SECRET_KEY") or "b'8k\xc0\xcc\x95\xf5\xe6\xb4*z\x05\xc9K\xb6L\x8d'"
   MONGODB_SETTINGS={'db':'UTA_Enrollment'}
