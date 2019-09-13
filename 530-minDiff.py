# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    diff = []

    def addItem(self, val, root:TreeNode):
        if(root is None):
            return TreeNode(val)
        
        if(val > root.val):
            root.right = self.addItem(val, root.right)
        else:
            root.left = self.addItem(val, root.left)

        return root
        

    def inOrderTraversal(self, root:TreeNode, arr, minDiff) -> None:
        if(root):
            self.inOrderTraversal(root.left, arr, minDiff)
            arr.append(root.val)
            print(arr)
            if(len(arr)>1):
                minDiff.append(abs(arr[-1] - arr[-2]))
            print(minDiff)
            self.inOrderTraversal(root.right, arr, minDiff)

    def getMinimumDifference(self, root: TreeNode) -> int:
        minDiff = []

        self.inOrderTraversal(root, [], minDiff)

        return min(minDiff)


solution = Solution()
root = TreeNode(543)
root = solution.addItem(384, root)
root = solution.addItem(652, root)
root = solution.addItem(445, root)
root = solution.addItem(699, root)

print(solution.getMinimumDifference(root))


        