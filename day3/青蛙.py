day=1
i=0

while i<20:
    if i<20:
        i=i+3
        print("第",day,"天最高爬了",i,"米")
        if i<20:
            i=i-2
        else:
            print("终于在第",day,"天爬了出来！")
    day=day+1

