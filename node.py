newest_node=None
active_nodes=[]

class node:
    def __init__(self):
        self.on=False
  #      self.color = "green"
    
 #   def get_color(self):
 #       return color  

    def is_on(self):
        return self.on
    
    def is_off(self):
        return self.off

    def activate(self):
        self.on=True
 #       self.color = color
        return self.on

    
 