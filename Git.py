def list_prime(o):
    for k in range(2,o+1):
        for p in range(2,k):
            if (k%p)==0:
                break
        else:
            print(k,end=' ')
    print()
list_prime(50)


val =50
print([x for x in range(2,val+1) if all ( x%y != 0 for y in range(2,x))])