#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tree(object):
    data = ''
    left = None
    right = None

    def __init__(self, data):
        self.data = data

# 前序遍历
def preOrder(tree):
    print(tree.data, end='')
    print('->', end='')
    if not tree.left is None:
        preOrder(tree.left)
    if not tree.right is None:
        preOrder(tree.right)

# 中序遍历
def inOrder(tree):
    if not tree.left is None:
        inOrder(tree.left)
    print(tree.data, end='')
    print('->', end='')
    if not tree.right is None:
        inOrder(tree.right)

# 后序遍历
def postOrder(tree):
    if not tree.left is None:
        postOrder(tree.left)
    if not tree.right is None:
        postOrder(tree.right)
    print(tree.data, end='')
    print('->', end='')

treeA = Tree('A')
treeB = Tree('B')
treeC = Tree('C')
treeD = Tree('D')
treeE = Tree('E')
treeF = Tree('F')
treeG = Tree('G')

treeA.left = treeB
treeA.right = treeC

treeB.left = treeD
treeB.right = treeE

treeC.left = treeF
treeC.right = treeG

preOrder(treeA)
print('')
inOrder(treeA)
print('')
postOrder(treeA)
print('')
