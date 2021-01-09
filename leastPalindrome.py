def leastPalindrome(s):

    if(len(s) % 2 == 0):
        l = len(s)
        half = int(l/2)
        front = s[0 : half]
        back = s[half : len(s)]
        i = len(front)-1
        j = 0
        while(i > 0 and j < len(back)):
            if(ord(front[i]) < ord(back[j])):
                front = incrementString(front)
                return front + front[::-1]

            elif(ord(front[i]) > ord(back[j])):
                return front + front[::-1]

            else:
                i -= 1
                j += 1

        return s

    else:

        front = s[0 : int((len(s)-1)/2)]
        back = s[int((len(s)+1)/2) : len(s)]
        midChar = s[int((len(s)-1)/2)]
        i = len(front)-1
        j = 0
        while(i > 0 and j < len(back)):
            if(ord(front[i]) < ord(back[j])):
                front = incrementString(front)
                return front + midChar + front[::-1]

            elif(ord(front[i]) > ord(back[j])):
                return front + midChar + front[::-1]

            else:
                i -= 1
                j += 1

        return s

def incrementString(s):
    if(s == ""):
        return "a"

    if(s[len(s) - 1] != "z"):
        return s[0 : len(s) - 1] + chr(ord(s[len(s) - 1]) + 1)

    else:
        return incrementString(s[0 : len(s) - 1]) + "a"
