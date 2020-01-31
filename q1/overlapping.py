def overlapping(L1,L2):
    #define coordinates of the 2 lines
    
    x1= L1[0]
    x2=L1[1]
    x3=L2[0]
    x4=L2[1]

    #if any coordinate of L2 in between the coordinates of line L1, there is overlapping

    if  (x1<=x3<=x2) or (x1<=x4<= x2):
         return ("overlapping")
    elif (x1>=x3>=x2) or (x1>=x4>= x2):
         return ("overlapping")

    #otherwise no overlapping

    else:
        return("no overlapping")




