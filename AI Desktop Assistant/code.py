import speech_recognition as sr
import wikipedia
import openai
import pyaudio
import os


def say(text):
    os.system(f"Say {text}")

if __name__ == "__main__":
    print("Hello")
    say("Hello I am Jarvis A.I")