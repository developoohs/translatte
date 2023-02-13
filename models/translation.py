from collections import OrderedDict
from googletrans import Translator,LANGUAGES


"""
Seçilen dil
Sık kullanılan diller

-- Program başlarken yüklenecekler.
-- program çalışırken yazılacak
-- program kapanırken son kez güncellenecek
"""


class GoogleTranslate:
    def __init__(self):
        self.translator = Translator()
        self.src=False
        self.dest:str
        self.detected_lang:str
        self.text:str
        self.output_text :str

        self.all_lang: dict
        self.most_used_dict = OrderedDict()

    def translate(self, text=None,dest_lang=None,src_lang=False):
        self.text = text or self.text
        self.src = src_lang or "self.detect_lang(self.text)"
        self.dest = dest_lang or self.dest
        

        if src_lang is not False and dest_lang is not None  and text is not None:
            self.src =  self.detect_lang(self.text)
            result = self.translator.translate(text=text, src=src_lang, dest=dest_lang).text
            #self.dest = dest_lang
            self.output_text = result
        elif src_lang is False and dest_lang is None and text is not None:
            self.src =  self.detect_lang(self.text)
            result = self.translator.translate(text=text, src=src_lang, dest=dest_lang).text
            self.output_text = result
        elif src_lang is False and dest_lang is not None and text is not None:            
            self.src =  self.detect_lang(self.text)
            result = self.translator.translate(text=text, dest=dest_lang).text
            self.output_text = result
        elif src_lang is False and dest_lang is  None and text is  None:
            self.src =  self.detect_lang(self.text)
            result = self.translator.translate(text=self.text, src=self.src,dest=self.dest).text
            self.output_text = result
        elif src_lang is not False and dest_lang is  None and text is  None:
            self.src_lang = src_lang
        else:
            print("ELSE")
        


    def reverse(self):
        self.src, self.dest = self.dest, self.src
        return self
    
    def detect_lang(self,text:str):
        return self.translator.detect(text).lang

    def select_lang(self,lang):
        self.dest =  lang
        return self

    def get_all_lang(self):
        all_lang = LANGUAGES
        #enumarate 
        all_lang_numkey = {i:{key:value} for i,(key,value) in enumerate(all_lang.items())}
        self.all_lang =  all_lang_numkey
        return all_lang_numkey

    def add_most_used_lang(self,key:int,value:dict):
        self.most_used_dict[key] = value
        self.most_used_dict.move_to_end(key,last=False)
        return self

    # TODO "The code will be edited later"
    def search_lang(self):
        listem={}
        all_lang=self.get_all_lang()
        for x in all_lang:
            listem[list(all_lang[x].keys())[0]] = list(all_lang[x].values())[0]
        choices = listem
        query = query.lower()
        results = []
        for key, value in choices.items():
            score_key = 0
            score_value = 0
            for c, q in zip(key.lower(), query):
                if c == q:
                    score_key += 1
            for c, q in zip(value.lower(), query):
                if c == q:
                    score_value += 1
            if (score_key / len(query) >= 0.6 or key.endswith(query[-(len(key) - score_key):]) or query in key) or \
            (score_value / len(query) >= 0.6 or value.endswith(query[-(len(value) - score_value):]) or query in value):
                results.append((key, value, max(score_key / len(query), score_value / len(query))))
        if not results:
            max_match = 0
            max_key = None
            max_value = None
            for key, value in choices.items():
                match = sum([1 for c, q in zip(key.lower(), query) if c == q]) + \
                        sum([1 for c, q in zip(value.lower(), query) if c == q])
                if match > max_match:
                    max_match = match
                    max_key = key
                    max_value = value
            return max_key, max_value
        sort = sorted(results, key=lambda x: x[2], reverse=True)
        #sort the outputs by similarity values
        float_tuples = [(tup[0], tup[1], float(tup[2])) if len(tup) >= 3 and isinstance(tup[2], (float, int)) else (tup[0], tup[1], 0) for tup in sort]
        return sorted(float_tuples, key=lambda x: x[-1], reverse=True)



"""   def show_all_lang_list(self):
        value_list = self.get_all_lang()
        pools = []
        for i in value_list:
            key =list(value_list[i].keys())[0]
            value =list(value_list[i].values())[0]
            index = i
            pools.append([index,key,value])
        return pools"""