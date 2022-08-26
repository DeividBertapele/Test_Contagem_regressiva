# Fazendo Contagem Regressiva #
from time import sleep


print('='*35)
print('     TREINO TABATA (HIIT)     ')  # imprimindo o cabeçalho #
print('='*35)
sleep(3) # pausando antes de começar #

print('CONTAGEM REGRESSIVA  => TABATA <=') # Imprimindo a tela 
print('-'*35)
for cont in range(30, 0, -1):
    print(cont)
    sleep(1)
print('Acabou o tempo!!!')

print('PARABÉNS!! Chegou até o fim do treino..')
