# import matplotlib.pyplot as plt
import numpy as np
import sys
import math

dictionary_triplets = {} # dictionary to store triplets

def sort_triplets(tax1, tax2, tax3):
    list_custom = []
    list_custom.append(tax1)
    list_custom.append(tax2)
    list_custom.append(tax3)
    list_custom.sort()
    # (t1, t2, t3, t4) = list_custom
    return list_custom
def append_to_dictionary(line):
    for ch in ['(',')', ';']:
        if ch in line:
            line = line.replace(ch, "")
    line = line.replace(" ", ",")
    (tax1, tax2, tax3, weight) = line.split(",")
    weight = float(weight)

    (t1, t2, t3) = sort_triplets(tax1, tax2, tax3) # any sorting order

    # print(tax1, tax2, tax3, tax4, weight, t1, t2, t3, t4)
    key_current = (t1, t2, t3)

    if key_current not in dictionary_triplets: # Initialize as list
        dictionary_triplets[key_current] = []

    dictionary_triplets[key_current].append((tax1, tax2, tax3, weight)) # append to the list
def generate_best_triplets(inputFile,outputFile):

    with open(inputFile) as fileobject:
        for line in fileobject:
            append_to_dictionary(line)
    
    keys = list(dictionary_triplets.keys())
    three_tax_seq = keys[0:]
    f = open(outputFile, "w")
    for key in three_tax_seq:
        vals = dictionary_triplets[key]
        max_weight = -math.inf
        triplet_string = ""
        for val in vals:
            (_1, _2, _3, w) = val
            if (float(w)>=max_weight):
                max_weight = float(w)
                triplet_string = "(" + _1 + ",(" + _2 + "," + _3 + ")); " + str(w) + "\n"
            
        f.write(triplet_string)
    f.close() 
    #print(dictionary_triplets)
generate_best_triplets(str(sys.argv[1]),str(sys.argv[2]))