from customtkinter import *
from playsound import playsound as pl
import commandHandler
import threading

class VoiceAssistant(CTk):
    def __init__(self):
        super().__init__()

        self.title('Voice Assistant')
        self.geometry('500x550+550+40')
        self.resizable(False, False)
        
#параметры виджетов
    def widgets(self):
        self.button = CTkButton(self, text="Start Assistant", width=60, height=60, command=self.start_assistant)
        self.optionmenu_1 = CTkOptionMenu(self, values=["Dark", "Light"], command=lambda x: set_appearance_mode(self.optionmenu_1.get().lower()))
        self.optionmenu_1.set("Theme mode")
        
#прорисовка виджетов
    def setWidgets(self):
        self.optionmenu_1.grid(row=0, column=1, pady=10, padx=1)
        self.button.place(x=215, y=210)
        
#старт ассистента в отдельном потоке
    def start_assistant(self):
        threading.Thread(target=commandHandler.startListening).start()

if __name__ == "__main__":
    app = VoiceAssistant()
    app.widgets()
    app.setWidgets()
    app.mainloop()
