from collections import deque
class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root == None:
        return "None"
    return "Node('" + root.val + "'," + serialize(root.left) + "," + serialize(root.right) + ")"
def deserialize(s):
    return eval(s)
# So, what if we can't use eval?
def serialize2(root):
    if root == None:
        return "None"
    return "Node '" + root.val + "' " + serialize2(root.left) + " " + serialize2(root.right)
def parse_string(c,d):
    if c[len(c)-1] == "'":
        final = c[1:len(c)-1]
        return final
    nc = d.popleft()
    if not nc[len(nc)-1] == "'":
        return parse_string(c + " " + nc,d)
    final = c + " " + nc
    final = final[1:len(final)-1]
    return final

def deserialize2(s):
    if not type(s) is deque:
        return deserialize2(deque(s.split(' ')))
    c = s.popleft()
    if c == "Node":
        val = s.popleft()
        val = parse_string(val,s)
        left = deserialize2(s)
        if left == "None":
            left = None
        right = deserialize2(s)
        if right == "None":
            right = None
        return Node(val,left,right)
    if c == "None":
        return None
    raise Exception("Syntax error, expected Node, got " + c)
node = Node('root',Node('left',Node('left.left')),Node('right'))
assert deserialize( serialize(node) ).left.left.val == 'left.left'
assert deserialize2( serialize2(node) ).left.left.val == 'left.left'

