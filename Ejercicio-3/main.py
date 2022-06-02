from Menu import Menu


if __name__ == '__main__':
    menu = Menu()
    opcion = None
    while opcion != 0:
        menu.mostrar()
        opcion = int(input('Tu opcion: '))
        menu.menuOp(opcion)
    else: 
        print('Saliendo del Programa')
