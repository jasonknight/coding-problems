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
# This is the simple solution, using Python itself as the deserializer
node = Node('root',Node('left',Node('left.left')),Node('right'))
assert deserialize( serialize(node) ).left.left.val == 'left.left'
# So, what if we can't use eval?
# Well, we'll need to create a recursive descent parser.
# That's just a fancy way of saying a token stream (in this case a deque)
# where we pop tokens (one or more) that are semantically relavent.
# We won't make it too fancy, but obviously we could create classes,
# and functions for specific "productions". In our case, we really only
# have 3 productions, Node, None and String. 
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
        # In our little serialization language, a 
        # string can only appear right after a Node
        val = parse_string(val,s)
        # Left and Right can only be Node, or None
        left = deserialize2(s)
        right = deserialize2(s)
        return Node(val,left,right)
    # We handle the None case
    if c == "None":
        return None
    raise Exception("Syntax error, expected Node, got " + c)
assert deserialize2( serialize2(node) ).left.left.val == 'left.left'
# let's see if we handle string parsing
node2 = Node('root',Node('left',Node('left left')),Node('right'))
assert deserialize2( serialize2(node2) ).left.left.val == 'left left'

