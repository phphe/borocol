import sys
sys.path.append('./')
import config as appConfig

bind = '127.0.0.1:8000'      #绑定ip和端口号
workers = 4
errorlog = './gunicorn.log'
loglevel = 'debug' if appConfig.debug else 'error'
