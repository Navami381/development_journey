#title,language,run_time,year,rating

movies=[
   ["kgf","kannada",150,2005,8],            #0
    ["balan","malayalam",130,2026,7],
    ["ramayan","hindi",150,2026,8],
    ["abcd","malayalam",140,2008,6],
    ["goatlyf","malayalam",160,2024,9]

]
#runtime,yr,rating of abcd
print(movies[3][2:])

#display all movie_titles
all_movies=[m[0] for m in movies]
print(all_movies)

#display all movie years
all_yrs={m[-2] for m in movies}
print(all_yrs)

#display all movie language
all_lang={m[1] for m in movies}
print(all_lang)