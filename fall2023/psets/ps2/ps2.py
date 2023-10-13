class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree (a key so that ind keys are smaller)
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            # return self.right.select(ind)
            return self.right.select(ind - left_size - 1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one

    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
            # If we add the node here, there is no point in going through the rest 
            # of the code. 
            return self
        elif self.key > key: 
            if self.left is None:
                # Create new node
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                # Create new node
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        
        self.size += 1
        # We are currently recalculating size for ALL nodes below the one called, when we should just 
        # be recalculating ones along the path we iterate (and each of these only increase by 1).
        # self.calculate_sizes()
        return self
        # return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        
        if child_side == "R" and self.right is not None:
            root = self.right
        elif child_side == "L" and self.left is not None:
            root = self.left
        else:
            return self
        
        if direction == "R":
            ysize = root.size
            x = root.left
            # C
            T2 = x.right

            # set x's right child to y, y's left child to x's right child B
            x.right = root
            root.left = T2

            x.size = ysize
            # set y's size to B + C + 1
            leftsize = root.left.size if root.left else 0
            rightsize = root.right.size if root.right else 0

            root.size = leftsize + rightsize + 1

            if child_side == "L":
                self.left = x
            else:
                self.right = x

            # Calculate sizes from new root
            # root.calculate_sizes()

        elif direction == "L":
            xsize = root.size
            y = root.right
            T2 = y.left

            y.left = root
            root.right = T2
            
            y.size = xsize
            # set x's size to B + C + 1
            leftsize = root.left.size if root.left else 0
            rightsize = root.right.size if root.right else 0

            root.size = leftsize + rightsize + 1

            if child_side == "L":
                self.left = y
            else:
                self.right = y
            
            
            # Calculate sizes from new root
            # root.calculate_sizes()
        
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self