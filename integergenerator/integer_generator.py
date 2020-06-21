import random
class IntegerGenerator():

    def integergenerator(self,filecsvpath,numberofrecord):
        list1=[]
        index=[0, 1]
        f=open(filecsvpath, "r")
        for line in f.readlines ():
            print(line)
            list1.append(line.split(","))
        print(list1)

        print(list1[1][index[0]])


        nf = open("generatedfile","w")
        for file in range(1, (numberofrecord + 1)):
            rand=random.randrange(1,numberofrecord+100)
            rand1 = random.randrange(1, numberofrecord + 100)
            list1.append([rand,list1[1][1],rand1])
            nf.writelines(str(list1[file]) + "\n")



