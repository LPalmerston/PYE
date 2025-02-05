#List: [], ordeded, changeable, duplicate

list1= [1, 2, 3, "dog", "cat", "New York", True, False, 3.15]
#esto es una lista, ordenada y modificable, acepta valores duplicados

n=1
for x in list1:
    print("Item", n,"=", x)
    n=n+1
#imprimir los elementos de la lista

n=1
for x in list1:
    print("Item", n,"=", type(x))
    n=n+1
#imprimir el tipo de los elementos de la lista

list1.append(5)
#agregar un valor al final de la lista
list1.remove(1)
#remomer un valor igual al valor colocado
list1[0]="Uno"
#cambiar un valor de la posicion indicada

print("Los cantidad de items son:", len(list1))
#impririr el largo de la lista

print("El tipo de variable es", type(list1))
#impririr el tipo de dato

def PrintList (list):
    n=1
    for x in list:
        print("Item Nº", n,"=", x)
        n=n+1
#crea una funcion

PrintList(list1)
#imprimir una funcion

