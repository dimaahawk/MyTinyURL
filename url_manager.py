import logging
import hashlib
from db_handler import DbHandler

try:
    import secrets
except ImportError as e:
    print 'no secrets.py was found, please ensure you have the file present in the project root directory.\n'

logging.basicConfig(format='[%(asctime)s]:[%(levelname)s]:[%(filename)s %(lineno)d]:[%(funcName)s]:%(message)s')
logger = logging.getLogger('url_manager')
logger.setLevel(logging.DEBUG)

class UrlManager(object):

    def __init__(self):
        pass

    def hash_url(self, url):
        url = url.strip()
        full_url_hash = hashlib.sha256(url).hexdigest()
        short_url_hash = full_url_hash[len(full_url_hash) - 10:]  # Get the last 10 characters from the hash
        return_tuple = (full_url_hash, short_url_hash, url)
        return return_tuple

    def is_url_valid(self, url):
        if url.startswith('http://') or url.startswith('https://'):
            return True
        else:
            return False

    def put_new_url(self, incoming_request):
        incoming_url = incoming_request.form['input_url']
        if self.is_url_valid(incoming_url):
            ua = incoming_request.headers['User-Agent']
            ip = incoming_request.remote_addr
            full_hash, short_hash, url = self.hash_url(incoming_url)

            with DbHandler() as db:
                db.insert_new_short_url(full_hash, short_hash, url, ip, ua)
            return short_hash

        else:
            return False

    def get_url_by_short_hash(self, short_url_hash):
        with DbHandler() as db:
            return_url = db.get_url_from_short_hash(short_url_hash)
            db.increment_visit_by_short_hash(short_url_hash)

        return return_url
