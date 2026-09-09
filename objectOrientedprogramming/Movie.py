"""
Movie title,language,year,director,genre 
    -setmovie(title,language,year,director,genre)
    -getmovie(self)
"""
class Movie:
    title:str
    language:str
    year:int
    director:str
    genre:str

    def __init__(self,title,language,year,director,genre):
        self.title=title
        self.language=language
        self.year=year
        self.director=director
        self.genre=genre
    def get_movie(self):
        print(self.title,self.language,self.year,self.director,self.genre)

interstellar_instance=Movie("INTERSTELLAR","English",2014,"Christopher nolan","SCI-FI")

interstellar_instance.get_movie()