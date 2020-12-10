import os
import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
chunk = 1024
DURATION = 5

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(BASE_DIR, '201114165.wav')
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print('Grabando....')
frames = list()
for i in range(0, int(RATE/CHUNK * DURATION)):
    data = stream.read(CHUNK)
    frames.append(data)
print(f'Grabacion finalizada. Archivo: {filename}')
stream.stop_stream()
stream.close()
audio.terminate()
#preparando muestras para almacenar
data_bin = b''.join(frames)  # de lista a texto binario
#guardar archivo
with wave.open(filename, 'wb') as wav:
    wav.setnchannels(CHANNELS)
    wav.setsampwidth(audio.get_sample_size(FORMAT))
    wav.setframerate(RATE)
    wav.writeframes(data_bin)
#leyendo archivo  
f = wave.open(r"201114165.wav","rb")  
#iniciando pyaudio  
p = pyaudio.PyAudio()  
#abriendo stream 
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                   channels = f.getnchannels(),  
                   rate = f.getframerate(),  
                   output = True)  
#leyendo muestras  
data = f.readframes(chunk)  
#reproduciendo stream
while data:  
       stream.write(data)  
       data = f.readframes(chunk)  
#parando stream
stream.stop_stream()  
stream.close()  
#cerrando pyaudio  
p.terminate()  