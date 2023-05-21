from vosk import Model, KaldiRecognizer
import pyaudio, json

class Listener:
    def __init__(self):
        self.model = Model(r'assets\model_small') #модель
        self.recognize = KaldiRecognizer(self.model, 16000)
        
        mic = pyaudio.PyAudio() #микрофон
        self.stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        

    def start_listener(self):
        self.stream.start_stream() #начинаем прослушиваем канал микрофона

        while True:
            data = self.stream.read(4096, exception_on_overflow=False)
            
            if len(data) == 0:
                break
            if self.recognize.AcceptWaveform(data):
                result = self.recognize.Result()
                result = json.loads(result)
                return result["text"]
            '''
            else:
                text = recognize.PartialResult()
                print(text[17:-3])
            '''
            
            
    def stop_listener(self):
        self.stream.stop_stream #останавливаем прослушиваем канал микрофона
        
