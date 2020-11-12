"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # go left
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
                return
            self.left.insert(value)
        # go right
        else:
            if self.right is None:
                self.right = BSTNode(value)
                return
            self.right.insert(value)

        # ITERATIVE
        # temp = self
        # while True:
        #     if value < temp.value:  # go left
        #         if temp.left is None:
        #             temp.left = BSTNode(value)
        #             break
        #         temp = temp.left
        #     else:  # go right
        #         if temp.right is None:
        #             temp.right = BSTNode(value)
        #             break
        #         temp = temp.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case
        if target == self.value:
            return True
        # go left
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        # go right
        else:
            if self.right:
                return self.right.contains(target)
        # target not found
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        if self.right is None:
            return self.value
        # the work
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # apply the fn
        fn(self.value)
        # go left
        self.left and self.left.for_each(fn)
        # go right
        self.right and self.right.for_each(fn)

    #
    # Part 2 -------------------------
    #

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    #
    # Stretch Goals -------------------------
    # Note: Research may be required
    #

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()

# print("in order")
# bst.in_order_dft()

# print("post order")
# bst.post_order_dft()
