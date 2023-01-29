
from collections import OrderedDict


class MostUsed():
    """
    Program kapanmadan önce bir json dosyasına yazılmalı
    """
    def __init__(self):
        self.most_used_dict = OrderedDict()

#Yeni ögeyi ordereddict'tin en başına ekliyor
    def most_commonly_used(self,key,value):
        self.most_used_dict[key] = value
        self.most_used_dict.move_to_end(key,last=False)

#commondline'da göstermek
    def show(self):
        for i in self.most_used_dict:
            key =list(self.most_used_dict[i].keys())[0]
            value =list(self.most_used_dict[i].values())[0]
            v = f"{i} {key} {value}"
            print(v)
        return "başarılı"



de = MostUsed()

de.most_commonly_used(2,{"en":"english"})

de.most_commonly_used(1,{"tr":"turkish"})
de.most_commonly_used(3,{"kr":"Korean"})
de.most_commonly_used(1,{"tr":"turkish"})
