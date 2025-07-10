import speech_recognition as sr
import os
import webbrowser
import datetime
import pywhatkit
import wikipedia
import subprocess
import pyjokes
from flask import Flask, request, jsonify, render_template



USER = "Master"
BOT = "Assistant"

app = Flask(__name__)


def say(text):
    os.system(f"say {text}")

def greet_me():
    hour = datetime.datetime.now().strftime("%H")
    hour = int(hour)
    if (hour>= 4) and (hour < 12):
        print(f"Good morning {USER}")
        subprocess.run(["say", f"Good morning {USER}"])
    elif (hour >= 12) and (hour < 16):
        print(f"Good afternoon {USER}")
        subprocess.run(["say", f"Good afternoon {USER}"])
    elif (hour >= 16) and (hour < 19):
        print(f"Good evening {USER}")
        subprocess.run(["say", f"Good evening {USER}"])
    else :
        print(f"Hello {USER}")
        subprocess.run(["say", f"Hello {USER}"])
    print(f"I am {BOT}.How may i assist you {USER}?")
    subprocess.run(["say", f"I am {BOT}.How may i assist you {USER}?"])


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            print(e)
            return ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command')
    response = handle_command(command)
    return jsonify({'response': response})


def handle_command(query):
        if not query:
            return
        # todo: Add more sites
        sites=[["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["facebook","https://www.facebook.com/"],
            ["chatgpt","https://chat.openai.com/"],
            ["instagram","https://www.instagram.com/"],
            ["imdb","https://www.imdb.com/"],
            ["ibomma","https://film.ibomma.name/telugu-movies/"],
            ["ipl","https://www.iplt20.com/"],
            ["apple","https://www.apple.com/in/iphone/"],
            ["microsoft","https://www.microsoft.com/en-in/"],
            ["amazon","https://www.amazon.in/"],
            ["flipkart","https://www.flipkart.com"],
            ["smashkarts","https://smashkarts.io/"],
            ["mysql","https://www.mysql.com"],
            ["Dev C","https://www.bloodshed.net"],
            ["java","https://www.java.com/en/download/"],
            ["jiocinema","https://www.jiocinema.com/"],
            ["jiomart","https://www.jiomart.com/"],
            ["vivo","https://www.vivo.com/in/"],
            ["oppo","https://www.oppo.com/in/"],
            ["motorola","https://www.motorola.in/"],
            ["nothing","https://in.nothing.tech/"],
            ["oneplus","https://www.oneplus.in/"],
            ["sbi bank","https://sbi.co.in/"],
            ["icici bank","https://www.icicibank.com/"],
            ["mlrit","https://erp.mlrinstitutions.ac.in/"],
            ["irctc","https://www.irctc.co.in/nget/train-search"],
            ["redbus","https://www.redbus.in/"],
            ["abhibus","https://www.abhibus.com/"],
            ["bookmyshow","https://in.bookmyshow.com/"],
            ["insider","https://insider.in/online"],
            ["airindia","https://www.airindia.com/"],
            ["airways","https://www.qatarairways.com/"],
            ["bitcoin","https://bitcoin.org/en/"],
            ["medplus","https://www.medplusmart.com/"],
            ["rapido","https://rapido.bike/"],
            ["olacabs","https://www.olacabs.com/"],
            ["uber","https://www.uber.com/in/en/ride/"],
            ["bigbasket","https://www.bigbasket.com/"],
            ["zepto","https://www.zeptonow.com/"],
            ["blinkit","https://blinkit.com/"],
            ["tsbie","https://results.cgg.gov.in"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} {USER}")
                webbrowser.open(site[1])
        playlist = []
        # todo: Add a feature to play a specific song
        if "play" and "from music" in query:
            musicPath = "/Users/gundigaabhishek/Downloads/speed-122837.mp3"
            os.system(f"open {musicPath}")

        if "exit" in query or "stop" in query:
            say(f"Have a nice day {USER},Take care!")
            exit()

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir time is {strfTime} {USER} ")
            say(f" time is {strfTime} {USER}")

        if "the date" in query:
            strf = datetime.datetime.now().strftime("%d:%m:%Y")
            print(f"the date is {strf} {USER}")
            say(f" the date is {strf} {USER}")

        apps=[["WhatsApp", "/Applications/WhatsApp.app"],
            ["Asphalt", "/Applications/Asphalt9.app"],
            ["Facetime", "/System/Applications/FaceTime.app"],
            ["Photobooth","/System/Applications/Photo Booth.app"],
            ["Anaconda","/Applications/Anaconda-Navigator.app"],
            ["App store","/System/Applications/App Store.app"],
            ["Arduino","/Applications/Arduino IDE.app"],
            ["Automator","/System/Applications/Automator.app"],
            ["Books","/System/Applications/Books.app"],
            ["Calculator","/System/Applications/Calculator.app"],
            ["Calendar","/System/Applications/Calendar.app"],
            ["Chess","/System/Applications/Chess.app"],
            ["Clock","/System/Applications/Clock.app"],
            ["Contacts","/System/Applications/Contacts.app"],
            ["Dictionary","/System/Applications/Dictionary.app"],
            ["Discord","/Applications/Discord.app"],
            ["Recorder","/Applications/eXtra Voice Recorder.app"],
            ["Find my","/System/Applications/FindMy.app"],
            ["Font Book","/System/Applications/Font Book.app"],
            ["Freeform","/System/Applications/Freeform.app"],
            ["GarageBand","/Applications/GarageBand.app"],
            ["Chrome","/Applications/Google Chrome.app"],
            ["Home","/System/Applications/Home.app"],
            ["Image capture","/System/Applications/Image Capture.app"],
            ["iMovie","/Applications/iMovie.app"],
            ["JetBrains","/Applications/JetBrains Toolbox.app"],
            ["Keynote","/Applications/Keynote.app"],
            ["Launchpad","/System/Applications/Launchpad.app"],
            ["Mail","/System/Applications/Mail.app"],
            ["Maps","/System/Applications/Maps.app"],
            ["Messages","/System/Applications/Messages.app"],
            ["Excel","/Applications/Microsoft Excel.app"],
            ["OneNote","/Applications/Microsoft OneNote.app"],
            ["Outlook","/Applications/Microsoft Outlook.app"],
            ["MSPoint","/Applications/Microsoft PowerPoint.app"],
            ["Teams","/Applications/Microsoft Teams classic.app"],
            ["Word","/Applications/Microsoft Word.app"],
            ["Control","/System/Applications/Mission Control.app"],
            ["MyCaptain","/Applications/MyCaptain.app"],
            ["Notes","/System/Applications/Notes.app"],
            ["Numbers","/Applications/Numbers.app"],
            ["OneDrive","/Applications/OneDrive.app"],
            ["Pages","/Applications/Pages.app"],
            ["Photos","/System/Applications/Photos.app"],
            ["Podcasts","/System/Applications/Podcasts.app"],
            ["Preview","/System/Applications/Preview.app"],
            ["PyCharm","/Applications/PyCharm CE.app"],
            ["QuickTime","/System/Applications/QuickTime Player.app"],
            ["Reminders","/System/Applications/Reminders.app"],
            ["Safari","/Applications/Safari.app"],
            ["Shortcuts","/System/Applications/Shortcuts.app"],
            ["Siri","/System/Applications/Siri.app"],
            ["Stickies","/System/Applications/Stickies.app"],
            ["Stocks","/System/Applications/Stocks.app"],
            ["Settings","/System/Applications/System Settings.app"],
            ["TeamViewer","/Applications/TeamViewer.app"],
            ["TextEdit","/System/Applications/TextEdit.app"],
            ["Time Machine","/System/Applications/Time Machine.app"],
            ["TV","/System/Applications/TV.app"],
            ["VoiceMemos","/System/Applications/VoiceMemos.app"],
            ["Weather","/System/Applications/Weather.app"]]

        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]} sir...")
                os.system(f"open {app[1]}")

        if "play the video of" in query or "play" and "on YouTube" in query:
            song = query.replace("play", "")
            say("playing" + song)
            pywhatkit.playonyt(song)

        if "tell me about" in query or "who is" in query:
            human = ((query.replace("who is", ""))
                     or ((query.replace("tell me about", ""))))
            text = wikipedia.summary(human, 1)
            print(text)
            subprocess.run(["say", text])

        if "search" in query:
            look = query.replace("search","")
            res = pywhatkit.search(look)

        if "joke" in  query or "make me laugh" in query:
            joke=pyjokes.get_joke()
            print(joke)
            subprocess.run(["say",joke])

        if "save information on" in query or "save Information on" in query:
            human = query.replace("save information on", "")
            text = wikipedia.summary(human, 10)
            if not os.path.exists("Results"):
                os.mkdir("Results")
            with open (f"Results/{''.join(query.split('on')[1:])}.txt","w") as f:
                f.write(text)



if __name__ == '__main__':
    greet_me()
    from threading import Thread

    server_thread = Thread(target=lambda: app.run(debug=True, use_reloader=False))
    server_thread.start()
    while True:
        command = takeCommand()
        handle_command(command)





