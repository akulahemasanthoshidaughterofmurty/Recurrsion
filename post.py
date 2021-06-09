class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        list1=[]
        def post(root,list1):
            if(root!=None):
                post(root.left,list1)
                post(root.right,list1)
                list1.append(root.val)
        post(root,list1)
        return(list1)
