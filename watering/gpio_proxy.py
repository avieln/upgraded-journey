BOARD=1
BCM=2
OUT=3
IN=4

def setup(num,mode):

    text = 'out' if mode==OUT else 'in'
    print('Proxy: setting channel ' + str(num) + ' to ' + text)


def output(num,val):
    print('Proxy: output channel ' + str(num) + ' to ' + str(val))


def input(num,val):
    print('Proxy: input channel ' + str(num) + ' to ' + str(val))


def cleanup():
    print('Proxy: Cleanup')

def setmode(mode):
    print('Proxy: setmode')