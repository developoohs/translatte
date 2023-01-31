import json
import os
from file_operation.file_io import JSONHandler

"""
Seçilen dil
Sık kullanılan diller

-- Program başlarken yüklenecekler.
-- program çalışırken yazılacak
-- program kapanırken son kez güncellenecek
"""

class FileService:
    FILE_NAME = "translatte_config.json"
    def __init__(self):
        self.most_used_lang:dict
        self.selected_lang:str


    def load(self):
        print(self.FILE_NAME)

    def update(self):
        self.FILE_NAME

    




