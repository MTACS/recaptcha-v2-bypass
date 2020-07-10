from pydub import AudioSegment

def convert():
	    sound = AudioSegment.from_mp3("/home/nya/Downloads/audio.mp3")
	    sound.export("/home/nya/Downloads/audio.wav", format="wav") 
