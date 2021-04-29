# Species Tree Estimation using Sister Matrices from weighted quartets & triplets and using Neighbor Joining

For Species Tree estimation using FastME (NJ) and sister matrix


### Pipeline (with quartets):

1. Generate allquarttripletsets embedded weighted quartets from a set of gene trees
2. Generate the most dominant (i.e. best weighted) quartets from all combinations of quartets


### Pipeline (with triplets):

1. Generate all embedded weighted triplets from a set of gene trees
2. Generate the most dominant (i.e. best weighted) triplets from all combinations of triplets

## Pipeline (common steps):

3. Form a sister matrix using the above weighted quartets (S: sister/similarity matrix)
4. Form a difference matrix (D) using S i.e. D = 1 - S (element-wise, normalized).
5. Run NJ on this D matrix.

### Dependencies:

1. Needs fastme to be setup and the tool "fastme-2.1.5.2-linux64" in the same directory as the required python scripts
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


## Acknowledgement

- Neighbor Joining is computed by the [FastME](http://www.atgc-montpellier.fr/fastme/) tool.

  Lefort, Vincent et al. “FastME 2.0: A Comprehensive, Accurate, and Fast Distance-Based Phylogeny Inference Program.” Molecular biology and evolution vol. 32,10 (2015): 2798-800. doi:10.1093/molbev/msv150

- SisterEstimation uses some methods of the [PhyloNet](https://bioinfocs.rice.edu/phylonet) package for rf computations.
    
    C. Than, D. Ruths, L. Nakhleh (2008) PhyloNet: A software package for analyzing and reconstructing reticulate evolutionary histories, BMC Bioinformatics 9:322.
