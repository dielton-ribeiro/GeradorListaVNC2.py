import os

i = 101

l = input("Qual loja? ")

while True:
    tem_selfs = input("Tem selfs? (s/n) ")
    if tem_selfs.lower() not in ['s', 'n']:
        print("Por favor, digite 's' para sim ou 'n' para não.")
    else:
        break

if tem_selfs.lower() == 's':
    while True:
        primeiro_self = int(input("Qual é o número do primeiro self? "))
        ultimo_self = int(input("Qual é o número do último self? "))
        if ultimo_self < primeiro_self:
            print("O último self não pode ser menor que o primeiro self. Tente novamente.")
        else:
            break

while True:
    tem_temporario = input("Tem caixa temporário? (s/n) ")
    if tem_temporario.lower() not in ['s', 'n']:
        print("Por favor, digite 's' para sim ou 'n' para não.")
    else:
        break

if tem_temporario.lower() == 's':
    while True:
        primeiro_temporario = int(input("Qual é o número do primeiro caixa temporário? "))
        ultimo_temporario = int(input("Qual é o número do último caixa temporário? "))
        if ultimo_temporario < primeiro_temporario:
            print("O último caixa temporário não pode ser menor que o primeiro caixa temporário. Tente novamente.")
        else:
            break

script_dir = os.path.dirname(os.path.abspath(__file__))

folder_name = "Loja" + str(l)

os.mkdir(os.path.join(script_dir, folder_name))

num_pdv = int(input("Quantos pdv? "))

for j in range(i , num_pdv + i):
    if tem_selfs.lower() == 's' and primeiro_self <= j-100 <= ultimo_self:
        filename = "PDV " + str(j - 100).zfill(2) + " - SELF" + " - 172.25." + str(l) + "." + str(j) + ".vnc"
    elif tem_temporario.lower() == 's' and primeiro_temporario <= j-100 <= ultimo_temporario:
        filename = "PDV " + str(j - 100).zfill(2) + " - 172.25." + str(l) + "." + str(j) +" - TEMPORARIO "+".vnc"
    else:
        filename = "PDV " + str(j - 100).zfill(2) + " - 172.25." + str(l) + "." + str(j) + ".vnc"
    file_content = """ConnMethod=tcp
ConnTime=2021-10-17T18:00:35.134Z
Host=172.25.""" + str(l) + "." + str(j) + """
Password=bd48bfa22ac2d114
RelativePtr=0
Uuid=c4fb904e-bfb6-437d-9e99-ceb59c4535ea"""
    with open(os.path.join(script_dir, folder_name, filename), "w") as f:
        f.write(file_content)
