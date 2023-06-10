import webbrowser as wb
from datetime import datetime
import torch, time, random, openai
import numpy as np
import sounddevice as sd
from translate import Translator
from config import MUSIC, GPT_API

#открывает браузер
def openBrowser():
    w = wb.get()
    w.open('https://google.com')


#переводит числа в слова (нужно для синтеза речи)
def number_to_words(number):
    word_map = {
        0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
        11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
        15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать',
        19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
        50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят',
        90: 'девяносто', 100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
         500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот'
    }

    if 10 <= number <= 19:
        return word_map[number]

    words = ''
    if number >= 100:
        words += word_map[number // 100 * 100] + ' '
        number %= 100
    if number >= 20:
        words += word_map[number // 10 * 10] + ' '
        number %= 10
    if number > 0:
        words += word_map[number]

    return words


#показывает текущее время
def timeNow():
    current_datetime = datetime.now()
    return f"сейчас {number_to_words(current_datetime.hour)} часов {number_to_words(current_datetime.minute)} минут"


#синтез речи
def speak(text):
    #it was taken from https://www.youtube.com/watch?v=XTeGvaDaraI
    language = 'ru'
    model_id = 'ru_v3'
    sample_rate = 48000 #частота дискритизации
    speaker = 'aidar' # aidar, baya, kseniya, xenia, random
    put_accent = True
    put_yo = True
    device = torch.device('cpu') # cpu или gpu

    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                            model='silero_tts',
                            language=language,
                            speaker=model_id)
    model.to(device)


    # воспроизводим
    audio = model.apply_tts(text=text,
                                speaker=speaker,
                                sample_rate=sample_rate,
                                put_accent=put_accent,
                                put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()
    
    
#проигрывания музыки из списка
def music():
    w = wb.get()
    w.open(random.choice(MUSIC))

#запрос к ChatGPT
def gptReq(request):
    #request = Translator(from_lang='ru', to_lang='en').translate(request)
    openai.api_key = GPT_API
    response = openai.Completion.create(
                                        model="text-davinci-003",
                                        prompt=request,
                                        temperature=0.5,
                                        max_tokens=1000,
                                        top_p=1.0,
                                        frequency_penalty=0.5,
                                        presence_penalty=0.0,
                                        stop=''
                                        )
    
    #return Translator(from_lang='en', to_lang='ru').translate(response["choices"][0]["text"])
    return response["choices"][0]["text"]

#поиск в интернете
def search(request):
    wb.open(f'https://www.google.com/search?q={request}&source=hp&ei=92yEZNXQFYySxc8PwvmZyAs&iflsig')