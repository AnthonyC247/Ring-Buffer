class RingBuffer:
 
     def __init__(self, k: int): #Initializes the ringBuffer with a maximum size of k.
       self.k = k #To keep account of the maxsize of the queue 
       self.size = 0 #To keep track of the current size of the queue
       self.queue = [None] * k #Queue
       self.head = 0 #Naturally starts and will only change when either the full capacity and want to add another object
       self.tail = 0 #To scooch it up one before the head 

     def en_queue(self, value: int) -> None:
        #Adds an item at the rear of the queue. 
        #If the queue is full, then remove the front element and place the new value at the back of the queue
      
      if self.size == self.k: #To check if the queue has reached the max size

        
        '''append a new element overwriting the previous one'''
        self.queue[self.head] = value
        self.tail = (self.tail+1) % self.k
        self.head = (self.head+1) % self.k

      else: #Update the tail
        
        self.queue[self.tail] = value
        self.tail  = (self.tail + 1) % self.k
        self.size = self.size + 1

  
        

     def de_queue(self) -> bool: # Deletes the item at the front of the queue. otherwise returns False if the operation is not successful.
      if self.size == 0: #If the queue is empty 
        return False

      '''Operation implemented to delete item at front of queue'''
      temp = self.queue[self.head] #Assigning queue to access the front or head 
      self.queue[self.head] = None # First element is starting from the beginning 
      self.head = (self.head + 1) % self.k #implementing operation to delete front item
      self.size = self.size - 1 # Size decreases as first item deleted 
      return True

     def get_front(self) -> int: #Returns the front item from the queue. Returns -1 if the queue is empty.

      if self.size != 0: #Check if the queue is empty 
        return self.queue[self.head] #If the queue is empty, get the front or the head of the queue
      else:
        return -1 #If the queue is empty, return as integer -1 

     def get_rear(self) -> int: #Returns the last item from the queue. Returns -1 if the queue is empty.

      if self.size != 0: #Check if the queue is empty 
        #return self.queue[-1]
         return self.queue[self.tail-1] #If queue is not empty, get the back of the queue or tail 
      else:
        return -1 #If queue not empty return as integer -1

     def is_empty(self) -> bool: # Returns true if the queue is empty, or false otherwise.

      if self.size == 0: #Check if the queue is empty
        return True #If empty return Boolean expression True 
      else:
        return False #If not empty return Boolean expression False 

     def is_full(self) -> bool: #Returns true if the queue is full, or false otherwise.

      if self.size == self.k: #If the queue has reached max capacity 
        return True #If it is full, return Boolean expression True
      return False #If not full, return Boolean expression False

     def get_average(self) -> float: #Returns average of numbers in the ringBuffer, if it is empty returns None

      if self.size == 0: #Check if the queue is empty 
        return None #If the queue is empty return Boolean expression False 
      else:
        index = self.head #Assign starting index to the beginning or left of the queue, self.head 
        sum = 0 #To keep track of the average for later 
        for i in range(self.size): #Loop through the items of the size of the queue 
          sum += self.queue[index] #To increment through my queue at the head or the beginning 


          index = (index+1) % self.k #Modulus to implement the remainder of elements
      return sum / self.size #returning the average by diving the total by amount of elements