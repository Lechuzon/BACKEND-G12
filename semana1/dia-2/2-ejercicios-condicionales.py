# Se ingresa
#edad = input("Ingresa tu edad:")
# hace la conversion hacia un entero
#edad = int(edad)
# print(type(edad))
# print(type(edad_numerica))
# Se ingresa la edad de la persona y si es mayor de edad puede ingresar a la discoteca, caso contrario se llama a sus padres
# Si la persona tiene entre 40 y 60 años le ofreceremos un trago de cortesia aun asi no entre a la discoteca
# Si la persona tiene mas de 65 tampoco lo dejaremos ingresar porque ya es muy adulta (uitlizar elif)


#if edad > 65:
 #   print("No puedes ingresar, ya estas muy adulto")
#elif edad >= 18:
  #  print("Puedes ingresar a la disco")
   # if edad >= 40 and edad <= 60:
    #    print("Le ofreceremos un trago de cortesia")
#else: 
 #   print("No puedes ingresar a la disco")

# -----------

numeros = [1,10,40,50,55,3,4,9]

# En base al array de numero indicar cuantos son menores que 15 y cuantos son mayores que 15

mayor_que_15 = 0
menor_que_15 = 0

for numero in numeros:
    if numero > 15 :
        mayor_que_15 += 1
    else:
        menor_que_15 += 1


print("Hay {} mayores que 15". format(mayor_que_15))
print(f"Hay {menor_que_15} menores que 15")
