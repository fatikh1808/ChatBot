import speech_recognition as sr

# def speachToText():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Say something!")
#         audio = r.listen(source)

#     try:
#         # for testing purposes, we're just using the default API key
#         # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#         # instead of `r.recognize_google(audio)`
#         recognizedAudio = r.recognize_google(audio, language="ru_RU")
#         print("Google Speech Recognition thinks you said " + recognizedAudio)
#         return recognizedAudio
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print(
#             "Could not request results from Google Speech Recognition service; {0}".format(e))
