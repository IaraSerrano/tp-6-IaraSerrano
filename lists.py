# Replace the "ANSWER HERE" with your answer

def remove_elements(lista):
    if len(lista) >0:
        lista = lista[1:4] + lista[6:]
     return lista

lista = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(lista))


def add_elements(lista):
    if len(lista)>0:
        lista= ['Pink'] + lista + ['Yellow']
    return lista

lista = ['Red', 'Green', 'White', 'Black']
print(add_elements(lista))


def is_empty(lista):
    if lista==[]:
        return f"La lista esta vacia"
    else:
        return f"La lista no esta vacia"

lista=[]
print(is_empty(lista))


def check_lists(lista1, lista2):
    if lista1[2]==lista2[2]:
        return True
    else:
        return False
        
lista1=['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
lista2= ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
print(check_list(lista1, lista2))



def list_of_lists(listas):
    listas[0]= listas[0][:2]
    listas[1]= listas[1][1:4]
    listas[2]=listas[2][-2:]
    return listas
    
    
listas =  [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print(list_of_lists(listas))


