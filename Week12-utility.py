#Jordan Nealon
#CSCI 102 - Section E
#Week 12 Part A
def PrintOutput(string):
    print("OUTPUT " + string)
def LoadFile(file):
    text = open(file, "r")
    out = text.readlines()
    text.close()
    return out
def UpdateString(string1, string2, index):
    out = string1[0:index] + string2 + string1[index+1:-1] + string1[-1]
    print("OUTPUT " + out)
def FindWordCount(listin, string):
    count = 0
    for i in listin:
        find = True
        check = i
        while find:
            if string in check:
                count += 1
                check = check[check.find(string)+1:-1] + check[-1]
            else:
                find = False
    return count

