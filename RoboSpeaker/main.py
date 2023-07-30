import os
import pyttsx3

if __name__ == '__main__':
    text_speech = pyttsx3.init()
    text_speech.say("HELLO IM JARVIS and I Was Created By rishav"
                    "How may I help you")
    text_speech.runAndWait()

    print("Welcome to ROBOSpeaker Created by Rishav")

    while True:

        x = input("Enter what do you want me to speak or if you want to exit the program just enter 'q': ")
        if x == "q":
            text_speech.say("Bye Bye friend")
            text_speech.runAndWait()
            break
        text_speech.say(x)
        text_speech.runAndWait()




