SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total = SP + RJ + MG + ES + Outros

def porcentagem(parte, total):
    resul = (parte / total) * 100
    resultado = f'{resul:.2f}'
    return resultado

print(f'SP - {porcentagem(SP, total)}%')
print(f'RJ - {porcentagem(RJ, total)}%')
print(f'MG - {porcentagem(MG, total)}%')
print(f'ES - {porcentagem(ES, total)}%')
print(f'outros - {porcentagem(Outros, total)}%')