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
def ScoreFinder(players, scores, string):
    for i in range(len(players)):
        players[i] = players[i].lower()
    string = string.lower()
    if string in players:
        for i in range(len(players)):
            if players[i] == string:
                break
        print("OUTPUT " + string[0].upper() + string[1:-1] + string[-1] + " got a score of " + str(scores[i]))
    else:
        print("OUTPUT player not found")
def Union(list1, list2):
    out = list1
    for i in list2:
        if not(i in list1):
            out.append(i)
    return out
def Intersection(list1, list2):
    out = []
    for i in list1:
        if i in list2:
            out.append(i)
    return out
def NotIn(list1, list2):
    out = []
    for i in list1:
        if not(i in list2):
            out.append(i)
    return out

