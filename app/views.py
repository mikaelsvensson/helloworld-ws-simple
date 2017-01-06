import time

from app import application

@application.route('/')
def index():
    return "Hej"

@application.route('/time')
def show_time():
    return time.strftime("%c")