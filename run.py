import logging
import url_manager
from flask import Flask, redirect, request, render_template, make_response

logging.basicConfig(format='[%(asctime)s]:[%(levelname)s]:[%(filename)s %(lineno)d]:[%(funcName)s]:%(message)s')
logger = logging.getLogger('run')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('home.html')


@app.route('/404/')
def page_not_found():
    return '404'


@app.route('/add/', methods=['POST'])
def add_url():
    input_url = request.form['input_url']
    if input_url:
        logger.info('Params: {0}'.format(input_url))
        short_url_hash = url_manager.insert_new_url(input_url)
        return render_template('new_url_return.html', short_url_hash=short_url_hash)

    else:
        return 'EMPTY REQUEST'


@app.route('/s/')
def empty_lookup():
    return 'EMPTY REQUEST'


@app.route('/s/<string:short_url_hash>/')
def url_lookup(short_url_hash):
    redirect_url = url_manager.return_url_from_short_hash(short_url_hash)
    logger.info('Sending back: {0}'.format(redirect_url))
    if not redirect_url:
        return 'INVALID LOOKUP'
    else:
        return redirect(redirect_url, code=302)


@app.route('/foo/', methods=['GET', 'POST'])
def foo():
    headers, cookies = request.headers, request.cookies
    # logger.info('Headers: {0}'.format(headers))
    logger.info('Cookies: {0}'.format(cookies))
    resp = make_response('HELLO WORLD!')
    # resp = make_response(render_template('new_url_return.html', short_url_hash='foobar'))
    resp.set_cookie('urluid', value='testing01')
    resp.set_cookie('sessId', value='abc')
    resp.headers['X-HELLO'] = 'monkey'

    return resp


if __name__ == '__main__':
    app.run(debug=True)
