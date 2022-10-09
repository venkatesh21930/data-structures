class Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def in_order_traversal(self):
        if self is None:
            return []
        return Tree.in_order_traversal(self.left)+[self.key]+Tree.in_order_traversal(self.right)
    def to_tuple(self):
        if self is None:
            return None
        elif self.left is None and self.right is None:
            return self.key
        return Tree.to_tuple(self.left),self.key,Tree.to_tuple(self.right)
    def size(self):
        if self is None:
            return 0
        return 1+Tree.size(self.left)+Tree.size(self.right)
    def height(self):
        if self is None:
            return 0
        return 1+max(Tree.height(self.left),Tree.height(self.right))
    def display(self,space='\t',level=0):
        if self is None:
            print(space*level+'$')
            return
        elif self.left is None and self.right is None:
            print(space*level+str(self.key))
            return
        Tree.display(self.right,space,level+1)
        print(space*level+str(self.key))
        Tree.display(self.left,space,level+1)
    def is_bst(self):
        if self is None:
            return True,None,None
        is_bst_l,min_l,max_l=Tree.is_bst(self.left)
        is_bst_r,min_r,max_r=Tree.is_bst(self.right)
        is_bst_node=(is_bst_l and is_bst_r and (max_l is None or max_l<self.key) and (min_r is None or min_r>self.key))
        min_key=min([x for x in [min_l,self.key,min_r] if x is not None])
        max_key=max([x for x in [max_l,self.key,max_r] if x is not None])
        return is_bst_node,min_key,max_key
    def __str__(self):
        return 'BinaryTree <{}>'.format(self.to_tuple())

    @staticmethod
    def create_tree_from_tuple(data):
        if isinstance(data,tuple) and len(data)==3:
            node=Tree(data[1])
            node.left=Tree.create_tree_from_tuple(data[0])
            node.right=Tree.create_tree_from_tuple(data[2])
        elif data is None:
            node=None
        else:
            node=Tree(data)
        return node
tree=Tree.create_tree_from_tuple(((1,2,3),4,(5,6,7)))
print(tree)

print(tree.is_bst())
