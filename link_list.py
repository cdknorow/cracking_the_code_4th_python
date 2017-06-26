class LinkNode:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def append_at_tail(self, value):
        n = self
        while n._next is not None:
            n = n._next
        
        n._next = LinkNode(value)

    ## Note: the following functions don't need to be part of the class, just here for convinence
    def delete_at_index(self, index):
        n = self
        for i in range(index-1):
            if n._next is None:
                print "index is out of range."
                return None
            n = n._next

        n._next = n._next._next

    ## Note: the following functions don't need to be part of the class, just here for convinence
    def get_value_at_index(self, index):
        n = self
        for i in range(index):
            if n._next is None:
                print "index is out of range."
                return None
            n = n._next

        return n._value

    def print_values(self):
        n = self
        print n._value
        while n._next is not None:
            n = n._next
            print n._value

    def return_values_as_list(self):
        M = []
        n = self
        M.append(n._value)
        while n._next is not None:
            n = n._next
            M.append(n._value)

        return M

def build_linked_list(node, M):
    n = node(M[0])
    for i in M[1:]:
        n.append_at_tail(i)
    return n