from collections import defaultdict
from translate import Translator

class TextAnalysis():   
    memory = defaultdict(list)
    

    qwestions = {
        'как тебя зовут': "Я супер-крутой-бот и мое предназначение помогать тебе!",
        'сколько тебе лет': "Это слишком философский вопрос"
    }

    def __init__(self, text, owner):
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        if self.text.lower() in TextAnalysis.qwestions.keys():
            self.response = TextAnalysis.qwestions[self.text.lower()]
        else:
            self.response = self.get_answer()

    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"