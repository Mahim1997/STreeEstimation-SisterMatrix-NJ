# import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import subprocess
import re

# dictionary_triplets = {} # dictionary to store triplets

def get_dict_triplets_model_tree(file_model_tree):
    f = open(file_model_tree)
    line = f.readline()
    line = line.replace("\n", "")
    f.close()

    tmp_file_name = "TEMP_FILE_INPUT_TRIPLETS_SODA"
    with open(tmp_file_name, "w") as fp:
        fp.write(line)



    result = subprocess.run(['./triplets.soda2103', 'printTriplets', tmp_file_name], stdout=subprocess.PIPE)
    
    results_str = result.stdout.decode('utf-8')
    results_str = results_str.strip() # remove the empty line at the end
    
    results_str = re.sub("\n", "));\n(", results_str) # add initial brackets
    results_str = re.sub("^", "(", results_str) # for the very first
    results_str = re.sub("$", "));", results_str) # for the very last
    results_str = re.sub(" ", ",", results_str) # change white space to comma, ((11,9,|,5,6));
    results_str = re.sub(",\|,", ",(", results_str) # change ,|, to ),( to form ((11,9),(5,6));

    # print(results_str)

    results_array = results_str.split("\n") # split to form each quartets


    dictionary_model_tree_triplets = {}

    for line_result in results_array:
        if line_result not in dictionary_model_tree_triplets: # THIS line doesn't exist in dictionary
            dictionary_model_tree_triplets[line_result] = 1 # initialize to 1
        else: # THIS line does exist in dictionary, so increment
            dictionary_model_tree_triplets[line_result] += 1

    return dictionary_model_tree_triplets


def get_dict_weighted_triplets(file_weighted_triplets):
    dictionary_weighted_triplets = {}
    total_weight = 0.0
    with open(file_weighted_triplets, "r") as fin:
        line = fin.readline()
        while line:
            line = line.strip()
            vals = line.split(" ")
            ## IS THIS checking necessary ?? maybe redundant... need to check later.
            if vals[0] not in dictionary_weighted_triplets:
                wt = float(vals[1])
                total_weight += wt
                dictionary_weighted_triplets[vals[0]] = float(wt)
            # read next line
            line = fin.readline()

    return dictionary_weighted_triplets, total_weight


def calculate_triplet_score(file_model_tree, file_weighted_triplets):
    dictionary_weighted_triplets, total_weight = get_dict_weighted_triplets(file_weighted_triplets)
    dictionary_model_tree_triplets = get_dict_triplets_model_tree(file_model_tree)

    satisfied_weight = 0.0

    for triplet_key in dictionary_model_tree_triplets:
        if triplet_key in dictionary_weighted_triplets:
            satisfied_weight += dictionary_weighted_triplets[triplet_key]

    # print(dictionary_model_tree_triplets)
    print(satisfied_weight, total_weight, (satisfied_weight/total_weight))







####################################################### main ######################################################

def printUsage():
    print("python3 calculate_triplet_score.py <model-tree> <weighted-triplets>")
    exit()

if len(sys.argv) != 3:
    printUsage()


calculate_triplet_score(str(sys.argv[1]),str(sys.argv[2]))