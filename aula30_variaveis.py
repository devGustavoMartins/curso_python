"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

variável com letra minúscula -> pode mudar
variável com letra maiúscula -> não vai mudar
"""
velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_multa_1 = velocidade > RADAR_1
carro_range_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
multado_1 = carro_range_1 and velocidade_multa_1

if multado_1:
    print('Multado!')
elif velocidade_multa_1 and not carro_range_1:
    print('Ultrapassou a velocidade máxima, porém fora do radar')
elif not velocidade_multa_1 and carro_range_1:
    print('Passou na velocidade permitida!')