A = "abcdsfhjagj"

char_min = 'z'
char_max = 'z'
size = len(A)

for i in range(size):
    if i != size - 1 and A[i] < char_min:
        char_min = A[i]
    elif i != 0 and A[i] < char_max:
        char_max = A[i]

print(char_min+char_max)