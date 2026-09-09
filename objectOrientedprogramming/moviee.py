"""
design and create a simple python crud application of movie each movie with attributes
# id,title,year,genre,rating,run_time,director

"""

class Movies:

    def __init__(self):

        self.movies = [

            {"id": 1,"title":"Sarva Maya","year":2026,"genre":"supernatural fantasy","rating":7.8,"run_time":"2h 27m","Director":"abiiii"}
        ]

    def post(self,**kwargs):

        required_field = {"id","title","year","genre","rating","run_time","Director"}

        missing_fields = required_field.difference(kwargs.keys())

        if missing_fields:

            raise ValueError(missing_fields, " is missing ")

        self.movies.append(kwargs)

        print("movie records has been added.....")

    def get(self):

        if len(self.movies)==0:

            print("No Records Found.....")

        else:

            for movie in self.movies:

                print(movie)

    def retrieve(self,id = None):

        movie = [m for m in self.movies if m.get("id")==id][0]

        print(movie)

    def put(self,id=None,**kwargs):

        movie = [m for m in self.movies if m.get("id")==id][0]

        movie.update(kwargs)

        print("Movie Record has been updated....")

        print(movie)

    def delete(self,id=None):

        movie = [m for m in self.movies if m.get("id")==id][0]

        self.movies.remove(movie)

        print("movie record has been deleted.... ")

        self.get()

movie_instance = Movies()
movie_instance.post(id =2,title ="Drishyam" ,year = 2013,genre ="Crime Thriller",rating =8.5,run_time = "2h 40m",Director = "Jeethu Joseph")
movie_instance.post(id =3,title ="Premam",year = 2015,genre ="Romance/Comedy",rating =8.3,run_time = "2h 36m",Director = "Alphonse Puthren")
#movie_instance.get()
movie_instance.retrieve(id=3)
movie_instance.put(id=1,Director ="Akhil sathyan")
movie_instance.delete(id=2)

       






        