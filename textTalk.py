#import necessary library for text to speech capabilities
from gtts import gTTS

#insert text here within variable
talk = """  """

#create TTS object and tell it to say what's within the talk variable 
tts = gTTS(talk, lang='en')

#save to audio format
tts.save("pac.mp3")


