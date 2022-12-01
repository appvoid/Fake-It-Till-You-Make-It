from threading import Timer
class new:
    def __init__(self): pass
    def wait(self,time,callback):
        Timer(time,callback).start()