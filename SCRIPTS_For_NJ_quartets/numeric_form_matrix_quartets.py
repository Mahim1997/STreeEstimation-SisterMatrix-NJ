import sys
import numpy as np

# inputFile = "all_gt.triplets"
inputFile = sys.argv[1]

dictionary = {}
quartet_cnt = 0

taxa_list = []


with open(inputFile) as f:
    for string in f:
        if string != "\n":
            string = string.replace("\n", "")
            string = string.replace("(", "")
            string = string.replace(")", "")
            # string = string.replace(",", "")  # Do NOT replace COMMA
            string = string.replace("; ", ",")

            arr = string.split(",")
            (tax1, tax2, tax3, tax4, weight) = arr

            t1 = int(tax1)
            t2 = int(tax2)
            t3 = int(tax3)
            t4 = int(tax4)
            weight = float(weight)

            if t1 not in taxa_list:
                taxa_list.append(t1)
            if t2 not in taxa_list:
                taxa_list.append(t2)
            if t3 not in taxa_list:
                taxa_list.append(t3)
            if t4 not in taxa_list:
                taxa_list.append(t4)



            # if sisters not in pairs_list:
            #     pairs_list.append(sisters)
            
            # print(line, sisters, weight)

            quartet_cnt += weight

            ## one side.
            sisters = (t1, t2)
            sisters_reverse = (t2, t1)
            if sisters not in dictionary:
                dictionary[sisters] = weight
                dictionary[sisters_reverse] = weight
            else:
                dictionary[sisters] += weight
                dictionary[sisters_reverse] += weight

            ## other side.
            sisters = (t3, t4)
            sisters_reverse = (t4, t3)
            if sisters not in dictionary:
                dictionary[sisters] = weight
                dictionary[sisters_reverse] = weight
            else:
                dictionary[sisters] += weight
                dictionary[sisters_reverse] += weight

for key in dictionary:
    dictionary[key] = quartet_cnt - dictionary[key]
    dictionary[key] = float(dictionary[key])/float(quartet_cnt)


# print(len(taxa_list))
# print(taxa_list)

# print(len(pairs_list))
# for sis in pairs_list:
#     print(sis)

# print("-----------------------------------")

# for k in dictionary.keys():
#     print(k, dictionary[k])


for i in range(0, len(taxa_list)):
    for j in range(i, len(taxa_list)):
        v1 = taxa_list[i]
        v2 = taxa_list[j]
        pair_1 = (v1, v2)
        pair_2 = (v2, v1)
        if pair_1 not in dictionary.keys():
            if pair_2 not in dictionary.keys():
                dictionary[pair_1] = 1
                dictionary[pair_2] = 1



# print(len(dictionary))
# for key in dictionary.keys():
#     print(key, dictionary[key])



###########################################################
###########################################################
###########################################################

#################### numpy matrix 2D ######################

_2D_matrix = np.ones((len(taxa_list), len(taxa_list)))

for key in dictionary.keys():
    (v1, v2) = key
    _2D_matrix[v1 - 1, v2 - 1] = dictionary[key]


################ this format should be maintained ################

print(len(taxa_list))
for idx_row in range(len(_2D_matrix)):
# for row in _2D_matrix:
    row = _2D_matrix[idx_row]
    print((idx_row + 1), end='  ')
    for col in row:
        print(col, end='  ')
    print("")