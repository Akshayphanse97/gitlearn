def dict_word(s):
    d={}
    for char in s:
        d[char]=s.count(char)

    return d

print(dict_word('akshay'))


# e = {'name':'','age': ,'fav_movies':[],'fav_song':[]}
# user=input("enter the your name ,age,favries_movies,fav_song and seprates comma',' " ).split(',')
# for i in user:
#     e[i]=i



