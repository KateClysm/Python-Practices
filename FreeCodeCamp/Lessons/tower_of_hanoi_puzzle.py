NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1)) #Se crea la torre A como una lista con los discos del más grande (5) al más chico (1)
B = []
C = []

#Función recursiva para mover n discos desde la torre source hasta la torre target, usando auxiliary como ayuda.
def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
    # move the nth disk from source to target
    target.append(source.pop())
        
    # display our progress
    print(A, B, C, '\n')
        
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)