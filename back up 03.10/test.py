from _ast import Import
import ast
from _ast import *
from Levenshtein import ratio
import re

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
    def __init__(self, func=None, imp=None):
        self.identifiers = {}
        self.func = func
        self.imp = imp
        super().__init__()

    # def visit_Import(self, node):
    #     if self.imp and self.imp != node.names:
    #         return None
        
    #     try:
    #         names = self.identifiers[node.names]
    #     except KeyError:
    #         names = f'import{len(self.identifiers):x}'
    #         self.identifiers[node.names] = names
            
    #     return ast.copy_location(self.imp, node)

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

# check the field of ast nodes
def field_check(tree: AST) -> list:
    subtree = []
    checking = ['names', 'body', 'value', 'orelse']

    for node in ast.walk(tree):
        if(isinstance(node, Import) or isinstance(node, FunctionDef) or 
        isinstance(node, While) or isinstance(node, For) or 
        isinstance(node, comprehension) or isinstance(node, Return)):
        
            subtree.append(node)

    return subtree

def count_nodes(tree: AST):
    return len(list(ast.walk(tree)))

# method: sort the tree then compare the string with edit distance
def compare_ast(tree1: AST, tree2: AST):
    children_a = list(ast.iter_child_nodes(tree1))
    children_b = list(ast.iter_child_nodes(tree2))
    average = 0

    # If the types of the nodes are different, the trees are not identical
    # If the nodes have different numbers of children, the trees are not identical
    if (type(tree1) != type(tree2)
            or len(children_a) != len(children_b)):
        return 0
    
    if ((type(tree1) == type(tree2))
            and len(list(children_a)) == 0
            and len(list(children_b)) == 0):
        return 1

    # Compare each pair of children
    # for child1 in children_a:
    #     for child2 in children_b:
    #         if (child1 == child2):
    average += ratio(children_a, children_b)
            # score += ratio(child1, child2)
    # for child1, child2 in zip(ast.iter_child_nodes(tree1), ast.iter_child_nodes(tree2)):
    #     score += compare_trees(child1, child2)

    return average

def compare_subtree(subtree_list1: list, subtree_list2: list):
    score = 0
    node_a = ast.unparse(subtree_list1)
    node_b = ast.unparse(subtree_list2)

    score += ratio(node_a, node_b)

    # for subnode_a in node_a:
    #     for subnode_b in node_b:
    #         score += compare_ast(subnode_a, subnode_b)

    return score

def calculate_similarity_percentage(tree_a: Dict, tree_b: Dict) -> float:
    # total_nodes = count_nodes(tree_a) + count_nodes(tree_b)
    # print('Total nodes:', total_nodes)
    print(tree_a)
    subtree_a = list(tree_a[0].values())
    subtree_b = list(tree_b[0].values())
    
    return compare_subtree(subtree_a, subtree_b)

def nomarlized_file(filename):
    fn = filename

    with open(fn, "r") as source:
        codes = source.read()
        tree = ast.parse(codes, mode="exec")

    tree = NormFunctions(func=None).visit(tree)
    tree = NormIdentifiers().visit(tree)

    tree = field_check(tree)

    return tree

def main():
    """
    Set up the path of the two files to compare
    """
    # For the mac
    # compare_file1 = "/Users/trollcarrier/Desktop/GitHub/python-ast-comparison/structeq-subset-p1.py"
    # compare_file2 = "/Users/trollcarrier/Desktop/GitHub/python-ast-comparison/structeq-subset-p2.py"

    # for the Window
    compare_files = ["source1.py", "source2.py"]
    subtree = {}

    for num in range(len(compare_files)):
        for file in compare_files:
            subtree["subtree{0}".format(num+1)] = nomarlized_file(file)

    for subtree1 in subtree.items():
        for subtree2 in subtree.items():
            similarity = calculate_similarity_percentage(subtree1, subtree2)

    print('Similarity: {:.2f}%'.format(similarity * 100))


if __name__ == "__main__":
    main()
