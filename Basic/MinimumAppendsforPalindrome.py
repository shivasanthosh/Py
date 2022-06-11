string = "njqeeosasrtcawhspirwsbgg"

def isPalindrome(s):
    return s == s[::-1]

def revIt(s):
    return s[::-1]

def getMinLastValue(string):
    for i in range(len(string)-1,-1,-1):
        if isPalindrome(string[-i:]):
            return len(string[-i:])




def generatePalindrome(s):
    string = str(s)
    minremoval=getMinLastValue(s)
    minLast = string[:-minremoval]
    newPalindrome = string+revIt(minLast)
    print(newPalindrome)
    print(len(newPalindrome)-len(string))
    print(isPalindrome(newPalindrome))

generatePalindrome(string)





