from exercise import movies

def cate_gory(cat):
    for movie in movies:
        if movie['category'] == cat:
            print(movie['name'])

cat = input()
cate_gory(cat)

