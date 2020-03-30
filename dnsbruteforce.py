import sys
import dns.resolver

argumentos = sys.argv #le os argumentos
try:
    dominio = argumentos [1]
    lista = argumentos [2]
    print(dominio,lista)
except:
    print("Arquivo nÃ£o encontrado ou invalido")
    sys.exit(1)

#abre a list
try:
    dominio = open(lista)
    linhas = dominio.read().splitlines()
except:
    print("Arquivo não encontrado ou invalido")
    sys.exit(1)

#para cada linha da list testa o dns
for linha in linhas:
    subdominio = linha + '.bancocn.com'
    try:
        respostas = dns.resolver.query(subdominio,'a')
        for resultado in respostas:
            print(subdominio,resultado)
    except:
        pass
