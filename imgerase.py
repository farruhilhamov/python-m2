import os
import datetime
sreda = os.getcwd()
print("\n",sreda,"\n")

now  = datetime.datetime.now()
ac = input("do you want to enter a path? y/n: ")
if ac == "y":
    path = input("enter a path with images: ")
    os.chdir(path)
else:
    pass
lists = os.listdir()
for i in lists:
    if i [len(i)-4:len(i)] == ".png" or i [len(i)-4:len(i)] == ".jpg":
        print(i) 
        sec = os.path.getmtime(i)
        date_time = datetime.datetime.utcfromtimestamp(sec)
        ts = date_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ") [:10].split("-")
        for s in range(0,3):
            ts [s] = int(ts[s])
        print(date_time)
        #print(datetime.datetime(ts))
        ranger = str(now-date_time)
        try:    
            if int(str(ranger) [0:2]) > 30:
                print("more than 30 days,deleted")
                os.remove("{}".format(i))
            else:
                print("fresh file")
        except:
            if int(str(ranger) [0:1]) > 30:
                print("more than 30 days,deleted")
                os.remove("{}".format(path+i))
            else:
                print("fresh file")
            print()

#C:\Users\Freddy\Pictures