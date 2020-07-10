import speech_recognition as sr


def recognize():
    
	    global text
	    
	    filename = '/home/nya/Downloads/audio.wav'

	    r = sr.Recognizer()

	    with sr.AudioFile(filename) as source:
		    audio_data = r.record(source)
		    recognize.text = r.recognize_google(audio_data)
