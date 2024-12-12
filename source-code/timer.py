import time

startTime = time.time()
curTime = 0.0
latTime = 0.0
pauseTime = 0.0

##basic func
def start():
    global startTime
    startTime = time.time()

def pause():
    global curTime
    curTime = time.time()

def resume():
    global latTime
    latTime = time.time()
    global pauseTime
    pauseTime += latTime - curTime

def end():
    global startTime
    global curTime
    global latTime
    global pauseTime
    startTime = time.time()
    curTime = 0.0
    latTime = 0.0
    pauseTime = 0.0

##advanced func
def resumePreDetect():
    return time.time() - curTime

def pausePreDetect():
    return time.time() - latTime

def getPauseTime():
    return pauseTime

def getTotalTime():
    return time.time() - startTime - pauseTime

def fTime():
    minute = int(getTotalTime() / 60)
    second = int(getTotalTime() % 60)
    if 0 <= minute < 10:
        fMinute = str('0' + str(minute))
    elif 10 <= minute < 60:
        fMinute = str(minute)
    else:
        fMinute = 'fMinute_error'

    if 0 <= second < 10:
        fSecond = str('0' + str(second))
    elif 10 <= second < 60:
        fSecond = str(second)
    else:
        fSecond = 'fSecond_error'
    return fMinute, fSecond