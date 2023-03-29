from deep_translator import GoogleTranslator
import json

translator = GoogleTranslator(source='auto', target='en')  # output -> Weiter so, du bist großartig

file_in = open("testejson.json")

dici = json.load(file_in)

new_dici = {}
for designation, description in dici.items():
    en_translation = translator.translate(designation)
    print(en_translation)
    new_dici[designation] = {
                            "des": description,
                            "en" : en_translation}
    
file_out = open ("dicionario_translation.json", "w")
json.dump(new_dici, file_out, ensure_ascii=False, indent=4)
file_out.close()