for i in range(1, 8):
    for j in range(i, 50, 7):
        if j == 8 and j == 9:
            print(f" {j}", end=" ")
        else:
            print(j, end=" ")
    print()
    