from Node import Node

class Linked:
    def __init__(self,limit):
        self.start_node = None
        self.limit= limit
        self.cont=0

    def traverse_list(self):
        if self.start_node is None:
            print('List has no element')
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def insert_at_end(self, data):
            new_node = Node(data)
            if self.start_node is None:
                self.cont+=1
                self.start_node = new_node
                return
            n = self.start_node
            while n.ref is not None:
                n= n.ref
            if self.limit == self.cont:
                self.delete_at_start()
            n.ref = new_node
            self.cont+=1
                     
            
    def insert_at_start(self, data):
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node= new_node

    def delete_at_start(self):
        if self.start_node is None:
            print('The list has no element to delete')
            return
        self.start_node = self.start_node.ref
        self.cont-=1

    def getItem(self):
        listResul=[]
        nodAux = self.start_node
        while nodAux != None:
            listResul.append(nodAux.item)
            nodAux=nodAux.ref
        return listResul
