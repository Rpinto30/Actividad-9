movies = []

while True:
    print("-"*20+"Metflix"+"-"*20)
    print(" 1)Agregar pelicula\n 2)Mostrar todas las peliculas\n 3)Buscar pelicula por género\n 4)Eliminar una pelicula por titulo\n 5)Ver estradísticas del cátalogo\n 6)Salir")
    op = input('Ingrese una de las opciones: ')
    match op:
        case '1': pass
        case '2': pass
        case '3': pass
        case '4': pass
        case '5': pass
        case '6':
            print("\n ▢  ¡¡¡Hasta luego!!!")
            break
        case _: print('\n'+"✖"*5+"   Lo siento, intentelo nuevamente   "+"✖"*5+'\n')