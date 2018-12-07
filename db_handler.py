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


class DbHandler(object):

    def __init__(self):
        self.host = 'localhost'
        self.user = secrets.LOCALHOST_DB['mytinyurl_user']
        self.password = secrets.LOCALHOST_DB['mytinyurl_password']
        self.db = secrets.LOCALHOST_DB['mytinyurl_db']
        self.table = secrets.LOCALHOST_DB['mytinyurl_table']
        self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db)
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

    def insert_new_short_url(self, full_hash, short_hash, url, ip_address, user_agent):

        if self.get_url_from_short_hash(short_hash):
            logger.info('URL exists already... returning short hash: {}'.format(short_hash))
            return True

        query = url_shortener_queries.insert_new_url.format(self.table, full_hash, short_hash, url, ip_address, user_agent)
        logger.info('Running Query: {0}'.format(query))
        self.cur.execute(query)
        self.conn.commit()

        return True

    def increment_visit_by_short_hash(self, short_url_hash):
        query = url_shortener_queries.update_visits_by_short_hash.format(self.table, short_url_hash)
        logger.info('Running Query: {0}'.format(query))
        self.cur.execute(query)
        self.conn.commit()

        return True

    def get_url_from_short_hash(self, short_url_hash):
        query = url_shortener_queries.get_url.format(self.table, short_url_hash)
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
