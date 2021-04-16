import JarvisAI
import re
import pprint
import random
import smtplib
import pyowm

isOn = True

obj = JarvisAI.JarvisAssistant()

# res = obj.setup()


def t2s(text):
    obj.text2speech(text)


def randomizer(arr):
    return random.choice(arr)


# weather
OpenWmapApikey = 'b114494f3d13c1171b52683221bc69cf'
# hotkeys
weathHotKeys = 'weather|temperature'
# messages
currentWeather = "Weather is currently"
averageTempWeather = "Average Temp. Currently "


# funtion
def getWeather(city):
    OpenWMap = pyowm.OWM(OpenWmapApikey)
    mgr = OpenWMap.weather_manager()
    Weather = mgr.weather_at_place(city)
    Data = Weather.weather
    curWeath = Data.detailed_status
    aveTem = Data.temperature(
        'celsius')['temp']
    print(currentWeather, curWeath)
    t2s(f"{currentWeather}, {curWeath}")
    print(averageTempWeather, aveTem)
    t2s(f"{averageTempWeather}, {aveTem}")


# email
# hotKeys
emailHotKeys = "email|mail|send mail|message"
# messages
errorEmailSend = "Sorry my friend . I am not able to send this email"
insertYourMessage = "Please write your message -> "
emailCustomer = "email to whom? "
emailSent = "Email has been sent!"


# function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('fotihtashlanov@gmail.com', 'Fotix1997')
    server.sendmail('fotihtashlanov@gmail.com', to, content)
    server.close()


# infoAbtBot
# hotKeys
infoHotKeys = "your name|who are you"
# messages
messageInfo = "My name is Jarvis, I am your personal assistant"


# howAreYou
# hotKeys
hruHotKeys = "how are you"
# messages
hruMessages = ['good', 'fine', 'great']


# greeting
# hotkeys
greetingHotKeys = "hello"
# messages
greetAnsArr = ['Hi', 'Hello', "YOOU"]

# turnOff
# hotkeys
tornOffHotKeys = "bye|sleep|bye-bye|good bye"
# messages
turnOffMess = ["Bye", "bye-bye", "good bye", "see you soon"]


while isOn:
    status, command = obj.hot_word_detect()
    if status:
        while True:
            # use any one of them
            res = obj.mic_input()
            # res = obj.mic_input_ai(debug=True)

            if re.search("jokes|joke|Jokes|Joke", res):
                joke_ = obj.tell_me_joke('en', 'neutral')
                print(joke_)
                t2s(joke_)
                break

            if re.search(emailHotKeys, res):
                try:
                    t2s(insertYourMessage)
                    content = input(insertYourMessage)
                    to = input(emailCustomer)
                    sendEmail(to, content)
                    t2s(emailSent)
                except Exception as e:
                    print(e)
                    t2s(errorEmailSend)

            if re.search('setup|set up', res):
                setup = obj.setup()
                print(setup)
                break

            if re.search(weathHotKeys, res):
                city = res.split(' ')[-1]
                getWeather(city)
                break

            if re.search('news', res):
                news_res = obj.news()
                pprint.pprint(news_res)
                t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
                t2s(news_res[0])
                t2s(news_res[1])
                break

            if re.search('tell me about', res):
                topic = res[14:]
                wiki_res = obj.tell_me(topic, sentences=1)
                print(wiki_res)
                t2s(wiki_res)
                break

            if re.search('date', res):
                date = obj.tell_me_date()
                print(date)
                print(t2s(date))
                break

            if re.search('time', res):
                time = obj.tell_me_time()
                print(time)
                t2s(time)
                break

            if re.search('open', res):
                domain = res.split(' ')[-1]
                open_result = obj.website_opener(domain)
                print(open_result)
                break

            if re.search('launch', res):
                dict_app = {
                    'chrome': '../../../../Applications/Google Chrome.app',
                }

                app = res.split(' ', 1)[1]
                path = dict_app.get(app)
                if path is None:
                    t2s('Application path not found')
                    print('Application path not found')
                else:
                    t2s('Launching: ' + app)
                    obj.launch_any_app(path_of_app=path)
                break

            if re.search(greetingHotKeys, res):
                print(randomizer(greetAnsArr))
                t2s(randomizer(greetAnsArr))
                break

            if re.search(hruHotKeys, res):
                response = randomizer(hruMessages)
                print(f"I am {response}")
                t2s(f"I am {response}")
                break

            if re.search(infoHotKeys, res):
                print(messageInfo)
                t2s(messageInfo)
                break

            if re.search(tornOffHotKeys, res):
                t2s(randomizer(turnOffMess))
                isOn = False
                break

            if re.search('what can you do', res):
                li_commands = {
                    "open websites": "Example: 'open youtube.com",
                    "time": "Example: 'what time it is?'",
                    "date": "Example: 'what date it is?'",
                    "launch applications": "Example: 'launch chrome'",
                    "tell me": "Example: 'tell me about India'",
                    "weather": "Example: 'what weather/temperature in Mumbai?'",
                    "news": "Example: 'news for today' ",
                }
                ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
                I can open websites for you, launch application and more. See the list of commands-"""
                print(ans)
                pprint.pprint(li_commands)
                t2s(ans)
                break
    else:
        continue
