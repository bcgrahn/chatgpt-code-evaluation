

# This code example uses a recursive function to traverse a tree structure
# and a helper function to find the maximum value in the tree

def traverse_tree(tree, max_val):
    if tree is None:
        return max_val
    max_val = max(max_val, tree.val)
    max_val = traverse_tree(tree.left, max_val)
    max_val = traverse_tree(tree.right, max_val)
    return max_val

def find_max_val(tree):
    max_val = -float('inf')
    return traverse_tree(tree, max_val)