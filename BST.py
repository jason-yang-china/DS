from typing import Optional

import random
import math
class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
#        self.height = 1

    def __str__(self):
        return 'node value:' + str(self.value)

class AVLTree:
    def __init__(self):
        self._root = None

    def find(self, value: int) -> Optional[TreeNode]:
        node = self._root
        while node and node.value != value:
            node = node.left if node.value > value else node.right
        return node

    def print_in_order(self):
        if (self == None):
            return
        node = self._root
        self.print_left(node.left)
        print(node.value)
        self.print_right(node.right)

    def search(self, value:int):
        if self._root == None:
            return

        node = self._root
        data = None
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                data = node.value
        return data


    def print_left(self, current):
        if (current == None):
            return
        print(current.value)
        self.print_left(current.left)
        if current.right != None:
            self.print_right(current.right)
        # print(node.value)

    def print_right(self, current):
        if (current == None):
            return
        print(current.value)
        self.print_right(current.right)
        if current.left !=None:
            self.print_left(current.left)

    def print_rootnode(self):
        if (self._root == None):
            return
        return self._root.value

    def minValue(self):
        if (self == None):
            return
        current = self._root

        while (current.left != None):
            current = current.left
        return current.value

    def height(self, bst):
        if (bst == None):
            return 0

        return max(self.height(bst.left), self.height(bst.right)) + 1

    def insert(self, value: int):
        if not self._root:
            self._root = TreeNode(value)
            return

        parent = None
        node = self._root
        while node:
            parent = node
            if node.value > value:
                node = node.left
            else:
                node = node.right
        new_node = TreeNode(value)
        new_node.parent = parent

        if parent.value > value:
            parent.left = new_node
        else:
            parent.right = new_node
        isBalance = self.isBalanced(self._root)

        if not isBalance:
            # left height - right height > 1
            if new_node.value > new_node.parent.value:
                self.totalRotate(new_node)
            else:
                self.rightRotate(new_node)

    # case 3 A<B<C
    def leftRotate(self, node):
        C = node.parent.parent.value
        node.parent.parent.value = node.parent.value
        node.parent.value = node.value
        node.parent.parent.left = TreeNode(C)
        node.parent.parent.left.parent = node.parent.parent
        node.parent.right = None


    # case 1 A>B<C and root node is A
    def totalRotate(self, node):
        if self._root == node.parent.parent:
            node.right = node.parent.parent
            node.left = node.parent
            node.left.parent = node
            node.left.right = None
            node.right.parent = node
            node.right.left = None
            node.parent = None
            self._root = node
        else:
            self.leftRotate(node)


            # case 2 A>B>C and root node is A
    def rightRotate(self, node):
        # just modify the value of the parent A to middle one
        if self._root == node.parent.parent:
            self._root = node.parent
        else:
            A = node.parent.parent.value
            node.parent.parent.value = node.parent.value
            node.parent.value = node.value
            node.parent.parent.right = TreeNode(A)
            node.parent.parent.right.parent = node.parent.parent
            node.parent.left = None
            #node = None

    def isBalanced(self, root):
        if not root:
            return True

        lh = self.height(root.left)
        rh = self.height(root.right)

        if (abs(lh-rh) <= 1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True:
            return True

        return False



    def delete(self, node):
        if self._root == None:
            return

        node = self.find(node.value)
        if node is not None:
            # it does not have either left child or right child
            if node.left is None and node.right is None:
                if node == self._root:
                    self._root = None
                else:
                    if node.value < node.parent.value:
                        node.parent.left = None
                    else:
                        node.parent.right = None

            # it does not have left child but it does have right child
            elif node.left is None and node.right is not None:
                if node == self._root:
                    self._root = node.right
                    self._root.parent = None
                    node.right = None
                else:
                    if node.value < node.parent.value:
                        node.parent.left = node.right
                    else:
                        node.parent.right = node.right

                    node.right.parent = node.parent
                    node.parent = None
                    node.right = None
            # it does have left child but it does not have right child
            elif node.left is not None and node.right is None:
                if node == self._root:
                    self._root = node.left
                    self._root.parent = None
                    node.left = None
                else:
                    if node.value < node.parent.value:
                        node.parent.left = node.left
                    else:
                        node.parent.right = node.left

                    node.left.parent = node.parent
                    node.parent = None
                    node.left = None
             # it does have either left child and right child
            else:
                min_code = node.right
                if min_code.left:
                    min_code = min_code.left

                if node.value != min_code.value:
                    node.value = min_code.value
                    self.delete(min_code)


btree = AVLTree()
#treeList = [65, 45, 36, 47, 80, 9, 85, 101, 54, 31]
#treeList = [195, 35, 85, 173, 8, 123, 36, 33, 54, 172, 99, 71, 134, 197, 147, 142, 68, 116, 187, 198]
#treeList = [195, 35, 85, 173, 8, 123, 36, 33, 54, 172, 99, 71]
#treeList = [195, 35, 85, 173, 8, 123]
treeList = [195, 35, 85, 173, 8, 123, 36, 33, 54, 172, 99, 71]

#[169, 168, 133, 31, 29, 190, 93, 23, 166, 181, 24, 82, 175, 66, 164, 3, 8, 98, 183, 41]
#treeList = random.sample(range(1, 200), 20)

print(treeList)
for item in treeList:
    btree.insert(item)

height = btree.height(btree._root)
print('height is '+str(height))
isBalance = btree.isBalanced(btree._root)
print(isBalance)
btree.print_in_order()
#btree.delete(TreeNode(85))
#btree.print_in_order()