class Csvconvertor:

    def getcsv(self,separator,inputfile):
        csvfilepath = "C:\\Users\\Aman\\PycharmProjects\\datagenerator\\csvconverter\\csv.txt"
        file1=open(inputfile,"r")
        r=file1.read()
        e=r.replace(separator,',')
        e.split(",")
        file2=open(csvfilepath,"w")
        file2.write(e)
        file2.close()
        return csvfilepath
