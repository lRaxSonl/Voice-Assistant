import listener, config, random, assistant_functions

listen = listener.listen()

def cmdFilter(response):    #фильтрует команду
    for i in config.TBR:
        cmd = response.replace(i, "")
        
    for i in config.NAME:
        cmd = cmd.replace(i, "")
    return cmd


def cmdHandler(response):
    for name in config.NAME:    #ищет имя
        if name in response.split():
            print(config.ANSWER[random.randint(0, 2)])
            cmd = cmdFilter(response)
        else:
            cmd = cmdFilter(response)
    
    for cmd_help, cmd_browser in zip(config.CMD_LIST["help"], config.CMD_LIST["open_browser"]):
        if cmd_help in cmd:
            print("help")
            
        if cmd_browser in cmd:
            assistant_functions.openBrowser()
            break

    for cmd_time in config.CMD_LIST["time"]:
        if cmd_time in cmd:
            print(assistant_functions.time())
            break


if __name__ == "__main__":
    cmdHandler(listen)