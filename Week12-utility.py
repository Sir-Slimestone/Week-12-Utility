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

