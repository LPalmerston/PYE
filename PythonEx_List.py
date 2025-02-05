#PythonEx

print("Hola mundo")

#LIST 

fruits_list= [1, 2, 3, "dog", "cat", "New York", True, False, 3.15]
#esto es una lista, ordenada y mutable, acepta valores duplicados
n=1
for x in fruits_list:
    print("Fruit", n,"=", x)
    n=n+1
#imprimir todos los elementos de la list

fruits_list.append(5)
#agregar un valor al final de la lista
fruits_list.remove(1)
#remomer un valor igual al valor colocado
fruits_list[0]="Uno"
#cambiar un valor de la posicion indicada

print("Los cantidad de valores son:", len(fruits_list))
#impririr el largo de la lista

print("El tipo de variable es", type(fruits_list))
#impririr el tipo de dato

def PrintList (list):
    n=1
    for x in list:
        print("Fruit Nº", n,"=", x)
        n=n+1
#crea una funcion

PrintList(fruits_list)
#imprimir una funcion

