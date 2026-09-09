"""
Song  id,moviename,title,trackno,singer,duration
        -setsong(id,moviename,title,trackno,singer,duration)
        -getsong()
"""
class Song:
    id:int
    moviename:str
    title:str
    trackno:int
    singer:str
    duration:str
    def __init__(self,id,moviename,title,trackno,singer,duration):
        self.id=id
        self.moviename=moviename
        self.title=title
        self.trackno=trackno
        self.singer=singer
        self.duration=duration
    def get_song(self):
        print(self.id,self.moviename,self.title,self.trackno,self.singer,self.duration)
        
malare_instance=Song(1, "Premam", "Malare", 1, "Vijay Yesudas", "5:16")


malare_instance.get_song()

