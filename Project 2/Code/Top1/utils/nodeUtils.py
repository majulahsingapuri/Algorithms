# Node
class SNode(): # Simple node with one data field and one pointer
    def __init__(self, id, connectedNodes = [], checkNode = True): 
        self.id = id
        self.connectedNodes = connectedNodes
        self.checkNode = checkNode
        self.breadCrumb = None
        self.distance = None
