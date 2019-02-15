#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Tree(object):
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def addLeft(self, left):
        self.left = Tree(left)

    def addRight(self, right):
        self.right = Tree(right)

    def getNodeCount(self):
        count = 0
        if not self.left is None:
            count += 1
        if not self.right is None:
            count += 1
        return count

    def log(self):
        print('[', end='')
        print(self.data, end=', left = ')
        if self.left is None:
            print('None', end='')
        else:
            print(self.left.data, end='')
        print(' , right = ', end='')
        if self.right is None:
            print('None', end='')
        else:
            print(self.right.data, end='')
        print(']')

    def remove(self, node):
        print(self.left, self.right)
        if self.left == node:
            self.left = None
        elif self.right == node:
            self.right = None


# 插入操作
def addBranch(node, value):
    if node.data > value :
        if node.left is None:
            node.addLeft(value)
        else:
            addBranch(node.left, value)
    else:
        if node.right is None:
            node.addRight(value)
        else:
            addBranch(node.right, value)

# 打印树
def printTree(tree):
    if tree is None:
        return
    print(tree.data)
    nodeList = []
    if not tree.left is None:
        nodeList.append(tree.left)
    if not tree.right is None:
        nodeList.append(tree.right)
    printNodeList(nodeList)

def printNodeList(nodeList):
    newNodeList = []
    hasNode = False
    for node in nodeList:
        if node is None:
            print('x', end=' , ')
            # newNodeList.append(None)
            # newNodeList.append(None)
            continue
        print(node.data, end=' , ')
        if not node.left is None:
            newNodeList.append(node.left)
            hasNode = True
        else:
            newNodeList.append(None)
        if not node.right is None:
            newNodeList.append(node.right)
            hasNode = True
        else:
            newNodeList.append(None)
    print('')
    if hasNode:
        printNodeList(newNodeList)

# 查找操作
def findNumOnTree(tree, num):
    if tree is None:
        print(num, ', not find')
        return None
    if tree.data == num:
        print(num, ', get it')
        return tree
    if tree.data > num:
        return findNumOnTree(tree.left, num)
    else:
        return findNumOnTree(tree.right, num)

# 删除节点
def deleteNode(tree, num):
    delNode = tree
    parentNode = None
    while not delNode.data == num:
        parentNode = delNode
        if delNode.data > num:
            delNode = delNode.left
        else:
            delNode = delNode.right
    print(1)
    if delNode.getNodeCount() == 0:
        # delNode = None
        parentNode.remove(delNode)
    parentNode.log()


tree = Tree(33)
addBranch(tree, 17)
addBranch(tree, 50)
addBranch(tree, 13)
addBranch(tree, 18)
addBranch(tree, 34)
addBranch(tree, 58)
addBranch(tree, 16)
addBranch(tree, 25)
addBranch(tree, 51)
addBranch(tree, 66)
addBranch(tree, 19)
addBranch(tree, 27)

addBranch(tree, 55)

printTree(tree)

t = findNumOnTree(tree, 55)
# print(t)
deleteNode(tree, 55)
