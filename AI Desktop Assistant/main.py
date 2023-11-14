import speech_recognition as sr
import subprocess
import webbrowser
import os
from datetime import datetime
from openai import OpenAI
from config import apikey

chatStr = ""


def chat(query):
    global chatStr

    client = OpenAI(api_key=apikey)

    chatStr += f"Harry: {query}\n Jarvis: "
    try:
        response = client.completions.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
    except Exception as e:
        print(e)

    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"


def ai(query):
    client = OpenAI(api_key=apikey)
    text = (
        f"OpenAI response for query: {query}\n------------------------------------n\n"
    )

    try:
        response = client.completions.create(
            model="text-davinci-003",
            prompt=query,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
    except Exception as e:
        print(e)

    try:
        text += response["choices"][0]["text"]
    except Exception as e:
        print("Some error occured")

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    file_name = "_".join(str(query).lower().split("intelligence")[1:].strip().split())
    with open(f"Openai/{file_name}.txt", "w") as f:
        f.write(text)


def say(text):
    subprocess.run(
        ["espeak", text]
    )  # This is specificly for ubuntu, install espeak using sudo command


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 1568
        r.dynamic_energy_threshold = True
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occured, Sorry from Jarvis"


if __name__ == "__main__":
    print("Hello")
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening...")
        query = take_command()

        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.com",
            "google": "https://www.google.com",
            "linkedin": "https://www.linkedin.com",
            "instagram": "https://www.instagram.com",
            "facebook": "https://www.facebook.com",
            "chatgpt": "https://chat.openai.com/",
        }

        for site, url in sites.items():
            if f"open {site.lower()}".lower() in query.lower():
                say(f"Opening {site} Sir...")
                webbrowser.open(url)

        if "play music" in query.lower():
            music_path = "dreams.mp3"
            os.system(f"open {music_path}")

        elif "time now" in query.lower():
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Current time is: {current_time}")
            say(f"Sir the time is {current_time}")

        elif "current date" in query.lower():
            current_date = datetime.now().strftime("%d/%m/%y")
            print(f"Current date is: {current_date}")
            say(f"Sir the date is {current_date}")

        elif "using artificial intelligence" in query.lower():
            ai(query)

        elif "jarvis quit" in query.lower():
            exit()

        elif "reset chat" in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
