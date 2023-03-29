import json, re

file_in = open("dicionario_medico_reduzido.json", encoding="utf-8")

dici = json.load(file_in)

file = open('termos_traduzidos.txt', encoding='utf8')
lines = file.readlines()
dicionario={}
for line in lines:
    entries = re.findall(r'^[^@ ]+', line)
    translation = re.findall(r'@\s(.+)$', line)
    entry = ''.join(entries)
    trans = ''.join(translation)
    dicionario[entry] = trans

print(dicionario)

new_dici = {}
for designation, description in dici.items():
    new_dici[designation] = {
                            "des": description,
                            "en" : dicionario.get(designation, "Não encontrado")}
    
file_out = open ("dicionario_translation_2.json", "w", encoding="utf-8")
json.dump(new_dici, file_out, ensure_ascii=False, indent=4)
file_out.close()