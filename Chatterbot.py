from chatterbot import ChatBot
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time
from chatterbot.trainers import ChatterBotCorpusTrainer
from Antwort_aus_txt import Antwort_aus_txt as txt_antw
import webbrowser
import os

class GUI_Start(tk.Tk):

    def __init__(self, *args, **kwargs):
        """Erstellen und Setzen von Fenstervariabeln"""
        tk.Tk.__init__(self, *args, **kwargs)
        
        PATH = './db.sqlite3'
        chatbot_gelernt = os.path.isfile(PATH)
        print('1')
        """Erzeugen des ChatBots"""
        self.chatbot = ChatBot(
            "TestBot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[
            {'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Entschuldige das habe ich nicht verstanden.',
            'maximum_similarity_threshold': 0.80},
            {'import_path':'chatterbot.logic.MathematicalEvaluation',}]
        )
        print('1')
        """Trainieren des ChatBots mit Datenbanken"""
        if chatbot_gelernt==False:
            trainer = ChatterBotCorpusTrainer(self.chatbot)
            trainer.train("./begruessung.json")
            trainer.train("./smalltalk.json")
            trainer.train("./verabschiedung.json")
            trainer.train("./essentrinken.json")
        print('1')
        """Einlesen der txt-Datei"""
        self.Beispiel_txt = txt_antw("Tuttlingen.txt")
        print('1')
        self.Beispiel_txt.lade_datei()
        print('1')
        self.title("TestBot")
        print('1')
        self.initialize()
        print('1')
    def initialize(self):
        """GUI Definition"""
        self.grid()

        self.respond = ttk.Button(self, text='Senden', command=self.get_response)
        self.respond.grid(column=6, row=3, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=0, row=3, columnspan=6, sticky='nesw', padx=3, pady=3)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Unterhaltung:')
        self.conversation_lbl.grid(column=0, row=0, sticky='nesw', padx=0, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=7, sticky='nesw', padx=3, pady=3)
        
        self.conversation['state'] = 'normal'
        self.conversation.insert(tk.END, "Chatbot: Stelle mir eine Frage oder öffne den Webbrowser durch den Befehl: Öffne mir den Webbrowser\n")
        self.conversation['state'] = 'disabled'

    def get_response(self):
        
        """Antwort erhalten und auf der Oberfläche ausgeben"""
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)
        score = self.Beispiel_txt.get_Score(user_input)
        print(score)
        if user_input=="Öffne mir den Webbrowser":
            url = 'https://www.google.de/?q='
            webbrowser.get('windows-default').open(url)
            response="Webbrwoser wird geöffnet"
        elif score is None:
            response = self.chatbot.get_response(user_input)
        else:
            response = self.Beispiel_txt.get_Antwort(user_input)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "Du: " + user_input + "\n" + "ChatBot: " + str(response) + "\n"
        )
        self.conversation['state'] = 'disabled'

        time.sleep(0.1)


ChatBot_Test = GUI_Start()
ChatBot_Test.mainloop()