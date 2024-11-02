class Node: 
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    #Métodos de BST

    ###### Inserir um nó ######
    def insert(self,value):
        if self.root is None:
            self.root = None(value)
        else: 
            self._insert_recursive(self.root,value)

    def _insert_recursive(self, current_node,value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left,value)
        else: 
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right,value)

    ###### Buscar por um nó ######
    def search (self, value):
      return self._search_recursive(self.root,value)

    def _search_recursive(self, current_node, value):
      if current_node is None:
          return False
      elif current_node.value == value: 
          return True
      elif current_node.value > value: 
          return self._search_recursive(current_node.left,value)
      else:
          return self._search_recursive(current_node.right,value)

    ###### Remoção de um Nó ######
    def delete (self, value):
      self.root = self._delete_recursive(self.root.value)

    def _delete_recursive(self, current_node, value): 
      if current_node is None: 
        return current_node
      if value < current_node.value: 
        current_node.left = self._delete_recursive(current_node.left,value)
      elif value > current_node.value: 
        current_node.right = self._delete_recursive(current_node.right,value)
      else: 
        #Caso 1: Nó sem filhos
        if current_node.left is None and current_node.right is None: 
          return None
        #Caso 2:Nó com um filho
        elif current_node.left is None: 
          return current_node.right
        elif current_node.right is None:
          return current_node.left
        #Caso 3: Nó com dois filhos
        else: 
          successor_value = self.find_min(current_node.right)
          current_node.value = successor_value  
          current_node.right = self._delete_recursive(current_node.right, successor_value)
      return current_node
    
    def _find_min(self,node):
      while node.left is not None:
        node = node.left
      return node.value
    
    ###### Percorrer a BST ######
    #In-order
    def in_order_traversal(self):
      result = []
      self._in_order_recursive(self.root,result)
      return result

    def _in_order_recursive(self, current, result): 
      if current: 
         self._in_order_recursive(current.left,result)
         result.append(current.value)
         self._in_order_recursive(current.right,result)
    
    #Pre-order
    def pre_order_traversal(self):
      result = []
      self._pre_order_recursive(self.root,result)
      return result

    def _pre_order_recursive(self, current, result): 
      if current: 
        result.append(current.value)
        self._pre_order_recursive(current.left,result)
        self._pre_order_recursive(current.right,result)
    
    #Pos-Order
    def pos_order_traversal(self):
      result = []
      self._pos_order_recursive(self.root,result)
      return result

    def _pos_order_recursive(self, current, result): 
      if current: 
        self._pos_order_recursive(current.left,result)
        self._pos_order_recursive(current.right,result)
        result.append(current.value)
    
    #Level Order
    def level_order_traversal(self):
      result = []
      if not self.root:
        return result
      queue = [self.root] #FIFO queue
      while queue: 
        current = queue.pop(0)
        result.append(current.value)
        if current.left: 
          queue.append(current.left)
        if current.right: 
          queue.append(current.right)
      return result