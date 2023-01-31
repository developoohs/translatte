import json
import os


class JSONHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r') as f:
                    return json.load(f)
            except json.decoder.JSONDecodeError:
                print(f"{self.file_name} is not a valid json file.")
                return None
        else:
            print(f"{self.file_name} not found.")
            return None
       

    def write(self, data):
        with open(self.file_name, 'w') as f:
            json.dump(data, f)
            f.close()

"""file_name = "most_used_language.json"

JSONHandler(file_name).read()

data = {'name': 'asdasdasd', 'age': 30}

JSONHandler(file_name).write(data)

print(JSONHandler(file_name).read())"""