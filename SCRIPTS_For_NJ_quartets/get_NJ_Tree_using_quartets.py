"""
Need the following files.
1. summarize_quartets_stdin.pl
2. triplet_count.sh
3. triplet-encoding-controller.sh
4. triplets.soda2103
5. form_max_matrix_quartets.py

AND TO RUN NJ.
6. fastme-2.1.5.2-linux64

"""
#### Import things #####
########################
import sys
import os
import re

########################
TEMP_QUARTET_FILE = "TEMP_QUARTET_FILE"
TEMP_QUARTET_CONVERTED_FILE = "TEMP_QUARTET_CONVERTED_FILE"
TEMP_MATRIX_FOR_NJ_QUARTETS = "TEMP_MATRIX_FOR_NJ_QUARTETS"
TEMP_OUTPUT_NJ_TREE_QUARTETS = "TEMP_OUTPUT_NJ_TREE_QUARTETS"
########################

inputFile = sys.argv[1]
outputFile = sys.argv[2]

print("Input file = ", inputFile, ", Output file = ", outputFile)



### Remove these files ####
# os.system("rm -f TEMP_QUARTET_FILE")
# os.system("rm -f TEMP_QUARTET_CONVERTED_FILE")
# os.system("rm -f TEMP_MATRIX_FOR_NJ_QUARTETS")
# os.system("rm -f TEMP_OUTPUT_NJ_TREE_QUARTETS")



dictionary = {} # empty dictionary
dictionary_reverse = {} # also empty dictionary

def get_new_quartets(string, dictionary):
    string = string.replace("\n", "")
    string = string.replace("(", "")
    string = string.replace(")", "")
    # string = string.replace(",", "")  # Do NOT replace COMMA
    string = string.replace("; ", ",")
    arr = string.split(",")
    (tax1, tax2, tax3, tax4, weight) = arr
    # return (tax1, tax2, tax3, weight)
    # (tax1, (tax2, tax3)): weight

    # Put in reversed dictionary
    if dictionary[tax1] not in dictionary_reverse:
        dictionary_reverse[dictionary[tax1]] = tax1
    if dictionary[tax2] not in dictionary_reverse:
        dictionary_reverse[dictionary[tax2]] = tax2
    if dictionary[tax3] not in dictionary_reverse:
        dictionary_reverse[dictionary[tax3]] = tax3
    if dictionary[tax4] not in dictionary_reverse:
        dictionary_reverse[dictionary[tax4]] = tax4

    tax1 = dictionary[tax1]
    tax2 = dictionary[tax2]
    tax3 = dictionary[tax3]
    tax4 = dictionary[tax4]


    ## _quartet = "(" + str(tax1) + ",((" + str(tax2) + "," + str(tax3) + ")); " + weight + "\n"
    ## ((A,B),(C,D)); 41
    
    _quartet = "((" + str(tax1) + "," + str(tax2) + "),(" + str(tax3) + "," + str(tax4) + ")); " + weight + "\n"
    
    return _quartet

def obtain_taxa_name(cnt):
    # return "tax_" + str(cnt)
    return str(cnt)

def put_to_dictionary(string, taxa_counter=1):
    # Use the string of triplets to put to dictionary and convert back to new triplets.
    string = string.replace("\n", "")
    string = string.replace("(", "")
    string = string.replace(")", "")
    # string = string.replace(",", "")  # Do NOT replace COMMA
    string = string.replace("; ", ",")

    arr = string.split(",")
    (tax1, tax2, tax3, tax4, weight) = arr
    
    if tax1 not in dictionary:
        dictionary[tax1] = obtain_taxa_name(taxa_counter)
        taxa_counter += 1
    if tax2 not in dictionary:
        dictionary[tax2] = obtain_taxa_name(taxa_counter)
        taxa_counter += 1
    if tax3 not in dictionary:
        dictionary[tax3] = obtain_taxa_name(taxa_counter)
        taxa_counter += 1
    if tax4 not in dictionary:
        dictionary[tax4] = obtain_taxa_name(taxa_counter)
        taxa_counter += 1
    
    # print(tax1, tax2, tax3, tax4, weight)
    
    return taxa_counter

################## main ######################

## Step 1. Form quartets.
# command = "./quartet-controller.sh " + str(inputFile) + " " + str(TEMP_QUARTET_FILE)
# os.system(command)

## Step 2. Convert quartets taxa set to 1,2,3, ...

# Obtain the dictionary
taxa_counter = 1
list_quartets = []
with open(inputFile, "r") as f:
    string = f.readline()
    while string:
        list_quartets.append(string)
        taxa_counter = put_to_dictionary(string, taxa_counter)
        string = f.readline()



# Re-write using the dictionary
with open(TEMP_QUARTET_CONVERTED_FILE, "w") as f:
    for line in list_quartets:
        _quartet = get_new_quartets(line, dictionary)
        # print(_quartet)
        f.write(_quartet)


print("------ Forward -----")
print(dictionary)
print("+++++ Backward ++++++")
print(dictionary_reverse)


##  Form the max-matrix-quartets using python script
command = "python3 numeric_form_matrix_quartets.py " + TEMP_QUARTET_CONVERTED_FILE + " > " + TEMP_MATRIX_FOR_NJ_QUARTETS
os.system(command)

## Run NJ fast-me 
command = "./fastme-2.1.5.2-linux64 -i TEMP_MATRIX_FOR_NJ_QUARTETS -o TEMP_OUTPUT_NJ_TREE_QUARTETS -m NJ"
os.system(command)

## Remove whitespaces and newlines
command = "sed -i \'/^[[:space:]]*$/d\' TEMP_OUTPUT_NJ_TREE_QUARTETS"
os.system(command)

## Remove branches

command = "sed -i \'s/:[0-9]*\\.[0-9]*//g\' TEMP_OUTPUT_NJ_TREE_QUARTETS"
os.system(command)


## Convert back using dictionary.
with open(TEMP_OUTPUT_NJ_TREE_QUARTETS, "r") as f:
    tree = f.readline()
    print("#### Printing numeric tree #####")
    print(tree)
    # dictionary = {"NORTH":"N", "SOUTH":"S" } 

# https://stackoverflow.com/questions/10931150/phps-strtr-for-python
# Convert back 


def strtr(s, repl):
  pattern = '|'.join(map(re.escape, sorted(repl, key=len, reverse=True)))
  return re.sub(pattern, lambda m: repl[m.group()], s)


decodedTree = strtr(tree, dictionary_reverse)

# Convert back using reverse dictionary

print(decodedTree)

with open(outputFile, "w") as f:
    f.write(decodedTree)
