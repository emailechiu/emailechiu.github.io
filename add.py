print("I am a very smart kid, I can add to 10000 very quickly!") 
while (1):
    print()
    try:
        n=input("Tell me any 4-digit positive integer you want to add to from 1? ")
        n=int(n)
        if (n<1 or n>9999): 
            print("You entered an out of range integer, try again") 
        else: 
            result=0
            for i in range(1,n+1):
               print(i,end="")
               if i<n: print('+',end="")
               result=result+i
            print("=",end="")
            print(result)
    except ValueError:
         print("Not an integer, try again")
 
