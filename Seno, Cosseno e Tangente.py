'''import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COS de {:.2}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o tangente {:.2f}'.format(angulo, tangente))'''

'''outro modelo a baixo'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COS de {:.2}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem o tangente {:.2f}'.format(angulo, tangente))