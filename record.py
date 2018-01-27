import sys, threading
import pyaudio
import wave
import os
import speech_recognition as sr
import time
import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout,
    QPushButton)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"
RECORDING = False

def translate():
    starttime = datetime.datetime.now()
    i = 1
    name = "output.wav"
    print("%d %s Starting..." % (i, name))
    # Audio Translation
    r = sr.Recognizer()
    # for i in range(kn):
    try:
        with sr.WavFile(r'C:\Users\szzhy\PycharmProjects\vAssist\%s' % name) as source:
            audio = r.record(source)
            IBM_USERNAME = 'dcd61475-3c91-4a93-a12a-65d8099e8c03'
            IBM_PASSWORD = 'xxEb2kIejISc'
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='en-US')
            print(text)
            open(r'C:\Users\szzhy\Desktop\Speech\text\%s.txt' % name, 'a+').write(text)
            time.sleep(5)
            temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%s %d %s Completed' % (temptime, i, name))
    except Exception as e:
        print(e)
        temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s %d %s Incomplete' % (temptime, i, name))
    jtime = datetime.datetime.now()
    last = jtime - starttime
    print('Time Used：%s' % last)

def record_thread(fileName, stream, p):
    print('Recording')
    waveFile = wave.open(fileName, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(p.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    while RECORDING:
        waveFile.writeframes(stream.read(CHUNK))
    waveFile.close()
    print('Ended')
    translate()

def record_generator(fileName, recordBtn):
    global RECORDING
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
        channels=CHANNELS, rate=RATE,
        input=True, frames_per_buffer=CHUNK)
    while 1:
        recordBtn.setText(u'Start')
        yield
        recordBtn.setText(u'Stop')
        RECORDING = True
        t = threading.Thread(target=record_thread, args=(fileName, stream, p))
        t.setDaemon(True)
        t.start()
        yield
        RECORDING = False

app = QApplication(sys.argv)
mainWindow = QWidget()
layout = QVBoxLayout()
btn = QPushButton()
g = record_generator('output.wav', btn)
next(g)
btn.pressed.connect(lambda: next(g))
layout.addWidget(btn)
mainWindow.setLayout(layout)
mainWindow.show()
sys.exit(app.exec_())