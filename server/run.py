# module
from flask import Flask
from cassandra.cqlengine import connection
# file
import config
from config import db_keyspace, db_host, debug, app_host, app_port
from utils import str_rand

# func
controllerInstanceMap = {}
def getControllerInstance(ctl):
    key = str(id(ctl))
    if key not in controllerInstanceMap:
        controllerInstanceMap[key] = ctl()
    return controllerInstanceMap[key]

# connect databse
try:
    connection.setup([db_host], db_keyspace, lazy_connect=True)
    print("Make connection to DB lazily")
except Exception as e:
    print("Error: connection db failed")
    raise

# init app
app = Flask(__name__, static_url_path='/static')
# inject config to app
configNames = [item for item in dir(config) if not item.startswith("__")]
for name in configNames:
    app.config[name] = config.__dict__[name]
app.config['MAX_CONTENT_LENGTH'] = app.config['request_maxContentLength']

# register routes
with app.app_context():
    from routes import routes
    from middlewares import globalMiddlewares
    # for loop hasn't scope, so put loop code into func
    def resolveRoute(item):
        ctlInstance = getControllerInstance(item['controller'])
        originalAction = getattr(ctlInstance, item['action'])
        middlewares = globalMiddlewares
        if 'middlewares' in item:
            middlewares = middlewares + item['middlewares']
        def action(*args, **kwargs):
            next = originalAction
            for mdl in middlewares:
                oldNext = next
                def nextFunc(*args, **kwargs):
                    return mdl(oldNext, *args, **kwargs)
                next = nextFunc
            return next(*args, **kwargs)
        endPoint = item['name'] if 'name' in item else str_rand(4)
        app.add_url_rule(item['path'], endPoint, view_func=action, methods=item.get('methods', ['GET']))
    for item in routes:
        resolveRoute(item)

# bootstrap app
if __name__ == '__main__':
    app.run(host=app_host,port=app_port, debug=debug, threaded=True)
