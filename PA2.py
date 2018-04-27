#Kevin Wallace
#Bioinformatics
#The goal of the protein is to determine the percent of each protein is made up of 
#a specific amino acid.

# imports Bioinformatics module so we can access its funtions 
import BIOL420

# Testing the function pctOfProtein in the bioinformatics module
print BIOL420.pctOfProtein("msrslllrfllfllllpplp", ["L"]) 
print BIOL420.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]) 
print BIOL420.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) 
print BIOL420.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L'])
