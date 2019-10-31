N=int(input())
for N in range(2, N):
    if all(N%i!=0 for i in range(2,N)):
        print(N, end=" ")
