import taps_control
from schedule import Scheduler
import threading
import time
import json
import os

def job_func(channel, duration,controller):

    def f():
        print(thread.name + ' started channel ' + str(channel))
        controller.open_channel(channel_num=channel)
        time.sleep(duration)
        print( thread.name +' finished channel ' + str(channel))
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
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.json')
        with open(config_path, 'r') as f:
            data = json.load(f)
            print(data)
            for job in data.values():
                self.handle_job(job)

    def handle_job(self, job):
        when = job['when']
        start = job['start']
        con = self.con
        if when == 'daily':
            print('Queued a daily job on channel '+ str(job['channel']))
            self.scheduler.every(15).seconds.do(job_func, int(job['channel']), 0.01, con)
        else:
            getattr(self.scheduler.every(), when).at(start).do(job_func, int(job['channel']), int(job['duration']))

    def run(self):

        while True:
            self.scheduler.run_pending()


server = Server()

server.run()
