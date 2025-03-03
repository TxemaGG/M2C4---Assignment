#Exercise 1: 

#list

usuarios = ['Silvia', 'Eric', 'Ibon']

#tuple

escalada = ('roca', 'hielo', 'nieve')

#float

float_number = 10.99

#integer

integer_number = 12

#decimal

from decimal import Decimal
product_cost = Decimal(4.40)
commission_rate = Decimal(0.06)
qty = 200
product_cost += (commission_rate * product_cost)
print(product_cost * qty)

decimal_number = 932.8000000000000733635374672

#dictionary

rios = {
    "Africa" : "Nilo",
    "America" : "Amazonas",
    "Europa" : "Danubio",
}


#Exercise 2: Round your float up.

import math
float_number = 10.99
print(math.ceil(float_number))


#Exercise 3: Get the square root of your float.

float_number = 10.99
print(math.sqrt(float_number))


#Exercise 4: Select the first element from your dictionary.

rios = {
    "Africa" : "Nilo",
    "America" : "Amazonas",
    "Europa" : "Danubio",
}

print(list(rios.items())[0])


#Exercise 5: Select the second element from your tuple.

escalada = ('roca', 'hielo', 'nieve')
segundo_elemento = escalada[1]
print(segundo_elemento)


#Exercise 6: Add an element to the end of your list.

usuarios = ['Silvia', 'Eric', 'Ibon']
usuarios.append('Txema')
print(usuarios)


#Exercise 7: Replace the first element in your list.

usuarios = ['Silvia', 'Eric', 'Ibon']
usuarios[0]='Nuria'
print(usuarios)


#Exercise 8: Sort your list alphabetically.

usuarios = ['Silvia', 'Eric', 'Ibon']
usuarios.sort()
print(usuarios)


#Exercise 9: Use reassignment to add an element to your tuple.

escalada = ('roca', 'hielo', 'nieve')
escalada += ('indoor',)
print(escalada)
