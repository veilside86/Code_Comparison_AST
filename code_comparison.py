import ast_fuzzy_comparison as afc
import os
import sys
import ast
import random
from _ast import *
from Levenshtein import ratio

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class NormIdentifiers(ast.NodeTransformer):
    def __init__(self):
        self.identifiers = {}
        super().__init__()

    def visit_Name(self, node):
        try:
            id = self.identifiers[node.id]
        except KeyError:
            id = f'id_{len(self.identifiers)}'
            self.identifiers[node.id] = id
        
        return ast.copy_location(Name(id=id), node)

class NormFunctions(ast.NodeTransformer):
    def __init__(self, func=None):
        self.identifiers = {}
        self.func = func
        super().__init__()

    def visit_FunctionDef(self, node):
        if self.func and self.func != node.name:
            return None
    
        try:
            name = self.identifiers[node.name]
        except KeyError:
            name = f'function{len(self.identifiers):x}'
            self.identifiers[node.name] = name

        for i, arg in enumerate(node.args.args):
          arg.arg = f'arg{i}'

        new_func = FunctionDef(name=name, args=node.args, body=node.body, decorator_list=node.decorator_list)

        if isinstance(new_func.body[0], Expr) and isinstance(new_func.body[0].value, ast.Constant):
            del new_func.body[0]
        
        return ast.copy_location(new_func, node)

def field_check(tree: AST) -> list:
    tree = NormFunctions(func=None).visit(tree)
    tree = NormIdentifiers().visit(tree)
    
    return tree


def compare_subtree(subtree_list1: list, subtree_list2: list):
    score = 0
    node_a = ast.unparse(subtree_list1)
    node_b = ast.unparse(subtree_list2)

    score += ratio(node_a, node_b)

    return round(score, 4)


def compare_multiple_files(base: list, programs: list) -> list:
    try:
        tree_list = list(map(lambda prog: field_check(ast.parse(prog)), programs))
        base = list(map(lambda prog: field_check(ast.parse(prog)), base))
    except:
        print("***Make sure your code is running properly***")
        # reindent
        sys.exit()

    result = []
    for program_tree_num in range(0, len(tree_list)):
        subtrees1 = base
        subtrees2 = tree_list[program_tree_num]

        similarity = compare_subtree(subtrees1, subtrees2)
        result.append(similarity * 100)
            
    return result


def show_plot(x, y, base_file_name):
    data_points = list(zip(x, y))
    num_clusters = 5
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(data_points)
    labels = kmeans.labels_

    plt.figure(figsize=(8, 6))

    for i in range(num_clusters):
        cluster_points = np.array([data_points[j] for j in range(len(data_points)) if labels[j] == i])
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i}')

    plt.xlim(0, 105)
    plt.ylim(0, 105)
    plt.title('Two AST Similarity')
    plt.xlabel("Similarity of Edit Distance Algorithm")
    plt.ylabel("Similarity of Munkres Algorithm")
    plt.gcf().text(0.02, 0.95, 'base file: {}'.format(base_file_name), fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    """
    Set up the path of the two files to compare
    """
    # For the mac
    # compare_file1 = "JunseokSampleData/fizzbuzz1.py"
    # compare_file2 = "JunseokSampleData/fizzbuzz2.py"

    # for the Window
    # compare_file1 = "source1.py"
    # compare_file2 = "source2.py"
    # comp1 = "JunseokSampleData/fizzbuzz1.py"
    # comp2 = "JunseokSampleData/fizzbuzz2.py"
    
    # for the multiple files
    path = 'Samples'
    files = []
    for file in os.listdir(path):
        if file.endswith('.py'):
            files.append(file)

    # need to get rid of the base filename from the list to prevent comparing duplicate
    base_file_name = random.choice(files)
    files.remove(base_file_name)
    
    programs = []
    for file in files:
        Mem_file = open(os.path.join("Samples", file))
        prog = Mem_file.read()
        Mem_file.close()
        programs.append(prog)
        
    base_file = []
    Mem_file = open(os.path.join("Samples", base_file_name))
    base = Mem_file.read()
    Mem_file.close()
    base_file.append(base)
        
    similarity1 = compare_multiple_files(base_file, programs)
    similarity2 = afc.compare_many(base_file, programs)
    
    # print('Base file is: ' + base_file_name)
    # print('Compare files: {}'.format(files))
        
    # for num in enumerate(similarity1):
    #     print('Method1 Similarity_{}: {:.2f}%'.format(num[0]+1, num[1]))
        
    # print('--------------------------------------------------')
    # for num in enumerate(similarity2):
    #     print('Method2 Similarity_{}: {:.2f}%'.format(num[0]+1, num[1]))
    
    show_plot(similarity1, similarity2, base_file_name)


if __name__ == "__main__":
    main()
