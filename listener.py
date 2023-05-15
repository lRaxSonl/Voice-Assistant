from vosk import Model, KaldiRecognizer
import pyaudio, json

model = Model(r'assets\model_small') #модель
recognize = KaldiRecognizer(model, 16000)

def listen():
 
    mic = pyaudio.PyAudio() #микрофон
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream() #начинаем прослушиваем канал микрофона

    while True:
        data = stream.read(4096, exception_on_overflow=False)
        
        if len(data) == 0:
            break
        if recognize.AcceptWaveform(data):
            result = recognize.Result()
            result = json.loads(result)
            return result["text"]
            
        '''
        else:
            text = recognize.PartialResult()
            print(text[17:-3])
        '''
