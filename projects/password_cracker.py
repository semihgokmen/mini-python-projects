import random

import time

characters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","y","u","v","z","w","x","q","1",
                  "2","3","4","5","6","7","8","9","0"," "]
password=input("mesaj:")
current=""
index=0

while True:
    
    i=random.choice(characters)

    if password[index].lower()==i:
        current=current+password[index]
        index=index+1


        if current==password:
            break
        else:
            pass
    else:
        pass

    
    
    print(current+i,end="\r")
    time.sleep(0.005)

time.sleep(0.1)
print(current)


