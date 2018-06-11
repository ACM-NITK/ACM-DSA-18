

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Bstconverter:
	def sortedArrayToBST(self, nums):
		if len(nums) == 0:
			return None
		centerIndex = len(nums)//2
		center = TreeNode(nums[centerIndex])
		center.left = self.sortedArrayToBST(nums[:centerIndex])
		center.right = self.sortedArrayToBST(nums[centerIndex+1:])
		return center

temp = Bstconverter()
res = temp.sortedArrayToBST([1,2,3,4,5,6,7,8,9,10])
def preOrder_transversal(node):
        if node is None:
            return
        print("-->",node.val,end='')
        preOrder_transversal(node.left)
        preOrder_transversal(node.right)
preOrder_transversal(res)
