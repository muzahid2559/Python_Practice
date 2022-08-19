# list of movies that i loves
fav_movie = []

while True:
    print("movie no 1" +str(len(fav_movie)+1) + "or press enter to stop adding to the list.")
    movie = input()

    if movie == "":
        break
    fav_movie = fav_movie+[movie]
if len(fav_movie) != 0:
    print("the lists are ")
    for i in range(len(fav_movie)):
        print(fav_movie[i])