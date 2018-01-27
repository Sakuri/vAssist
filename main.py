import os
import  speech_recognition as sr
import time
import datetime

#Author Jiang
#Get file name
starttime = datetime.datetime.now()
i = 1
for name in os.listdir(r'C:\Users\szzhy\Desktop\Speech'):
    print("%d %s Starting..." % (i, name))
    # Audio Translation
    r = sr.Recognizer()
    # for i in range(kn):
    try:
        with sr.WavFile(r'C:\Users\szzhy\Desktop\Speech\%s' % name) as source:
            audio = r.record(source)
            text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='en-US')
            print(text)
            open(r'C:\Users\szzhy\Desktop\Speech\text\%s.txt' % name, 'a+').write(text)
            time.sleep(5)
            temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('%s %d %s Completed' % (temptime,i, name))

    except Exception as e:
        print(e)
        temptime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('%s %d %s Incomplete' % (temptime, i, name))
        continue
jtime = datetime.datetime.now()
last=jtime-starttime
print('Time Used：%s'%last)
