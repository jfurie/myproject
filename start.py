from flask import Flask
app = Flask(__name__)

#Logging
import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler('logger.log',mode='a', maxBytes=500,backupCount=20)
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)
from logging import Formatter
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))

#Routing
@app.route('/')
def hello_world():
    return 'Hello World 0!'

@app.route('/echo/<echo>')
def echo(echo):
	from pymongo  import MongoClient
	client = MongoClient('mongodb://appuser:{PASSWORD}@widmore.mongohq.com/furieTest', 10000)
	db = client.furieTest
	collection = db.test_collection
	import datetime
	post = {"author": "Me",
		"text": "Echo! %s" % echo,
		"tags": ["mongodb", "python", "pymongo"],
		"date": datetime.datetime.utcnow()}
	posts = db.posts
	post_id = posts.insert(post)
	app.logger.warn(echo)
	return 'Echo %s' % echo

if __name__ == '__main__':
    app.run(debug = True)