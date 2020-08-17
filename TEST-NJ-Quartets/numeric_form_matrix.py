import sys
import numpy as np

# inputFile = "all_gt.triplets"
inputFile = sys.argv[1]

dictionary = {}
triplet_cnt = 0

taxa_list = []
pairs_list = []

with open(inputFile) as f:
    for line in f:
        if line != "\n":
            line = line.replace("\n", "")
            line = line.replace(" ", "")
            line = line.replace(";", " ")

            arr = line.split(" ")
            weight = float(arr[1])
            triplet = arr[0].replace(" ", "")

            triplet = triplet.replace("(", "")
            triplet = triplet.replace(")", " ")
            triplet = triplet.replace(" ", "")

            t_arr = triplet.split(",")
            t1 = int(t_arr[0])
            t2 = int(t_arr[1])
            t3 = int(t_arr[2])

            if t2 not in taxa_list:
                taxa_list.append(t2)
            if t3 not in taxa_list:
                taxa_list.append(t3)
            if t1 not in taxa_list:
                taxa_list.append(t1)

            sisters = (t2, t3)
            sisters_reverse = (t3, t2)
            if sisters not in pairs_list:
                pairs_list.append(sisters)
            
            # print(line, sisters, weight)

            triplet_cnt += weight

            if sisters not in list(dictionary.keys()):
                dictionary[sisters] = weight
                dictionary[sisters_reverse] = weight
            else:
                dictionary[sisters] += weight
                dictionary[sisters_reverse] += weight

for key in list(dictionary.keys()):
    dictionary[key] = triplet_cnt - dictionary[key]
    dictionary[key] = float(dictionary[key])/float(triplet_cnt)


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