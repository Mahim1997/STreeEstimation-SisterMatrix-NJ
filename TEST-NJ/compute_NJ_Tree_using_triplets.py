"""
Need the following files.
1. summarize_triplets_stdin.pl
2. triplet_count.sh
3. triplet-encoding-controller.sh
4. triplets.soda2103
5. form_max_matrix_triplets.py

AND TO RUN NJ.
6. fastme-2.1.5.2-linux64

"""
#### Import things #####
########################
import sys
import os
import re

########################
TEMP_TRIPLET_FILE = "TEMP_TRIPLET_FILE"
TEMP_TRIPLET_CONVERTED_FILE = "TEMP_TRIPLET_CONVERTED_FILE"
TEMP_MATRIX_FOR_NJ = "TEMP_MATRIX_FOR_NJ"
TEMP_OUTPUT_NJ_TREE = "TEMP_OUTPUT_NJ_TREE"
########################

inputFile = sys.argv[1]
outputFile = sys.argv[2]

print("Input file = ", inputFile, ", Output file = ", outputFile)



### Remove these files ####
# os.system("rm -f TEMP_TRIPLET_FILE")
# os.system("rm -f TEMP_TRIPLET_CONVERTED_FILE")
# os.system("rm -f TEMP_MATRIX_FOR_NJ")
# os.system("rm -f TEMP_OUTPUT_NJ_TREE")



dictionary = {} # empty dictionary
dictionary_reverse = {} # also empty dictionary

def obtain_new_triplets(string, dictionary):
    string = string.replace("\n", "")
    string = string.replace("(", "")
    string = string.replace(")", "")
    # string = string.replace(",", "")  # Do NOT replace COMMA
    string = string.replace("; ", ",")
    arr = string.split(",")
    (tax1, tax2, tax3, weight) = arr
    # return (tax1, tax2, tax3, weight)
    # (tax1, (tax2, tax3)): weight

    # Put in reversed dictionary
    if dictionary[tax1] not in dictionary_reverse.keys():
        dictionary_reverse[dictionary[tax1]] = tax1
    if dictionary[tax2] not in dictionary_reverse.keys():
        dictionary_reverse[dictionary[tax2]] = tax2
    if dictionary[tax3] not in dictionary_reverse.keys():
        dictionary_reverse[dictionary[tax3]] = tax3

    tax1 = dictionary[tax1]
    tax2 = dictionary[tax2]
    tax3 = dictionary[tax3]


    _triplet = "(" + str(tax1) + ",((" + str(tax2) + "," + str(tax3) + ")); " + weight + "\n"
    return _triplet

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
    (tax1, tax2, tax3, weight) = arr
    if tax1 not in list(dictionary.keys()):
        dictionary[tax1] = obtain_taxa_name(taxa_counter)
        taxa_counter += 1
    if tax2 not in list(dictionary.keys()):
        dictionary[tax2] = obtain_taxa_name(taxa_counter)
        taxa_counter += 1
    if tax3 not in list(dictionary.keys()):
        dictionary[tax3] = obtain_taxa_name(taxa_counter)
        taxa_counter += 1
    # print(tax1, tax2, tax3, weight)
    return taxa_counter

################## main ######################

## Step 1. Form triplets.
# command = "./triplet-encoding-controller.sh " + str(inputFile) + " " + str(TEMP_TRIPLET_FILE)
# os.system(command)

## Step 2. Convert triplets taxa set to 1,2,3, ...

# Obtain the dictionary
taxa_counter = 1
list_triplets = []
with open(inputFile, "r") as f:
    string = f.readline()
    while string:
        list_triplets.append(string)
        taxa_counter = put_to_dictionary(string, taxa_counter)
        string = f.readline()



# Re-write using the dictionary
with open(TEMP_TRIPLET_CONVERTED_FILE, "w") as f:
    for line in list_triplets:
        _triplet = obtain_new_triplets(line, dictionary)
        # print(_triplet)
        f.write(_triplet)


print("------ Forward -----")
print(dictionary)
print("+++++ Backward ++++++")
print(dictionary_reverse)

##  Form the max-matrix-triplets using python script
# command = "python3 form_max_matrix_triplets.py " + TEMP_TRIPLET_CONVERTED_FILE + " > " + TEMP_MATRIX_FOR_NJ
command = "python3 numeric_form_matrix.py " + TEMP_TRIPLET_CONVERTED_FILE + " > " + TEMP_MATRIX_FOR_NJ
os.system(command)

## Run NJ fast-me 
command = "fastme -i TEMP_MATRIX_FOR_NJ -o TEMP_OUTPUT_NJ_TREE -m NJ"
os.system(command)

## Remove whitespaces and newlines
command = "sed -i \'/^[[:space:]]*$/d\' TEMP_OUTPUT_NJ_TREE"
os.system(command)

## Remove branches

command = "sed -i \'s/:[0-9]*\\.[0-9]*//g\' TEMP_OUTPUT_NJ_TREE"
os.system(command)


## Convert back using dictionary.
with open(TEMP_OUTPUT_NJ_TREE, "r") as f:
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

