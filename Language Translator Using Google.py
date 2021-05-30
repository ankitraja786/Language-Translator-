import googletrans


print(googletrans.LANGUAGES)


import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

recog1 = spr.Recognizer()
mc = spr.Microphone()

with mc as source:
	print("Speak 'hello' to initiate the Translation !")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	recog1.adjust_for_ambient_noise(source, duration=0.2)
	audio = recog1.listen(source)
	MyText = recog1.recognize_google(audio)
	MyText = MyText.lower()

if 'hello' in MyText:
	
	# Translator method for translation
	translator = Translator()
	
	# short form of english in which
	# you will speak
	from_lang = 'en'
	
	# In which we want to convert, short
	# form of hindi
	to_lang = 'hi'
	
	with mc as source:
		
		print("Speak a stentence...")
		recog1.adjust_for_ambient_noise(source, duration=0.2)
		
		
		audio = recog1.listen(source)
		
		
		get_sentence = recog1.recognize_google(audio)

	
		try:
			
			print("Phase to be Translated :"+ get_sentence)
			text_to_translate = translator.translate(get_sentence,src= from_lang,dest= to_lang)
			text = text_to_translate.text

	
			speak = gTTS(text=text, lang=to_lang, slow= False)
			speak.save("captured_voice.mp3")	
			
			os.system("start captured_voice.mp3")
		except spr.UnknownValueError:
			print("Unable to Understand the Input")
			
		except spr.RequestError as e:
			print("Unable to provide Required Output".format(e))
