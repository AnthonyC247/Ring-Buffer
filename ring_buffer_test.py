ringBuffer = RingBuffer(3)

print(ringBuffer.is_empty()) # return True

print(ringBuffer.en_queue(1)) # return None (No return is necessary for this function)

print(ringBuffer.en_queue(2)) # return None

print(ringBuffer.en_queue(3)) # return None

print(ringBuffer.en_queue(4)) # return None (the queue is full).  → it should overwrite the old values 

print(ringBuffer.get_rear())     # return 4

print(ringBuffer.get_front())    # return 2

print(ringBuffer.is_full())       # return True

print(ringBuffer.get_average()) # return 3.0

print(ringBuffer.de_queue())  # return True

print(ringBuffer.is_full())      # return False

print(ringBuffer.de_queue())   # return True

print(ringBuffer.de_queue())   # return True

print(ringBuffer.de_queue())   # return False (queue is empty)

print(ringBuffer.is_empty())    # return True

print(ringBuffer.get_rear())      # return -1

print(ringBuffer.get_front())     # return -1