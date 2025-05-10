""" 
4. Se tiene un archivo con el siguiente texto:

Paco Peco, chico rico,
insultaba como un loco
a su tío Federico;
y éste dijo: Poco a poco,
Paco Peco, poco pico. Me han dicho que has dicho un dicho
que han dicho que he dicho yo,
el que lo ha dicho, mintió,
y en caso que hubiese dicho
ese dicho que tú has dicho
que han dicho que he dicho yo,
dicho y redicho quedó.
y estaría muy bien dicho,
siempre que yo hubiera dicho
ese dicho que tú has dicho
que han dicho que he dicho yo.

Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función recibe “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.
"""

def reemplazar(texto):
    p_a_reemplazar = input('Por qué palabra quiere reemplazar? ')
    reemplazo = input('Por cuál? ')
    for oracion in range(len(texto)):
        if p_a_reemplazar in texto[oracion]:
            texto[oracion] = texto[oracion].replace(p_a_reemplazar, reemplazo)
    #no retorna nada porque modifica en el lugar

#abro
with open('texto_guia6_ej4.txt') as archivo:
    texto = archivo.readlines()
#formateo
for oracion in range(len(texto)):
    texto[oracion] = texto[oracion].strip('\n')
#muestro
print(texto)
print('_____________________________________________________________________________--')
reemplazar(texto)
print(texto)
#reemplazo
with open('texto_guia6_ej4.txt', 'w') as archivo:
    archivo.write('\n'.join(texto))




#chequeo
with open('texto_guia6_ej4.txt') as archivo:
    texto = archivo.readlines()
#formateo
for oracion in range(len(texto)):
    texto[oracion] = texto[oracion].strip('\n')
#muestro
print(texto)