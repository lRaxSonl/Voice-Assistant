import webbrowser as web
from datetime import datetime

def openBrowser():
    w = web.get()
    w.open('https://google.com')

def time():
    now = datetime.now() 
    current_time = now.strftime(f"сейчас %H часов %M минут") 
    return current_time
