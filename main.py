from listener import Listener
import config, eventHandler
from playsound import playsound as pl
from eventHandler import speak

listen = Listener()
print("\n\n\nговорите...")

def cmdFilter(response):    #фильтрует команду
    for i in config.TBR:
        cmd = response.replace(i, "")   #убирате все слова на удаление(находятся в файле конфиг в переменной "TBR" - To Be Remove)
        
    for i in config.NAME:
        cmd = cmd.replace(i, "")    #убирает все имена с ответа
    return cmd


def cmdHandler(response):
    response_sp = response.split()
    print(response_sp)
    print(response)
    for name in config.NAME:    #ищет имя
        if name in response_sp:
            nameI = response_sp.index(name) #находит индекс имени ассистента в ответе

            if len(response_sp)-1 == nameI: #если после того, как прозвучало слово помошник больше нет слов, то он спрашивает что вам нжно и вы можете повторить команду
                listen.stop_listener()  #остановка прослушивание
                pl(r'assets\audio\jarvis\yes-sir.wav')
                cmdHandler(listen.start_listener()) #повторный вызов функции
                break
            else:
                cmd = cmdFilter(response).strip()   #фильтрация команды
                continue
        
        else:
            cmd = cmdFilter(response).strip()
            continue

    for cmd_help, cmd_browser in zip(config.CMD_LIST["help"], config.CMD_LIST["open_browser"]):
        if cmd_help in cmd:
            speak("я умею: открывать браузер, показывать время")
            break
                
        if cmd_browser in cmd:
            pl(r'assets\audio\jarvis\right.wav')
            eventHandler.openBrowser()
            break

    for cmd_time in config.CMD_LIST["time"]:
        if cmd_time in cmd:
            speak(eventHandler.timeNow())
            break
        
        

if __name__ == "__main__":
    cmdHandler(listen.start_listener())