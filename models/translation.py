import googletrans
from googletrans import Translator


"""
Seçilen dil
Sık kullanılan diller

-- Program başlarken yüklenecekler.
-- program çalışırken yazılacak
-- program kapanırken son kez güncellenecek
"""

class Translation():

    def __init__(self):
        self.lang:str
        self.detected_lang: str
        self.text:str
        self.output_text:str
        self.reverse_text:str
        

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


    def translate(self,text_value=None,detect_lang=None):
        translate_ins = Translator()
        self.text = text_value
        if detect_lang == None:
            #EĞER DETECT LANG BOŞ İSE DOSYADAN YÜKLEYİP SON KULLANILAN DİLİ KULLAN
            output_text = translate_ins.translate(text_value,dest=self.lang).text
            self.output_text = output_text
            return output_text
        else:
            reverse_text = translate_ins.translate(self.output_text,detect_lang).text
            self.reverse_text = reverse_text
            return reverse_text
        
    
    def select_lang(self,lang):
        self.lang =  lang
        return True

    def detect_lang(self):
        translate_ins = Translator()
        detected_lang = translate_ins.detect(self.text).lang
        self.detected_lang = detected_lang
        return detected_lang

    def change_translate(self):
        detect_lang = self.detect_lang()
        reverse_text = self.translate(detect_lang=detect_lang)
        self.reverse_text = reverse_text
        return reverse_text

"""a  = MyTable(["index","key","value"])

a.add_data(x)
pr = a.print_all()

print(pr)"""

"""
var= Translation("bazen bazı şeyler gibi şey olmamak lazım","en")

all = var.show_all_lang_list()

tr = var.translate()
print(tr)
ch = var.change_translate()
print(ch)"""