from copygenerator.copy_generator import CopyGenerator
from csvconverter.csv_convertor import Csvconvertor
from integergenerator.string_gen import StringGenerator
from integergenerator.integer_generator import IntegerGenerator

class Start:

    def __init__(self):
        pass

    def generator(self):

        numberofrecords = int(input("Enter the number of records you want to create"))
        filepath = str(input("Enter the file path of the file"))
        separator = str(input("Enter the separator of the file"))
        csvfilepath = Csvconvertor().getcsv(separator, filepath)
        return numberofrecords, csvfilepath

    def print_main_menu(self):
            print("##################  DATA GENERATOR MENU ################")

            print("1.) Copy Generator")
            print("2.) Random String Generator")
            print("3.) Random Integer Generator")

            option = int(input("Enter the choice"))

            if(option==1):
                print("Calling Copy Generator")
                numberofrecords, csvfilepath=self.generator()
                convertedfilepath=CopyGenerator().copyGenerator(csvfilepath,numberofrecords)
            elif(option==2):
                print("Calling String Generator")
                numberofrecords, csvfilepath=self.generator()
                convertedfilepath = StringGenerator().stringgenerator(csvfilepath,numberofrecords)
            elif(option==3):
                print("Calling Integer Generator")
                numberofrecords, csvfilepath=self.generator()
                convertedfilepath = IntegerGenerator().integergenerator(csvfilepath,numberofrecords)
            else:
              print("You entered the wrong value")

            return  convertedfilepath

st = Start()
filepath = st.print_main_menu()
print(filepath)