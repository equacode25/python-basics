print("🚀 MISIÓN EQUA - Día 3 🚀")

nombre = input("¿Nombre de la astronauta? ")
puntos = 0

print("\nHola", nombre, "🐱")
print("Equa detecta dos caminos en el espacio.")

camino = input("¿Ir por ASTEROIDES o NEBULOSA? ").lower()

if camino == "asteroides":
    print("\nEs peligroso, pero encuentras minerales raros 💎")
    puntos = puntos + 10
elif camino == "nebulosa":
    print("\nLa vista es hermosa, pero no encuentras nada útil 🌫️")
    puntos = puntos + 5
else:
    print("\nTe quedas flotando sin decidir 😅")

print("\nAhora aparece un acertijo científico.")

respuesta = input("¿El agua es H2O? (si/no) ").lower()

if respuesta == "si":
    print("Correcto 🧪✨")
    puntos = puntos + 10
else:
    print("Ups... Equa te mira con decepción científica 🐱")

print("\nMISIÓN TERMINADA")
print("Puntos finales:", puntos)

if puntos >= 20:
    print("Eres una astronauta científica experta 🚀🌟")
elif puntos >= 10:
    print("Vas muy bien, sigue aprendiendo 💙")
else:
    print("Necesitas más práctica, pero vas en camino 🐱")
