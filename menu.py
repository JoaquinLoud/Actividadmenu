# Generar un menu, con N opciones, cominando diccionarios con tuplas, que permita colocar el valor de la opción,
#  la descripcion de opción y el nombre de al función que ejecutaria dicha opción.

# """------------------------Menu----------------------------"""
def menu():
    salir = False
    while (salir == False):
        try:
            n = int(input("Digite el numero de opciones que tendra el menu? : \n"))
            salir = True
        except:
            print('Error dato invalido')
    diccionario = {}




if __name__ == '__main__':
    pintarMenu()