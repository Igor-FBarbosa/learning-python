from math import radians, sin, cos, tan
ang = float(input('Qual ângulo escolhido? '))
angrad = radians(ang)
print(f'O ângulo {ang} tem {angrad:.2f} radianos')
print(f'Seno: {sin(angrad):.2f},\nCosseno: {cos(angrad):.2f},\nTangente: {tan(angrad):.2f}')
