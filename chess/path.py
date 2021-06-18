import sys

#declaring variables
from_x=0
from_y=0
to_x=0
to_y=0
l_from_x=0
l_from_y=0
l_to_x=0
l_to_y=0
l_current_x=0
l_current_y=0
l_target_x=0
l_target_y=0
amount_x=0
amount_y=0

#grabing input
from_x=int(sys.argv[1])
from_y=int(sys.argv[2])
to_x=int(sys.argv[3])
to_y=int(sys.argv[4])\

#calcuation
l_from_x=2*from_x
l_from_y=2*from_y
l_to_x=2*to_x
l_to_y=2*to_y

l_current_x=l_from_x
l_current_y=l_from_y
l_target_x=l_to_x
l_target_y=l_to_y

#======================
#=== actual pathing ===
#======================

#start
if(from_x < 6):
    if(from_y < 4):
        print("diagonaal rechts naar beneden")
        l_current_x+=1
        l_current_y+=1
    else:
        print("diagonaal rechts naar boven")
        l_current_x+=1
        l_current_y-=1
else:
    if(from_y < 4):
        print("diagonaal links naar beneden")
        l_current_x-=1
        l_current_y+=1
    else:
        print("diagonaal links naar boven")
        l_current_x-=1
        l_current_y-=1


#target
if(to_x < 6):
    if(to_y < 4):
        #rechts beneden
        l_target_x+=1
        l_target_y+=1
    else:
        #rechts boven
        l_target_x+=1
        l_target_y-=1
else:
    if(to_y < 4):
        #links beneden
        l_target_x-=1
        l_target_y+=1
    else:
        #links boven
        l_target_x-=1
        l_target_y-=1

#horizontal
if(l_current_x < l_target_x):
    amount_x=((l_target_x-l_current_x)/2)
    amount_x=round(amount_x, None)
    amount_x=str(amount_x)
    print(amount_x + " vakje(s) naar rechts")  
else:
    amount_x=((l_current_x-l_target_x)/2)
    amount_x=round(amount_x, None)
    amount_x=str(amount_x)
    print(amount_x + " vakje(s) naar links")  

#vertical
if(l_current_y < l_target_y):
    amount_y=((l_target_y-l_current_y)/2)
    amount_y=round(amount_y, None)
    amount_y=str(amount_y)
    print(amount_y + " vakje(s) naar beneden")  
else:
    amount_y=((l_current_y-l_target_y)/2)
    amount_y=round(amount_y, None)
    amount_y=str(amount_y)
    print(amount_y + " vakje(s) naar beneden") 


if(to_x < 6):
    if(to_y < 4):
        #rechts beneden
        print("diagonaal rechts naar beneden")
    else:
        #rechts boven
        print("diagonaal rechts naar boven")
else:
    if(to_y < 4):
        #links beneden
        print("diagonaal links naar beneden")
    else:
        #links boven
        print("diagonaal links naar boven")












""" def get_path(from_x,from_y,to_x,to_y):

    l_from_x=0

    l_from_x=2*from_x

    print(l_from_x) """

