import datetime

def getdate():
    return datetime.datetime.now()
def write_item(client):
    if (client==1):
        item_type=int(input("press 1 for manga, press 2 for anime:"))
        if item_type==1:
            add_item=input("what do you want to add:")
            with open("luffy_manga.txt","a") as f:
                f.write(str([str(getdate())])+": "+add_item+"\n")
            print("successfully written")
        elif item_type==2:
            add_item=input("what do you want to add:")
            with open("luffy_anime.txt","a") as f:
                f.write(str([str(getdate())])+": "+add_item+"\n")
            print("successfully written")
    elif (client==2):
        item_type=int(input("press 1 for manga, press 2 for anime:"))
        if item_type==1:
            add_item=input("what do you want to add:")
            with open("naruto_manga.txt","a") as f:
                f.write(str([str(getdate())])+": "+add_item+"\n")
            print("successfully written")
        elif item_type==2:
            add_item=input("what do you want to add:")
            with open("naruto_anime.txt","a") as f:
                f.write(str([str(getdate())])+": "+add_item+"\n")
            print("successfully written")
    elif (client==3):
        item_type=int(input("press 1 for manga, press 2 for anime:"))
        if item_type==1:
            add_item=input("what do you want to add:")
            with open("ichigo_manga.txt","a") as f:
                f.write(str([str(getdate())])+": "+add_item+"\n")
            print("successfully written")
        elif item_type==2:
            add_item=input("what do you want to add:")
            with open("ichigo_anime.txt","a") as f:
                f.write(str([str(getdate())])+": "+add_item+"\n")
            print("successfully written")

def retrieve_item(client):
    if (client==1):
        item_type=int(input("press 1 for manga, press 2 for anime:"))
        if (item_type==1):
            with open("luffy_manga.txt") as f:
                for i in f:
                    print(i,end="")
        elif (item_type==2):
            with open("luffy_anime.txt") as f:
                for i in f:
                    print(i,end="")
    elif (client==2):
        item_type=int(input("press 1 for manga, press 2 for anime:"))
        if (item_type==1):
            with open("naruto_manga.txt") as f:
                for i in f:
                    print(i,end="")
        elif (item_type==2):
            with open("naruto_anime.txt") as f:
                for i in f:
                    print(i,end="")
    elif (client==3):
        item_type=int(input("press 1 for manga, press 2 for anime:"))
        if (item_type==1):
            with open("ichigo_manga.txt") as f:
                for i in f:
                    print(i,end="")
        elif (item_type==2):
            with open("ichigo_anime.txt") as f:
                for i in f:
                    print(i,end="")




client=int(input("press 1 for luffy, 2 for naruto, 3 for ichigo: "))
add_method=int(input("press 1 to write, press 2 to retrieve:"))
if add_method==1:
    write_item(client)
else:
    retrieve_item(client)


