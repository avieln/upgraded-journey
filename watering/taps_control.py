from RPi import GPIO as GPIO

class TapsControl:

    	def __init__(self):
        	GPIO.setmode(GPIO.BOARD)
	        GPIO.setup(7, GPIO.OUT)
		GPIO.setup(11,GPIO.OUT)
		GPIO.setup(13,GPIO.OUT)

	def get_channels(self):
        	pass

	@staticmethod
	def open_channel(channel_num):
        	GPIO.output(channel_num, 1)
	        print('Opening channel ' + str(channel_num))

	@staticmethod
	def close_channel(channel_num):
        	GPIO.output(channel_num, 0)
        	print('Closing channel ' + str(channel_num))

	def  __del__(self):
		GPIO.cleanup()


