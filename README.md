# STree_FastME_NJ

For Species Tree estimation using FastME (NJ) and sister matrix


### Pipeline (with quartets):

1. Generate allquarttripletsets embedded weighted quartets from a set of gene trees
2. Generate the most dominant (i.e. best weighted) quartets from all combinations of quartets
3. Form a sister matrix using the above weighted quartets (S: sister/similarity matrix)
4. Form a difference matrix (D) using S i.e. D = 1 - S (element-wise, normalized).
5. Run NJ on this D matrix.


### Pipeline (with triplets):

1. Generate all embedded weighted triplets from a set of gene trees
2. Generate the most dominant (i.e. best weighted) triplets from all combinations of triplets
3 - 5 are the same as with quartets.

### Dependencies:

1. Needs fastme application setup and the tool "fastme-2.1.5.2-linux64"
2. For quartets, need the "quartet-controller.sh", "summarize_quartets.py" and "numeric_form_matrix_quartets.py" scripts
3. For triplets, need the "triplet_count.sh", "triplet-encoding-controller.sh" and "numeric_form_matrix_quartets.py" scripts

### Running:

#### For Quartets: 

```bash
  python3 SCRIPTS_For_NJ_quartets/get_NJ_Tree_using_quartets.py <best-wqrts-file> <output-file-name>
```

#### For Triplets:

```bash
  python3 SCRIPTS_For_NJ_triplets/compute_NJ_Tree_using_triplets.py <best-wtriplets-file> <output-file-name>
```
