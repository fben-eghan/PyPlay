class TreeNode:
    """
    A node in a binary search tree.

    Attributes:
        val (int): The value of the node.
        left (TreeNode): The left child node.
        right (TreeNode): The right child node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_search_tree(nums, left, right):
    """
    Recursively constructs a binary search tree from a sorted list of integers.

    Args:
        nums (List[int]): The sorted list of integers.
        left (int): The left index of the range to include in the binary search tree.
        right (int): The right index of the range to include in the binary search tree.

    Returns:
        TreeNode: The root node of the constructed binary search tree.
    """
    if left > right:
        return None
    mid = (left + right) // 2
    root = TreeNode(nums[mid])
    root.left = binary_search_tree(nums, left, mid-1)
    root.right = binary_search_tree(nums, mid+1, right)
    return root

def binary_search(root, target):
    """
    Recursively searches for a value in a binary search tree.

    Args:
        root (TreeNode): The root node of the binary search tree.
        target (int): The value to search for.

    Returns:
        TreeNode: The node containing the target value if it is found, None otherwise.
    """
    if not root:
        return None
    if root.val == target:
        return root
    if root.val > target:
        return binary_search(root.left, target)
    else:
        return binary_search(root.right, target)
