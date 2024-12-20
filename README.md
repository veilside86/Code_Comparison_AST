# Code comparison with AST
This study aims to explore the potential of leveraging Python code analysis and Abstract Syntax Trees (AST) to detect cheating and plagiarism in programming assignments.

## Result
- Compare with AI code

![Figure_1](https://github.com/user-attachments/assets/c664c55d-2683-4eb3-abbc-b4e5035d585c)

- Compare with Student code

![Figure_2](https://github.com/user-attachments/assets/d8c4b9e0-84e2-4cb6-93d5-252911d9ca1d)


## install requirements packages
> window
```
pip3 install -r requirements.txt
```
> mac OS
```
pip3 install -r requirements.txt
```

## To-Do List
1. [x] Apply the sorting algorithm to sort the trees to compare step by step
2. [x] Set up edit distance (Levenshtein distance) to compare the AST objects and calculate similarity
3. [x] Set up munkres (Hungarian) algorithm
4. [x] K-means Clustering to show similarity visually

## Documentation
+ [AST](https://docs.python.org/3/library/ast.html#module-ast)
  - [Munkres Module](https://software.clapper.org/munkres/)
  - [Levenshtein Module](https://rapidfuzz.github.io/Levenshtein/levenshtein.html#distance)
+ [Edit distance Algorithm](https://en.wikipedia.org/wiki/Levenshtein_distance)
+ [Hungarian Algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm)
+ [Kmeans Clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
