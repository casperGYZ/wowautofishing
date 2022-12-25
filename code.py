import math
import time
from collections import deque
import pyaudio
import audioop
import pyautogui
import random
import cv2
import mss as mss
import numpy as np

def listen():
    print('Well, now we are listening for loud sounds...')
    CHUNK = 1024  # CHUNKS of bytes to read each time from mic
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 18000
    THRESHOLD = 700  # The threshold intensity that defines silence
    # and noise signal (an int. ]lower than THRESHOLD is silence).
    SILENCE_LIMIT = 1  # Silence limit in seconds. The max ammount of seconds where
    # only silence is recorded. When this time passes the
    # recording finishes and the file is delivered.
    # Open stream
    p = pyaudio.PyAudio()


    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                   input_device_index=0)
    cur_data = ''  # current chunk  of audio data
    rel = RATE / CHUNK
    # print(rel)
    slid_win = deque(maxlen=SILENCE_LIMIT * int(rel))
    cur_data = stream.read(CHUNK)
    slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
    slid_win = deque(maxlen=SILENCE_LIMIT * int(rel))

    success = False
    listening_start_time = time.time()
    while True:
        try:
            cur_data = stream.read(CHUNK)
            slid_win.append(math.sqrt(abs(audioop.avg(cur_data, 4))))
            if (sum([x > THRESHOLD for x in slid_win]) > 0):
                print('I heart something!')
                success = True
                break
            if time.time() - listening_start_time > 20:
                print('I don\'t hear anything already 20 seconds!')
                break
        except IOError:
            break

    # print "* Done recording: " + str(time.time() - start)
    stream.close()
    p.terminate()
    return success


mon = {'top':1,'left':1,'width':1920, 'height':1080}

sct = mss.mss()

goudan_img = cv2.imread('needle.png', cv2.IMREAD_UNCHANGED)
w = goudan_img.shape[1]
h = goudan_img.shape[0]

threshold = 0.8


while 1:
    sct_img = np.array(sct.grab(mon))
    result = cv2.matchTemplate(sct_img, goudan_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    yloc, xloc = np.where(result >= threshold)
    rectangles = []
    time.sleep(round(random.uniform(1, 2)))
    pyautogui.press(']')
    if listen() == True:
        time.sleep(round(random.uniform(0.5, 1.3)))
        pyautogui.press('[')
    else:
        continue

    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles,1,0.2)

    for (x, y, w, h) in rectangles:
        cv2.rectangle(sct_img, (x,y), (x + w, y + h), (0, 255, 0), 2)
        pyautogui.click((x + 1 + w/2),(y - 5 + h/2))
        time.sleep(10)
        pyautogui.click((x + 1 + w / 2), (y + 1 + h * 7 / 8))
        time.sleep(10)
        pyautogui.click((x + 1 + w / 2), (y + 1 + h * 7 / 8))
        time.sleep(20)
        pyautogui.click(945,983)
        time.sleep(20)
        pyautogui.click(945, 983)
        time.sleep(1)
        pyautogui.click(945, 983)
        time.sleep(1)
        pyautogui.click(945, 983)
