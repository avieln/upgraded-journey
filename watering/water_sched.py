import taps_control
from schedule import Scheduler
import threading
import time
import json
import os
import logging

def job_func(channel, duration,controller):

    def f():
        logging.info(thread.name + ' started channel ' + str(channel))
        controller.open_channel(channel_num=channel)
        time.sleep(duration)
        logging.info(thread.name +' finished job on channel ' + str(channel))
        controller.close_channel(channel_num=channel)

    thread = threading.Thread(target=f)
    thread.start()
    return


class Server:

    def __init__(self):
        self.scheduler = Scheduler()
        self.semaphore = threading.Semaphore()
        self.con = taps_control.TapsControl()
        self.read_config()

    def read_config(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
        with open(config_path, 'r') as f:
            data = json.load(f)
            for job in data.values():
                self.handle_job(job)

    def handle_job(self, job):
        when = job['when']
        con = self.con
        if when == 'daily':
            logging.info('Queued a daily job on channel '+ str(job['channel']))
            self.scheduler.every().day.at(job['start']).do(job_func, int(job['channel']), int(job['duration']), con)
        elif when == 'every':
            self.scheduler.every(int(job['interval'])).seconds.do(job_func, int(job['channel']), int(job['duration']),con)

        elif when == "other":
            self.scheduler.every(2).days.do(job_func, int(job['channel']), int(job['duration']),con)

    def run(self):

        while True:
            self.scheduler.run_pending()


log_file = os.path.join(os.path.dirname(__file__), 'log')
logging.basicConfig(level=logging.INFO, filename=log_file)

server = Server()

server.run()
