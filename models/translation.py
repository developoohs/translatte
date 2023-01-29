import googletrans
from googletrans import Translator


class Translation():

    def __init__(self):
        self.lang:str

    def get_all_language(self):
        all_lang = googletrans.LANGUAGES
        #enumarate 
        all_lang_numkey = {i:{key:value} for i,(key,value) in enumerate(all_lang.items())}
        return all_lang_numkey


    def show_all_lang_list(self):
        value_list = self.get_all_language()
        pools = []
        for i in value_list:
            key =list(value_list[i].keys())[0]
            value =list(value_list[i].values())[0]
            index = i
            pools.append([index,key,value])
        return pools


    def translate(sentence,lang):
        translate_ins = Translator()
        prossed_sentence = translate_ins.translate(sentence,dest=lang).text
        return prossed_sentence

x = Translation().show_all_lang()



"""a  = MyTable(["index","key","value"])

a.add_data(x)
pr = a.print_all()

print(pr)"""