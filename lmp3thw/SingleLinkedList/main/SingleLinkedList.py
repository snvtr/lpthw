class SingleLinkedList():

    def __init__(self):
        """ class init """

        self.first = None
        self.last  = self.first

    def __str__(self):
        """ %s representation """

        ret_val = ''
        if self.first is not None:
            i = self.first
            while i.nxt is not None:
                ret_val += ''.join(['[', str(i.val), ', ', str(i.nxt.val), ']\n'])
                i = i.nxt
            ret_val += ''.join(['[', str(i.val), ', ', str(i.nxt), ']\n'])

        return ret_val

    def __repr__(self):
        """ %r representation """
        return self.__str__()
    
    def append(self, new_node):
        """ appends a node to the list """

        if self.first is None:
            self.first = new_node
            self.last  = self.first
        else:
            self.last.nxt = new_node
            self.last = new_node

        return self.last.val

    def pop(self):
        """ pops the last node from the list """
        pass

    def push(self, new_node):
        """ inserts a node in the beggining of the list """

        new_node.nxt = self.first
        self.first = new_node

        return self.first.val

    def shift(self):
        """ returns and deletes the first node of the list """

        if self.first is not None:
           val = self.first.val
           self.first = self.first.nxt
           return val
        else:
           return None

    def count(self):
        """ returns the node count """
        pass

    def delete(self, number):
        """ deletes node Number from the list """
        pass
          
    def first(self):
        """ returns the first node """
        pass

    def last(self):
        """ returns the last node """
        pass