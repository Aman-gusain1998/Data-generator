import random

class StringGenerator:

    def getString(self,sequence):
        stringfor = ""
        for i in range(1, 7):
            n = random.choice(sequence)
            stringfor = stringfor + n
        return stringfor

    def stringgenerator(self,filecsvpath,numberofrecords):
        list1=[]
        index=[1]
        sequence = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
                    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        f = open(filecsvpath, "r")
        for line in f.readlines():
            list1.append(line.split(","))

        nf = open("generatedfile", "w")
        for i in range(1, numberofrecords + 1):
            list1.append([list1[1][0], self.getString(sequence), list1[1][2]])
            nf.writelines(str(list1[i]) + "\n")
