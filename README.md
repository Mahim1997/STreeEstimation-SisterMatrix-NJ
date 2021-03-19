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


### Running:

```bash

```
