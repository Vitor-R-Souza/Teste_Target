import json

with open('dados_dias/dados.json', 'r') as file:
    dados = json.load(file)

DiasAcimaMedia = 0
valores = []
for Item in dados:
    if Item['valor'] == 0.0:
        pass
    else:
        valores.append(Item['valor'])

media = sum(valores) / len(valores)
MaiorValor =  max(valores)
MenorValor = min(valores)

for Item in dados:
    if Item['valor'] > media:
        DiasAcimaMedia = DiasAcimaMedia + 1

print(f'O maior valor: {MaiorValor:.2f}')
print(f'O menor valor: {MenorValor:.2f}')
print(f'A media: {media:.2f}')
print('Dias na qual o valor foi acima da media: ', DiasAcimaMedia)