import re

file = open('dicionario_medico.txt', encoding='utf8')
text = file.read()
text = re.sub(r'\f', '\n', text)
text = re.sub(r'(\n\n.+)\n\n', 'r\1', text)
entries = re.findall(r'\n\n(.+)((?:\n.+)+)', text)
#print(entries[:3])
new_entries = [(designation, description.strip()) for designation, description in entries]
#print(new_entries[:3])
'''
new_entries = []
for designation, description in entries:
    description = description.strip()
    new_entries.append((designation, description))
print(print(new_entries[:3]))
'''
file.close()

html = open('dicionario_medico.html', 'w', encoding='utf8')

header = '''<html>
<head>
<meta charset='utf-8'/>
<style>
table {
  font-family: helvetica;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<title>Dicionário Médico</title>
<body>
<h1 style="text-align:center; font-family:helvetica;">Dicionário Médico</h1>
<br>
<table>
<tr>
<th>Termo</th>
<th>Designação</th>
</tr>
'''
body = ''
for designation, description in new_entries:
    body += '<tr>'
    body += '<td>' + designation + '</td>'
    body += '<td>' + description + '</td>'
    body += '</tr>'

footer = '''
</table>
</body>
</html>
'''
html.write(header + body + footer)
html.close()