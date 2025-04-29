import sys 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 
        self.balance = None


def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.right) - getHeight(node.left) # orden de resta corregido

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)
        node.balance = balance

        #if balance > 1 and getBalance(node.left) >= 0:
            #rotate_right(node) 
        #elif balance > 1 and getBalance(node.left) < 0:
            #node.left = rotate_left(node.left)
            #rotate_right(node) 
        if balance > 1 and getBalance(node.right) > 0:
            rotate_left(node)
        #elif balance < -1 and getBalance(node.right) > 0:
            #node.right = rotate_right(node.right)
            #rotate_left(node) 
        
        return node 
    

def level_order_rec(root, level, res):
    if root is None:
        return
    
    if len(res) <= level:
        res.append([])
        
    res[level].append((root.value, root.height, root.balance))

    level_order_rec(root.left, level + 1, res)
    level_order_rec(root.right, level + 1, res)
    
def level_order(root):
    res = []
    level_order_rec(root, 0, res)
    return res


avl = AVLTree()
values_to_insert = [10, 9, 30, 40, 50, 25]


print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

res = level_order(avl.root)
for level in res:
    print(f'[{", ".join(map(str, level))}] ', end='')

print("\n--- Después de inserciones ---")

