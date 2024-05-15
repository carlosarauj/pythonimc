nome = 'Carlos'
altura = 1.76
peso = 79
imc = (peso/(altura**2))

if imc < 18.5:
    print(f"baixo peso, {imc}")
elif imc > 18.5 and imc <24.9:
    print(f"peso adequado, {imc}")
elif imc > 25 and imc < 29.9:
    print(f"sobrepeso, {imc}")
elif imc > 30:
    print(f"Obesidade, {imc}")