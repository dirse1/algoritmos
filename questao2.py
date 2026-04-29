distancia = float(input("Digite a quantidade de km percorridos: "))
diaria = int(input("Digite a quantidade de dias que alugou o carro: "))

valorDistancia = distancia*0.85 
valorDiaria = diaria*220

print('=== RESUMO DA VIAGEM DE TRAILER ===')
print(f'Valor das diarias {valorDiaria}\nValor da km percorrida: {valorDistancia}\nValor total é de: {valorDiaria + valorDistancia}R$\nMédia de km por dia: {distancia/diaria} Km') 

