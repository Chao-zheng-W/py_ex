lst=[{"title":"霸王别姬","actor":["葛优","张国荣"]},
     {"title":"三体","actor":["吴京","刘德华"]},
     {"title":"狂飙","actor":["张译","张颂文"]}]

#需求：输入演员名，得到ta出演的节目
name = input("演员名")
for item in lst:
    actors=item["actor"]
    title =item["title"]
    for actor in actors:
        if name == actor:
            print(name+"演了"+title)