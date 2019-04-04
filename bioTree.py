# -*- coding: utf-8 -*-

'''
二叉树：

1. 前序遍历

2. 中序遍历

3. 后序遍历

4. 层次遍历

5. 计算树的高度

6. 删除二叉树
'''



class treeNode(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self):
        self.root = self.initBiotree()

    def initBiotree(self):
        '''
        初始化一颗二叉树：
            A
           / \
          B    C
         / \   /
        D   E  F
        '''
        G = treeNode('G')

        D = treeNode('D')
        E = treeNode('E',G, None)
        F = treeNode('F')

        B = treeNode('B', D, E)
        C = treeNode('C', F, None)

        A = treeNode('A', B, C)
        return A

    def preTraverse(self, root):
        '''
        前序遍历（先序遍历）
        :param root: 根节点
        :return:
        '''
        if root == None:
            return

        print(root.value, end='')
        self.preTraverse(root.left)
        self.preTraverse(root.right)

    def preTraverse2(self, root):
        '''
        前序遍历非递归方式
        :param root:
        :return:
        '''
        if root == None:
            return
        rootStack = []
        p = root
        while p != None or len(rootStack) != 0:
            if p != None:
                print(p.value, end='')
                rootStack.append(p)
                p = p.left
            else:
                if len(rootStack) != 0:
                    p = rootStack.pop(-1)
                    p = p.right

    def preTraverse3(self, root):
        '''
        前序遍历非递归方式
        :param root:
        :return:
        '''
        if root == None:
            return

        rootStack = [root.right, root.left, root.value]

        while len(rootStack) != 0:
            temp = rootStack.pop(-1)
            if isinstance(temp, treeNode):
                rootStack.append(temp.right)
                rootStack.append(temp.left)
                rootStack.append(temp.value)
            else:
                if temp != None:
                    print(temp, end='')


    def midTraverse(self, root):
        '''
        中序遍历
        :param root: 根节点
        :return:
        '''
        if root == None:
            return

        self.midTraverse(root.left)
        print(root.value, end='')
        self.midTraverse(root.right)


    def midTraverse2(self, root):
        '''
        中序遍历非递归方法
        :param root: 根节点
        :return:
        '''
        if root == None:
            return

        rootStack = []
        p = root

        while p != None or len(rootStack) != 0:
            # 先找到最左叶子节点
            while p != None:
                rootStack.append(p)
                p = p.left
            if len(rootStack) != 0:
                p = rootStack.pop(-1)
                print(p.value, end='')
                p = p.right

    def midTraverse3(self, root):
        '''
        中序遍历非递归方法
        :param root: 根节点
        :return:
        '''
        if root == None:
            return

        rootStack = [root.right, root.value, root.left]

        while len(rootStack) != 0:
            temp = rootStack.pop(-1)
            if isinstance(temp, treeNode):
                rootStack.append(temp.right)
                rootStack.append(temp.value)
                rootStack.append(temp.left)
            else:
                if temp != None:
                    print(temp, end='')

    def afterTraverse(self, root):
        '''
        后序遍历
        :param root: 根节点
        :return:
        '''
        if root == None:
            return

        self.afterTraverse(root.left)
        self.afterTraverse(root.right)
        print(root.value, end='')


    def afterTraverse2(self, root):
        '''
        后序遍历非递归方法
        :param root: 根节点
        :return:
        '''
        if root == None:
            return

        rootStack = [root.value, root.right, root.left]
        while len(rootStack) != 0:
            temp = rootStack.pop(-1)
            if isinstance(temp, treeNode):
                rootStack.append(temp.value)
                rootStack.append(temp.right)
                rootStack.append(temp.left)
            else:
                if temp != None:
                    print(temp, end='')

    def layer_Order_Up2Down_L2R_Traverse(self, root):
        '''
        层次遍历,【从上到下】，左到右 --- 队列Queue
        :param root:
        :return:
        '''
        if root == None:
            return
        rootQueue = [root]
        while len(rootQueue) != 0:
            temp = rootQueue.pop(0)
            if isinstance(temp, treeNode):
                print(temp.value, end='')
                rootQueue.append(temp.left)
                rootQueue.append(temp.right)
            else:
                pass

    def layer_Order_Down2Up_L2R_Traverse(self, root):
        '''
        层次遍历,【从下到上】，从左到右 --- 堆栈Stack
        :param root:
        :return:
        '''
        if root == None:
            return
        rootStack = [root]
        tempQueue = [root]

        while len(tempQueue) != 0:
            temp = tempQueue.pop(0)
            if isinstance(temp, treeNode):
                # 存入堆栈中
                rootStack.append(temp.right)
                rootStack.append(temp.left)
                # 存入临时队列中
                tempQueue.append(temp.right)
                tempQueue.append(temp.left)
            else:
                pass

        while len(rootStack) != 0:
            # 出栈
            temp = rootStack.pop(-1)
            if isinstance(temp, treeNode):
                print(temp.value, end='')

    def biotreeHeight(self, root):
        '''
        求二叉树的高度
        :param root:
        :return:
        '''
        if root == None:
            return 0
        high_L = self.biotreeHeight(root.left)
        high_R = self.biotreeHeight(root.right)
        if high_L > high_R:
            print(root.value)
            high_L += 1
            return high_L
        else:
            print(root.value)
            high_R += 1
            return high_R


    def biotreeHeight1(self, root):
        '''
        求二叉树的高度
        :param root:
        :return:
        '''
        if root == None:
            return 0
        l = self.biotreeHeight1(root.left)
        r = self.biotreeHeight1(root.right)

        return max(r, l) + 1

    def deleteTreenode(self, root, value):
        '''
        删除二叉树中值为value的节点：
        找到该节点的父节点，将其对应的子树设置为None
        :param root:
        :return:
        '''
        pass


    def levelOrderBottom(self, root):
        if root == None:
            return

        rootQueue = [root]
        res = []

        while len(rootQueue) != 0:
            val = []
            temp = rootQueue
            rootQueue = []
            for i in temp:
                if isinstance(i, treeNode):
                    val.append(i.value)
                    rootQueue.append(i.left)
                    rootQueue.append(i.right)
            if len(val) != 0:
                res.append(val)

        return res[::-1]


if __name__ == '__main__':
    t = Tree()

    print(t.biotreeHeight1(t.root))





