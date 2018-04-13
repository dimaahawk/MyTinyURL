import sys
import logging
import MySQLdb
import hashlib
import _mysql_exceptions
import url_shortener_queries

try:
    import secrets
except ImportError as e:
    print 'no secrets.py was found, please ensure you have the file present in the project root directory.\n'

logging.basicConfig(format='[%(asctime)s]:[%(levelname)s]:[%(filename)s %(lineno)d]:[%(funcName)s]:%(message)s')
logger = logging.getLogger('url_manager')
logger.setLevel(logging.DEBUG)


def is_linux_or_mac():
    '''
    It's a function that returns a string that is 'darwin' if your OS is mac.  Returns 'linux if your system is linux

    '''
    if ('linux' in sys.platform):
        return 'linux'
    elif ('darwin' in sys.platform):
        return 'darwin'
    else:
        print "Couldn't find 'linux' or 'darwin' as the OS so I am exiting"
        sys.exit(1)


def get_db_cursor_obj():
    if is_linux_or_mac() == 'linux':
        local_db_connection = MySQLdb.connect(host='localhost', user=secrets.LOCALHOST_DB['mytinyurl_user']
                                              , passwd=secrets.LOCALHOST_DB['mytinyurl_password'], db='mytinyurl')
    else:
        local_db_connection = MySQLdb.connect(host='localhost', user='root'
                                              , passwd='', db='mytinyurl')

    local_db_cursor = local_db_connection.cursor()
    return_obj = (local_db_connection, local_db_cursor)

    return return_obj


def return_query_results(sql_query):
    conn, cur = get_db_cursor_obj()
    logger.info('Running Query: {0}'.format(sql_query))
    cur.execute(sql_query)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def insert_new_row(sql_query):
    conn, cur = get_db_cursor_obj()
    logger.info('Running Query: {0}'.format(sql_query))
    cur.execute(sql_query)
    conn.commit()
    cur.close()
    conn.close()

    return True


def hash_new_url(url):
    url = url.strip()
    full_url_hash = hashlib.sha256(url).hexdigest()
    short_url_hash = full_url_hash[len(full_url_hash) - 10:]  # Get the last 10 characters from the hash
    return_tuple = (full_url_hash, short_url_hash, url)
    return return_tuple


def insert_new_url(url):
    insert_object = hash_new_url(url)
    full_hash = insert_object[0]
    short_hash = insert_object[1]
    insert_url = insert_object[2]
    query = url_shortener_queries.insert_new_url.format(full_hash, short_hash, insert_url)
    insert_new_row(query)

    return short_hash  # Pass back the short hash to give the user


def return_url_from_short_hash(short_url_hash):
    query = url_shortener_queries.get_url.format(short_url_hash)
    logger.info('Running Query for short code lookup: {0}'.format(query))
    query_results = return_query_results(query)
    logger.info('Query results: {0}'.format(query_results))

    if len(query_results) < 1:
        return False

    elif len(query_results) > 1:
        return False

    else:
        return_url = query_results[0][0]
        logger.info('Query returned: {0}'.format(query_results))
        logger.info('URL is: {0}'.format(return_url))

    return return_url
