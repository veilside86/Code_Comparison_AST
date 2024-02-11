import ast
from _ast import *
from Levenshtein import ratio

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

# check the field of ast nodes
def field_check(tree: AST) -> list:
    subtree = []

    for node in ast.walk(tree):
        if(isinstance(node, Import) or isinstance(node, FunctionDef) or 
        isinstance(node, While) or isinstance(node, For) or 
        isinstance(node, comprehension) or isinstance(node, Return)):
            subtree.append(node)

    return subtree

# method: sort the tree then compare the string with edit distance
def calculate_similarity_percentage(tree_a: AST, tree_b: AST) -> float:
    score = 0
    node_a = ast.unparse(tree_a)
    node_b = ast.unparse(tree_b)

    score += ratio(node_a, node_b)
    
    return score

def main():
    """
    Set up the path of the two files to compare
    """
    # For the mac
    # compare_file1 = "/Users/trollcarrier/Desktop/GitHub/python-ast-comparison/structeq-subset-p1.py"
    # compare_file2 = "/Users/trollcarrier/Desktop/GitHub/python-ast-comparison/structeq-subset-p2.py"

    # for the Window
    compare_file1 = "source1.py"
    compare_file2 = "source2.py"

    with open(compare_file1, "r") as source:
        codes = source.read()
        # ast.parse give module object name
        tree1 = ast.parse(codes, mode="exec")
        
    with open(compare_file2, "r") as source:
        codes = source.read()
        tree2 = ast.parse(codes, mode="exec")

    tree1 = NormFunctions(func=None).visit(tree1)
    tree1 = NormIdentifiers().visit(tree1)
    tree2 = NormFunctions(func=None).visit(tree2)
    tree2 = NormIdentifiers().visit(tree2)

    # subtree1 = field_check(tree1)
    # subtree2 = field_check(tree2)

    similarity = calculate_similarity_percentage(tree1, tree2)

    print('Similarity: {:.2f}%'.format(similarity * 100))


if __name__ == "__main__":
    main()
