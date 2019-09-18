#This script is tested with
#>NC_006096.5 Gallus gallus breed Red Jungle Fowl isolate RJF #256 chromosome 9, GRCg6a
#(gc% = 43.4%)
#this program gave a gc% of 43.3 wich is not exactly the same


#Lets you enter the name of the file you want to analyse
inputs = input("Naam van het bestand: ")
#Opens the file thet is entered into the Python Shell
files = open(inputs,'r')
#Python reads the file
line = files.readline()
meta = ''
sequence = ''
while line:
    line = line.rstrip('\n')
    if '>' in line:
        meta =line
    else:
        sequence = sequence + line
    line = files.readline()
#counts all the A nucleotiden in the sequence
A = sequence.count("A")
#counts all the A nucleotiden in the sequence
T = sequence.count("T")
#counts all the A nucleotiden in the sequence
C = sequence.count("C")
#counts all the A nucleotiden in the sequence
G = sequence.count("G")
#prints the sequence
print(meta)
print(sequence)
#adds all the A,T,C and G counts up
an = (A + T + C + G)
print("Deze sequentie heeft ", (an), "nucleotiden.")
#calculates the gc% of the given sequence
GCpersentage = (((C + G)/(an))*100)
print("Het persentage CG in de sequentie is ", (round(GCpersentage, 1)), "procent")
