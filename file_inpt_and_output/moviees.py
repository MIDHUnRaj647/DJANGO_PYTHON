f=open('movies.csv')
dict={}
for i in f:
    data=i.split(',')
    movie=data[1]
    year=data[2]
    rating=data[3]
    if movie not in dict:
        dict[movie]={'movie':movie,'year':year,'rating':rating}
    else:
        dict[movie]={'movie':movie, 'year':year, 'rating':rating}
def printmovie(**args):
    movi=args.get('movie')
    if movi in dict:
        print(movi)
        if "property" in args:
            prop=args["property"]
            if prop in dict[movi]:
                print(prop,'>>',dict[movi][prop])
r=0
y=0
enter=input('enter r for rating, y for year')
if enter=="r":
    printmovie(movie="Emma", property='rating')
elif enter=="y":
    printmovie(movie="Emma", property='year')
else:
    print("wrong entry")