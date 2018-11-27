class Node:
    def __init__(self,val,left=False,right=False):
        self.val = val
        self.left = left
        self.right = right
    
def count_unival(root):
    cnt = 0 # global variable
    def count(rt):
        nonlocal cnt
        if not rt:
            return True
        l = count(rt.left)
        r = count(rt.right)
        if l and r:
            rl = rt.left
            rr = rt.right
            if not rl and not rr:
                cnt = cnt + 1
                return True
            elif rl and rr and rr.val == rt.val and rl.val == rt.val:
                cnt = cnt + 1
                return True
            elif rl and rl.val == rt.val:
                cnt = cnt + 1
                return True
            elif rr and rr.val == rt.val:
                cnt = cnt + 1
                return True
        return False
    count(root)
    return cnt

        
root = Node(0,Node(1),Node(0,Node(1, Node(1),Node(1)),Node(0)))
print(count_unival(root))

