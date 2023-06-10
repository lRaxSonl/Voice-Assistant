from listener import Listener
import config, eventHandler
from playsound import playsound as pl
from eventHandler import speak, gptReq

#фильрация команд
def cmdFilter(response):
    for i in config.TBR:
        cmd = response.replace(i, "")   #убирате все слова на удаление(находятся в файле конфиг в переменной "TBR" - To Be Remove)
        
    for i in config.NAME:
        cmd = cmd.replace(i, "")    #убирает все имена с ответа
    return cmd

#обработка команд
def cmdHandler(response):
    check_cmd = False #проверка на выполнения команды
    response_sp = response.split() #делем ответ от пользователя
    print(response_sp)
    print(response)
    for name in config.NAME:    #ищет имя
        if name in response_sp: #пробегаемся по разделённому ответу
            nameI = response_sp.index(name) #находит индекс имени ассистента в ответе

            if len(response_sp)-1 == nameI:
                pl(r'assets\audio\jarvis\yes-sir.wav')
                continue
            else:
                cmd = cmdFilter(response).strip()
                continue
        
        else:
            cmd = cmdFilter(response).strip()
            continue
        
    #команда помощь или открытие браузера
    for cmd_help, cmd_browser in zip(config.CMD_LIST["help"], config.CMD_LIST["open_browser"]):
        if cmd_help in cmd:
            check_cmd = True
            speak("я умею: открывать браузер, показывать время")
            break
                
        if cmd_browser in cmd:
            check_cmd = True
            pl(r'assets\audio\jarvis\right.wav')
            eventHandler.openBrowser()
            break
        
    #команда показать текущее время
    for cmd_time in config.CMD_LIST["time"]:
        if cmd_time in cmd:
            check_cmd = True
            speak(eventHandler.timeNow())
            break
        
    #команда на проигрывание музыки
    for cmd_music in config.CMD_LIST["music"]:
        if cmd_music in cmd:
            check_cmd = True
            pl(r'assets\audio\jarvis\right.wav')
            eventHandler.music()
 
    #команда поиск по запросу
    for cmd_search in config.CMD_LIST["search"]:
        if cmd_search in cmd:
            check_cmd = True
            pl(r'assets\audio\jarvis\right.wav')
            for i in config.CMD_LIST["search"]:
                req = response.replace(i, "")
                
            for i in config.NAME:
                req = req.replace(i, "")
                
            eventHandler.search(req)
    
    #команда на запрос к ChatGPT
    if check_cmd == False:
        req = gptReq(response) #отдаём изначальный запрос пользоватеся в чат гпт для обработки
        print(req)
        speak(req)
        
#старт ассистента
def startListening():
    listen = Listener()
    pl('assets/audio/jarvis/at-your-service-sir.wav')
    print("\n\n\nГоворите...")
    cmdHandler(listen.start_listener())
'''
if __name__ == "__main__":
    cmdHandler(listen.start_listener())
'''