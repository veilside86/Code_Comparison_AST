import ast
from _ast import *

class analyzeNode(ast.NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

# ast.unparse can cause RecursionError in highly complex expression
class wavied(analyzeNode):
    def classname(self, cls):
        return cls.__class__.__name__
    
    def visit_Load(self, node):
        pass

    def visit_Constant(self, node):
        pass

    def visit_Call(self, node):
        pass

    def visit_Assign(self, node):
        print(self.classname(node), node.targets[0].id, ast.unparse(node.value))

    def visit_Import(self, node):
        print(self.classname(node), ast.unparse(node.names), ast.unparse(node.names))

    def visit_Name(self, node):
        print(self.classname(node), node.id)

    def visit_FunctionDef(self, node):
        print(self.classname(node), ast.unparse(node.args), 
              ast.unparse(node.body), ast.unparse(node.decorator_list))
    
    def visit_Return(self, node):
        print(self.classname(node))

    def visit_For(self, node):
        print(self.classname(node), '\n',
              ast.unparse(node.body))
        
    def visit_While(self, node):
        print(self.classname(node), '\n',
              ast.unparse(node.body))

    def visit_If(self, node):
        print(self.classname(node), '\n', 
              ast.unparse(node.body), '\n',
              ast.unparse(node.orelse))


def compare_nodes(ast_a: AST, ast_b: AST, num: int) -> int:
    children_a = list(ast.iter_child_nodes(ast_a))
    children_b = list(ast.iter_child_nodes(ast_b))

    print(children_a, children_b)

    if ((type(ast_a) == type(ast_b))
            and len(list(children_a)) == 0
            and len(list(children_b)) == 0):
        return 1

    if ((type(ast_a) != type(ast_b))
            or (len(children_a) != len(children_b))):
        return 0
    
    for x in children_a:
        for y in children_b:
            if (x==y):
                num += 1
    
    return num
    
def compare_subtrees(parentA: list, parentB: list) -> tuple:
    best_match = []
    cnt = 0
    children_a = parentA.copy()
    children_b = parentB.copy()

    # if len(children_a) <= 1 or len(children_b) <= 1:
    for child_a in children_a:
        best_match += [child_a]
        for child_b in children_b:
            cnt += compare_nodes(child_a, child_b, cnt)
            best_match += [child_b]
    
    return cnt
    
def count_nodes(tree):
    return 1 + sum(count_nodes(child) for child in ast.iter_child_nodes(tree))

def compare_trees(tree1, tree2):
    children_a = list(ast.iter_child_nodes(tree1))
    children_b = list(ast.iter_child_nodes(tree2))
    # If the types of the nodes are different, the trees are not identical
    if type(tree1) != type(tree2):
        return 0
    
    if ((type(tree1) == type(tree2))
            and len(list(children_a)) == 0
            and len(list(children_b)) == 0):
        return 1

    # If the nodes have different numbers of children, the trees are not identical
    if len(children_a) != len(children_b):
        return 0

    # Compare each pair of children
    ##### Does order matter #####
    score = 1  # Count the current node
    for child1 in children_a:
        for child2 in children_b:
            score += compare_trees(child1, child2)
    # for child1, child2 in zip(ast.iter_child_nodes(tree1), ast.iter_child_nodes(tree2)):
    #     score += compare_trees(child1, child2)

    return score

def calculate_similarity_percentage(tree1, tree2):
    print(count_nodes(tree1))
    total_nodes = count_nodes(tree1)
    print('Total nodes:', total_nodes)
    
    matching_nodes = compare_trees(tree1, tree2)
    print('Matching nodes:', matching_nodes)

    similarity_percentage = (matching_nodes / total_nodes) * 100

    return similarity_percentage

def main():
    """
    Set up the path of the two files to compare
    """
    # For the mac
    # compare_file1 = "/Users/trollcarrier/Desktop/GitHub/python-ast-comparison/structeq-subset-p1.py"
    # compare_file2 = "/Users/trollcarrier/Desktop/GitHub/python-ast-comparison/structeq-subset-p2.py"

    # for the
    compare_file1 = "structeq-subset-p1.py"
    compare_file2 = "structeq-subset-p2.py"
    # compare_file2 = "x1.py"


    with open(compare_file1, "r") as source:
        codes = source.read()
        # ast.parse give module object name
        tree1 = ast.parse(codes, mode="exec")
        
    with open(compare_file2, "r") as source:
        codes = source.read()
        tree2 = ast.parse(codes, mode="exec")

    subtree1 = []
    subtree2 = []
    # subtree3 = []

    for node in ast.walk(tree1):
        if(isinstance(node, Import) or isinstance(node, FunctionDef) or 
           isinstance(node, While) or isinstance(node, For) or 
           isinstance(node, comprehension) or isinstance(node, Return)):
            subtree1.append(node)

    for node in ast.walk(tree2):
        if(isinstance(node, Import) or isinstance(node, FunctionDef) or 
           isinstance(node, While) or isinstance(node, For) or 
           isinstance(node, comprehension) or isinstance(node, Return)):
            subtree2.append(node)

    print('{:.2f}%'.format(calculate_similarity_percentage(tree1, tree2)))

    # for node in ast.walk(tree1):
    #     for i in range(len(tree1._fields)):
    #         if(isinstance(node, ast.AST._fields[i])):
    #             subtree3.append(node._fields)

    # print(subtree3)

    # if(isinstance(id, ast.iter_child_nodes(tree1))):
    #     for item in ast.iter_child_nodes(tree1):
    #          print(item)

    # imp = {
    #     node._fields[0]: node.names[0].name
    #     for node in ast.walk(tree1)
    #     if isinstance(node, Import)
    # }
    # fundef = {
    #     node._fields[0]: node.body[0]
    #     for node in ast.walk(tree1)
    #     if isinstance(node, FunctionDef)
    # }

    # print(imp, fundef)

    # print(compare_subtrees(subtree1, subtree2))
    # w = wavied()
    # print(f"---{compare_file1}---\n", w.visit(tree1))
    # print(f"---{compare_file2}---\n", w.visit(tree2))
    # ast_visit(tree1)

# def str_node(node):
#     if isinstance(node, ast.AST):
#         fields = [(name, str_node(val)) for name, val in ast.iter_fields(node) if name not in ('left', 'right')]
#         rv = '%s(%s' % (node.__class__.__name__, ', '.join('%s=%s' % field for field in fields))
#         return rv + ')'
#     else:
#         return repr(node)
    
# def ast_visit(node, level=0):
#     print('  ' * level + str_node(node))
#     for field, value in ast.iter_fields(node):
#         if isinstance(value, list):
#             for item in value:
#                 if isinstance(item, ast.AST):
#                     ast_visit(item, level=level+1)
#         elif isinstance(value, ast.AST):
#             ast_visit(value, level=level+1)


if __name__ == "__main__":
    main()
