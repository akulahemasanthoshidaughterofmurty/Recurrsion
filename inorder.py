class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list1=[]
        def inorder(root,list1):
            if(root!=None):
                inorder(root.left,list1)
                list1.append(root.val)
                inorder(root.right,list1)
        inorder(root,list1)
        return(list1)
