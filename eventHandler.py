import webbrowser as web
from datetime import datetime
import torch, time
import numpy as np
import sounddevice as sd

def openBrowser():
    w = web.get()
    w.open('https://google.com')



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



def timeNow():
    current_datetime = datetime.now()
    return f"сейчас {number_to_words(current_datetime.hour)} часов {number_to_words(current_datetime.minute)} минут"



def speak(text):
    #it was taken from https://www.youtube.com/watch?v=XTeGvaDaraI
    language = 'ru'
    model_id = 'ru_v3'
    sample_rate = 48000
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