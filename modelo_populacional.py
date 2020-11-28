from pylab import *

# Valor de k
k = 3.8
# Valor inicial da população
x = [0.5]
# Número de gerações
N = 50

for n in range(0, N):
    # Para cada iteracao calcula x_n+1 e adiciona a lista x
    x.append(k * x[n] * (1. - x[n]))

# Plotando
xlabel('Número de gerações')
ylabel('x(n)')
title('Mapa logístico (k=' + str(k) + ', x0=0.5)')
plot(x, 'b', linewidth=2)
ylim((0, 1))

# Mostra na tela
show()