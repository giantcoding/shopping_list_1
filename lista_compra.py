print(' ---------------------- ')
print(' | LISTA DE LA COMPRA | ')
print(' ---------------------- ')
print()

list = []

while True:
    print()
    print('1. Añadir producto')
    print('2. Ver lista de productos')
    print('3. Eliminar producto')
    print('4. Limpiar lista')
    print('5. Salir del programa')
    choice = input('Escriba el número correspondiente a la acción: ')

    if choice == "1":
        product = input('Escriba el producto: ')
        if product in list:
            print('')
            print('¡Ya tiene guardado este producto!')
        else:
            list.append(product)
            print()
            print('El producto ' + product + ' se ha guardado correctamente')
    
    if choice == "2":
        print()
        print(' | LISTA DE PRODUCTOS | ')
        print()
        print(list)
        for i in list:
            print("-", i)
    
    elif choice == "3":
        product = input('Escriba el producto que desea eliminar: ')
        if product not in list:
            print()
            print('El producto escrito no se encuentra en la lista')
    
        else:
            list.remove(product)
            print()
            print('El producto ' + product + ' ha sido eliminado correctamente')

    elif choice == "4":
        list.clear()
        print()
        print('Su lista se ha reseteado correctamente')

    elif choice == "5":
        break


    