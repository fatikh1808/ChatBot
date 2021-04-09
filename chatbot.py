import JarvisAI
import re
import pprint
import random
import smtplib
# import pyowm

# APIKEY = 'b114494f3d13c1171b52683221bc69cf'  # your API Key here as string
# OpenWMap = pyowm.OWM(APIKEY)                   # Use API key to get data

# Weather = OpenWMap.weather_at_place("London")

# Data = Weather.get_weather()

# temp = Data.get_temperature(unit='celsius')
# print("Average Temp. Currently ", temp['temp'])  # get avg. tmp
# print("Max Temp. Currently ", temp['temp_max'])  # get max tmp
# print("Min Temp. Currently ", temp['temp_min'])  # get min tmp>>


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('fotihtashlanov@gmail.com', 'Fotix1997')
    server.sendmail('fotihtashlanov@gmail.com', to, content)
    server.close()

# send weather/launch


obj = JarvisAI.JarvisAssistant()

# res = obj.setup()


def t2s(text):
    obj.text2speech(text)


while True:
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

            if re.search("email|mail|send mail|message", res):
                try:
                    t2s("Please write your message))")
                    content = input("please write your message -> ")
                    to = input("email to whom? ")
                    sendEmail(to, content)
                    t2s("Email has been sent!")
                except Exception as e:
                    print(e)
                    t2s("Sorry my friend . I am not able to send this email")

            if re.search('setup|set up', res):
                setup = obj.setup()
                print(setup)
                break

            if re.search('google photos', res):
                photos = obj.show_google_photos()
                print(photos)
                break

            if re.search('local photos', res):
                photos = obj.show_me_my_images()
                print(photos)
                break

            if re.search('weather|temperature', res):
                city = res.split(' ')[-1]
                weather_res = obj.weather(city=city)
                print(weather_res)
                t2s(weather_res)
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

            if re.search('hello', res):
                print('Hi')
                t2s('Hi')
                break

            if re.search('how are you', res):
                li = ['good', 'fine', 'great']
                response = random.choice(li)
                print(f"I am {response}")
                t2s(f"I am {response}")
                break

            if re.search('your name|who are you', res):
                print("My name is Jarvis, I am your personal assistant")
                t2s("My name is Jarvis, I am your personal assistant")
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
