def s(n):
    pr=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if (pr[p]==True):
            for i in range(p*p, n+1, p):
                pr[i]=False
        p+=1
    for p in range(2, n+1):
        if pr[p]:
            print(p)
n=int(input("Enter a number: "))
print("The following are the prime numbers smaller")
print("than or equal to: ", n)
s(n)
