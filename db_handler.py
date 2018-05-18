import sys
import logging
import MySQLdb
import url_shortener_queries

try:
    import secrets
except ImportError as e:
    print 'no secrets.py was found, please ensure you have the file present in the project root directory.\n'

logging.basicConfig(format='[%(asctime)s]:[%(levelname)s]:[%(filename)s %(lineno)d]:[%(funcName)s]:%(message)s')
logger = logging.getLogger('db_handler')
logger.setLevel(logging.DEBUG)


HOST = 'localhost'
USER = secrets.LOCALHOST_DB['mytinyurl_user']
PASSWORD = secrets.LOCALHOST_DB['mytinyurl_password'] if secrets.LOCALHOST_DB.has_key('mytinyurl_password') else ''
DB = 'mytinyurl'


def is_linux_or_mac():
    '''
    It's a function that returns a string that is 'darwin' if your OS is mac. 
    Returns 'linux if your system is linux
    '''
    if ('linux' in sys.platform):
        return 'linux'
    elif ('darwin' in sys.platform):
        return 'darwin'
    else:
        print "Couldn't find 'linux' or 'darwin' as the OS so I am exiting"
        sys.exit(1)


class DbHandler(object):

    def __init__(self):
        if is_linux_or_mac() == 'linux':
            self.conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, db=DB)
        else:
            self.conn = MySQLdb.connect(
                host=HOST, user=USER, passwd='', db=DB
            )

        self.cur = self.conn.cursor()

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur:
            self.cur.close()

        if self.conn:
            self.conn.close()

    def run_adhoc_select_query(self, sql_query):
        logger.info('Running Ad Hoc Query: {0}'.format(sql_query))
        self.cur.execute(sql_query)
        results = self.cur.fetchall()
        return results

    def get_query_results(self, sql_query):
        logger.info('Running Query: {0}'.format(sql_query))

    def insert_new_short_url(self, full_hash, short_hash, url):
        query = url_shortener_queries.insert_new_url.format(full_hash, short_hash, url)
        logger.info('Running Query: {0}'.format(query))
        self.cur.execute(query)
        self.conn.commit()
        return True

    def get_url_from_short_hash(self, short_url_hash):
        query = url_shortener_queries.get_url.format(short_url_hash)
        logger.info('Running Query: {0}'.format(query))
        self.cur.execute(query)
        query_results = self.cur.fetchall()

        if len(query_results) < 1 or len(query_results) > 1:
            return False
        else:
            return_url = query_results[0][0]
            logger.info('Query returned: {0}'.format(query_results))
            logger.info('URL is: {0}'.format(return_url))

        return return_url

    def increment_visit_by_short_hash(self, short_url_hash):
        query = url_shortener_queries.update_visits_by_short_hash.format(short_url_hash)
        logger.info('Running Query: {0}'.format(query))
        self.cur.execute(query)
        self.conn.commit()
        return True

if __name__ == '__main__':
    with DbHandler() as db:
        db.increment_visit_by_short_hash('1cf23604e5')