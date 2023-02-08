from Core.jobs import *
from Core.todo_route import todo
from Utils.wawu_logger import logger_init

from flask import Flask
from flask_cors import *
from flask_apscheduler import APScheduler


class Config(object):
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    
logger_init()

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(todo)
CORS(app, supports_credentials=True)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.add_job(id="auto_send_email", func=auto_send_email, trigger='cron', day='*', hour='06', minute='30', second='00')
scheduler.start()
