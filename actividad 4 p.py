
# 1. Declarar una lista vacía
lista_vacia = []

# 2. Declarar una lista con más de 5 elementos
lista_larga = ['amarillo', 'rojo', 'azul', 'verde', 'morado', 'gris']

# 3. Encuentre la longitud de su lista
longitud_lista = len(lista_larga)

# 4. Obtener el primer elemento, el elemento central y el último elemento de la lista
primer_elemento = lista_larga[0]
elemento_central = lista_larga[len(lista_larga) // 2]
ultimo_elemento = lista_larga[-1]

# 5. Declara una lista llamada tipos_datos_mezclados, pon tu(nombre, edad, altura, estado civil, dirección)
tipos_datos_mezclados = ['juan', 20, 1.75, 'soltero', 'olaya']

# 6. Declare una variable de lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Añadir una empresa de TI a it_companies utilizando los metodos de insercion.
it_companies.insert(0, 'instagran')
it_companies.append('tik tok')

# 8. Comprobar si una determinada empresa existe en la lista it_companies.
empresa_a_buscar = 'Google'
if empresa_a_buscar in it_companies:
    print(f'{empresa_a_buscar} existe en la lista it_companies')
else:
    print(f'{empresa_a_buscar} no existe en la lista it_companies')

# 9. Ordena la lista con el método sort()
it_companies.sort()
print(it_companies)

# 10. Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()
print(it_companies)

# 11. Elimine la primera empresa informática de la lista.
it_companies.pop(0)

# 12. Eliminar todas las empresas de TI de la lista
it_companies.clear()