import RPi.GPIO as GPIO

class TapsControl:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)

    def get_channels(self):
        pass

    @staticmethod
    def open_channel(channel_num):
        GPIO.ouput(channel_num, 1)
        print('Opening channel ' + str(channel_num))

    @staticmethod
    def close_channel(self, channel_num):
        GPIO.ouput(channel_num, 0)
        print('Closing channel ' + str(channel_num))