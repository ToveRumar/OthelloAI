newest_node=None
active_nodes=[]

class node:
    def __init__(self):
        self.on=False
        
    def is_on(self):
        return self.on

    def activate(self):
        self.on=True
        return self.on

    
 