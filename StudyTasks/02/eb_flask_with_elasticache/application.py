from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap

# EB looks for an 'application' callable by default.
application = Flask(__name__)
bootstrap = Bootstrap(application)

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/<name>')
def user(name):
    return render_template('user.html', name=name)

@application.route('/elasticache', methods=['GET', 'POST'])
def elasticache():
    cache_value = None
    if request.method == 'POST' and 'posted_cache_value' in request.form:
        cache_value = request.form['posted_cache_value']
    return render_template('elasticache.html', posted_cache_value=cache_value)

# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run(host='0.0.0.0')
