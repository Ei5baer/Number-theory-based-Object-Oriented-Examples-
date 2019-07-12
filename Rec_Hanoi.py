#Hanoi_tow = [[1],[2],[3],[4],[5],[6]]

#Parameters to this function are number of disks, three rods

def hanoi (N, src, mid, dst):
    if(N==1):
        print("moving top disk from" + src + "to" + dst )
        return
    hanoi(N-1,src, dst, mid)
    print ("moving top disk from " + src + " to " + dst)
    hanoi(N-1, mid, src, dst)
    if (N==0):
        print ("Nope")

T_A = "T_A"
T_B = "T_B"
T_C = "T_C"

hanoi (6, T_A, T_B, T_C)
    
    


