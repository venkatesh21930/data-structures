class BSTNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
        
    def insert(self,data):
        if self is None:
            self= BSTNode(data)
        elif data < self.key:
            self.left= BSTNode.insert(self.left,data)
            self.left.parent=self
        elif data > self.key:
            self.right= BSTNode.insert(self.right,data)
            self.right.parent=self
        return self
      
    def display(self,space='\t',level=0):
        if self is None:
            print(space*level+'$')
            return
        elif self.left is None and self.right is None:
            print(space*level+str(self.key))
            return
        BSTNode.display(self.right,space,level+1)
        print(space*level+str(self.key))
        BSTNode.display(self.left,space,level+1)
        
    def to_tuple(self):
        if self is None:
            return None
        elif self.left is None and self.right is None:
            return self.key
        return BSTNode.to_tuple(self.left),self.key,BSTNode.to_tuple(self.right)
      
    def find(self,data):
        if self is None:
            return None
        if self.key==data:
            return self
        elif self.key>data:
            return BSTNode.find(self.left,data)
        else:
            return BSTNode.find(self.right,data)
          
    def update(self,data,new_data):
        node=self.find(data)
        if node is not None:
            node.key=new_data
            
    def list_all(self):
        if self is None:
            return []
        return BSTNode.list_all(self.left)+[self.key]+BSTNode.list_all(self.right)
      
    def is_balanced(self):
        if self is None:
            return True,0
        bal_l,h_l=BSTNode.is_balanced(self.left)
        bal_r,h_r=BSTNode.is_balanced(self.right)
        bal=bal_l and bal_r and abs(h_l-h_r)<=1
        h=1+max(h_l,h_r)
        return bal,h
        
    def __str__(self):
        return 'BSTNOde <{}>'.format(self.to_tuple())
      
bst=BSTNode(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(11)
bst.insert(7)
bst.insert(17)
bst.display()
print(bst)
print(bst.list_all())
      
