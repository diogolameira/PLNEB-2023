#EX 2

s = input("String: ")

def string_manipulation():
    # Inverter a string
    reversed = s[::-1]
    print("String invertida:", reversed)

    # Contar o número de "a" e "A"
    num = s.count('a') + s.count('A')
    print("Número de \'a' e \'A':", num)

    # Contar o número de vogais
    vogais = 'aeiouAEIOU'
    num_vogais = 0
    for char in s:
        if char in vogais:
            num_vogais += 1
    print("Número de vogais:", num_vogais)

    # Converter para minúsculas
    lowercase = s.lower()
    print("String em minúsculas:", lowercase)

    # Converter para maiúsculas
    uppercase = s.upper()
    print("String em maiúsculas:", uppercase)

string_manipulation()