#Kevin Wallace
#Bioinformatics
#The goal is to get the AT content and checks to see if it has high medium 
#or low content.

import BIOL420

#opens the file to be read
sequences = open("data.csv")

for line in sequences:
    #Splits the info at commas and stores each piece in its respective variable.
    columns = line.rstrip("\n").split(',')
    species = columns[0]
    sequence = columns[1]
    geneName = columns[2]
    geneExpression = columns[3]
    #gets the AT content of the sequence.
    ATcontent = BIOL420.AT_Content(sequence)
    #checks to see if the AT content is high, medium or low
    if BIOL420.HighAT(ATcontent) == True: 
        print "Your gene is called: %s" % geneName + " and it has high AT content at: %.3f" % ATcontent
    elif BIOL420.MedAT(ATcontent) == True:
        print "Your gene is called: %s" % geneName + " and it has medium AT content at: %.3f" % ATcontent
    #Could just be an else statement but to test the funtion for this program 
    #used the funtion. 
    elif BIOL420.LowAT(ATcontent) == True:
        print "Your gene is called: %s" % geneName + " and it has low AT content at: %.3f" % ATcontent