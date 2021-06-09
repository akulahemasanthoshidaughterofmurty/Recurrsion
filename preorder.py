class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        list1=[]
        def pre(root,list1):
            if(root!=None):
                list1.append(root.val)
                pre(root.left,list1)
                pre(root.right,list1)
        
        pre(root,list1)
        return(list1)
