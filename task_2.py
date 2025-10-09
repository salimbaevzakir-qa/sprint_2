class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"


# Вызов метода add_movie() для объекта Comedy
comedy = Comedy()
result_comedy = comedy.add_movie('Большой куш')
print(result_comedy)

# Вызов метода add_movie() для объекта Drama
drama = Drama()
result_drama = drama.add_movie('Оружейный барон')
print(result_drama)

