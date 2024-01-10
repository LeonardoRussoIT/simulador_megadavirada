import random
from time import sleep

def jogos():
    return sorted(random.sample(range(0, 100+1), 6))

def resultado():
    return sorted(random.sample(range(0, 100+1), 6))

def contar_acertos(jogada, numeros_sorteados):
    return len(set(jogada).intersection(numeros_sorteados))

qntd_jogadas = int(input('Quantos bilhetes você deseja comprar? '))

seus_bilhetes = []
for _ in range(0, qntd_jogadas):
    seus_bilhetes.append(jogos())

numeros_sorteados = resultado()

ganhou = False
melhor_jogada = None
max_acertos = 0
for bilhete in seus_bilhetes:
    if bilhete == numeros_sorteados:
        ganhou = True
    else:
        acertos_atual = contar_acertos(bilhete, numeros_sorteados)
        if acertos_atual > max_acertos:
            max_acertos = acertos_atual
            melhor_jogada = bilhete
    
sleep(1)
print(f'Você gastou R${float(5 * qntd_jogadas):.2f} em apostas...')
sleep(1)
print('e você...')
sleep(3)
if ganhou:
    print('Ganhou, você acaba de receber R$588.800.000,00!')
    sleep(1)
    print(f'Os números sorteados foram: {numeros_sorteados}')
else:
    print('Não ganhou :(')
    sleep(1)
    print(f'Os números sorteados foram: {numeros_sorteados}')
    print(f'Sua melhor jogada foi {melhor_jogada}, com {max_acertos} acerto(s)')
