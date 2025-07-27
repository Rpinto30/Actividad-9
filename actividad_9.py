movies = [['Spiderman',2004,'Acción']]

genres = ['Acción', 'Drama', 'Comedia', 'Terror', 'Ciencia Ficción', 'Animación', 'Documental']
error_mesagge = "✖"*5+"   Lo siento, intentelo nuevamente   "+"✖"*5

def input_integer(message): #INGRESAR UN ENTERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = int(input(message))
            break
        except ValueError: print(error_mesagge)
    return value

def set_movie():
    movies_size = input_integer("▶  Ingresa la cantidad de peliculas que deseas ingresar: ")
    for mov in range(movies_size):
        movie = []
        print("-"*15+f"PELÍCULA {mov+1}"+"-"*15)
        movie_name = input("▶  Ingresa el nombre de la película: ")
        movie_year = input_integer("▶  Ingresa el año de la película: ")
        for i,j in enumerate(genres): print(f"  {i+1}) {j}")
        while True:
            movie_genre = input_integer("▶  Ingresa el genero de la película: ")
            if  0 < movie_genre <= len(genres): break
            else: print(error_mesagge)
        movies.append([movie_name, movie_year, genres[movie_genre-1]])
        print(f"\n PELÍCULA: ({movie_name} del año {movie_year}, {genres[movie_genre-1]}) agregada correctamente")

    print("-"*50+"\nTodas las peliculas fueron agregadas correctamente!")

def show_movies():
    if len(movies) > 0:
        print("-"*20+"TODAS LAS PELICULAS REGISTRADAS"+"-"*20)
        print(f"{'No':<5}{'Titulo':<30}{'Año de publicación':<20}{'Genero':<20}")
        for i,movie in enumerate(movies): print(f"{i+1:<5}{movie[0]:<30}{movie[1]:<20}{movie[2]:<20}")
    else: print("-"*50+"\n  ◇ Lo siento, no encontramos ninguna pelicula registrada")


while True:
    print("-"*20+"METFLIX"+"-"*20)
    print(" 1)Agregar pelicula\n 2)Mostrar todas las peliculas\n 3)Buscar pelicula por género\n 4)Eliminar una pelicula por titulo\n 5)Ver estradísticas del cátalogo\n 6)Salir")
    op = input('▶  Ingrese una de las opciones: ')
    match op:
        case '1': set_movie()
        case '2': show_movies()
        case '3': pass
        case '4': pass
        case '5': pass
        case '6':
            print(movies)
            print("\n ▢  ¡¡¡Hasta luego!!!")
            break
        case _: print(error_mesagge)