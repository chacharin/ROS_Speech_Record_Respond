#!/usr/bin/env python

from datetime import datetime

import rospy
from std_msgs.msg import String
from gtts import gTTS
import os

def callback(data):
    global recive_speech
    recive_speech = data.data
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


    if(recive_speech == "hello"):
        say_answer("Hello, how are you to day?")
    
    if(recive_speech == "how are you"):
        say_answer("Am fine, Thank you")
    
    if(recive_speech == "what's your name"):
        say_answer("My name is: Robot--Talking")

    if(recive_speech == "what time is it"):
        now = datetime.now()
        H_str = now.strftime("%H")
        M_str = now.strftime("%M")
        say_answer(H_str+"hour and!  "+M_str+" minute")
    

    
def listen():
    global DATA
    rospy.init_node('comsay', anonymous=True)
    rospy.Subscriber("result", String, callback)
    rospy.spin()

def say_answer(input_str):
    text = input_str
    tts = gTTS(text)
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
    os.remove("speech.mp3")


if __name__ == '__main__':
    listen()
     
    