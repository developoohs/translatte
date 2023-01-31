from commands.cmd_table import CLITable
from models.translation import Translation
from utils.most_used_language  import MostUsed
from file_operation.file_io import JSONHandler
import argparse


"""
- Dil seç
- Çevirilen yazıyı tersine çevir
- Çevir


"""


class CommandLineApp:
    def __init__(self):
        self.translation = Translation()

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description='A simple command line application')
        parser.add_argument("-t", dest="text", help="Input text for translation")
        parser.add_argument("--lang", dest="language", help="Target language for translation")
        parser.add_argument("--ch", dest="change" ,help='reverse the translation.')
        self.args = parser.parse_args()

    def run(self):
        text = self.args.text
        language = self.args.language
        change = self.args.change
        counter = 0
        if language and text:
            counter = counter +1
            lang = self.translation.select_lang(language)
            translate = self.translation.translate(text)
            JSONHandler("input_text.json").write({"input_text":text})
            print(translate)
            
        elif text:
            translate = self.translation.translate(text)

            print("### ONLY Text :",translate)
        elif language:
            lang = self.translation.select_lang(language)
            print("## LANG : ",lang)
        else:
            pass

        if language and text and change:
            counter = counter +1
            var = JSONHandler("input_text.json").read()
            reverse_text = self.translation.change_translate()
            #ordered dict ile veri dönüşecek ve işlemler yapılacak sonra dosyaya kaydolacak
            #arka planda çalışır halde olup komut satırından anında etkileşime geçme de ayarlanmalı
            var["input_lang"] = "en"
            print(var)
            print(reverse_text,"-*")
        
        else:
            print("ELSE")

        


    def main(self):
        self.parse_arguments()
        self.run()

    def print_usage(self):
        print('Usage: python app.py -t <translate> --lang <language> --ch <change>')

    def print_error(self, message):
        print(f'Error: {message},******')
        
    def print_output(self, output):
        print(f'Output: {output}')

    def handle_exception(self):
        try:
            self.main()
        except Exception as e:
            self.print_error(str(e))
            self.print_usage()


