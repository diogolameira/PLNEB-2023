TPC4 - Criar html a partir do livro de doenças do aparelho digestivo e apresentar as definições das palavras que surgem tanto no livro como no dicionário médico.

Foi obtido um MemoryError:
Traceback (most recent call last):
  File , line 21, in <module>
    linha = re.sub(palavra, f"<a href title='{dicionario.get(palavra)}'>{palavra}</a>", linha)
  File "C:\Program Files (x86)\Python37-32\lib\re.py", line 192, in sub
    return _compile(pattern, flags).sub(repl, string, count)
MemoryError

Por isso, verificou-se a funcionalidade do programa utilizando apenas uma pequena parte dos ficheiros html e json (pasta teste), onde o erro já não se verificou e se observou o pretendido.