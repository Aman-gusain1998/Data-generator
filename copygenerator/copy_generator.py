class CopyGenerator:


    def copyGenerator(self,filecsvpath,numberofrecord):
        copygeneratorfilepath="generatedfile"
        fo = open(filecsvpath,"r")
        a = fo.read()
        print(a)
        fo.close()
        fr = open(copygeneratorfilepath,"w")
        for file in range (1,(numberofrecord+1)):
            print(a)
            fr.writelines(a+"\n")
        fr.close()
        return copygeneratorfilepath


