

def main():
    char= str(input())
    print(reverse(char))
    return  0

def reverse(char):
    if len(char)==0:
        return char
    return reverse(char[1:])+char[0]

if __name__=='__main__':
    main()
