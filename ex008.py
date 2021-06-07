print('Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros')
medida = float(input('Digite o valor em metros: '))
cm = medida*100
mm = medida*1000
print('O valor de {}m corresponde a {}cm e a {}mm'.format(medida, cm, mm))
