from gtts import gTTS
import os

mensaje= "Certificacion PCEP"
lenguage="es"
myobj=gTTS(text=mensaje,lang=lenguage,slow=False)
myobj.save("certificacion.mp3")
os.system("start certificacion.mp3")