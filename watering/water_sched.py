import taps_control
from schedule import Scheduler
import threading
import time
import json


def job_func(channel, duration):

    def f():
        print(thread.name + ' started channel ' + str(channel))
        taps_control.TapsControl.open_channel(channel_num=channel)
        time.sleep(duration)
        print( thread.name +' finished channel ' + str(channel))
        taps_control.TapsControl.open_channel(channel_num=channel)

    thread = threading.Thread(target=f)
    thread.start()
    return


class Server:

    def __init__(self):
        self.scheduler = Scheduler()
        self.semaphore = threading.Semaphore()
        server.read_config()

    def read_config(self):
        with open('config.json', 'r') as f:
            data = json.load(f)
            for job in data.values():
                self.handle_job(job)

    def handle_job(self, job):

        when = job['when']
        start = job['start']

        if when == 'daily':
            self.scheduler.every().day.at(start).do(job_func, int(job['channel']), int(job['duration']))
            self.scheduler.every().minute.do(job_func, int(job['channel']), 0.5)
        else:
            getattr(self.scheduler.every(), when).at(start).do(job_func, int(job['channel']), int(job['duration']))

    def run(self):

        while True:
            self.scheduler.run_pending()


server = Server()

server.run()