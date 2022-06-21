def solve(A, B):
    len_b = len(B)
    flag_0 = 0
    sub_arr_0 = 0
    for i in range(len_b-1):
        if B[i] == 0:
            flag_0 += 1
        if B[i] == 1 and flag_0!=0:
            sub_arr_0 += (flag_0 * (flag_0 + 1) // 2)
            flag_0 = 0
    if B[len_b - 1] == 0:
        flag_0 += 1
        print((flag_0 * (flag_0 + 1) // 2))
        sub_arr_0 += (flag_0 * (flag_0 + 1) // 2)
    else:
        sub_arr_0 += (flag_0 * (flag_0 + 1) // 2)



    return (A*(A+1)//2) - sub_arr_0


A = 5
B = [ 0, 1, 1, 0, 1 ]

A = 9
B = [ 1, 0, 0, 1, 1, 1, 1, 1, 1 ]


# A = 5
# B = [ 0, 1, 0, 0, 0 ]

print(solve(A,B))