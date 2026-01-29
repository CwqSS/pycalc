from src.expression.ExpressionNode import ExpressionNode

class ExpressionTree:
    def __init__(self):
        self.root = None
    
    def generate_reverse_polish_notation(self, root):
        if root != None:
            root.display()
            self.post_inorder(root.left)
            self.post_inorder(root.right)

    def calculate(self):
        return self.root.calculate()
    
    def display(self):
        self.post_inorder(self.root)

    def display_reverse(self):
        self.generate_reverse_polish_notation(self.root)
    
    def post_inorder(self, root: ExpressionNode):
        if root != None:
            self.post_inorder(root.left)
            root.display()
            self.post_inorder(root.right)
