class MusicQueue:
    # Initialise queue
    def __init__(self):
        self.queue = []

    # add message to queue
    def enqueue(self, message):
        # TODO check if file is on disk, if multiple exist, add random one
        self.queue.append(message)

    # Pop first element
    def dequeue(self):
        return self.queue.pop(0)

    # Remove element at idx
    def removeIdx(self, idx):
        if idx < self.size():
            self.queue.pop(idx)
            return True
        return False

    # Remove first instance of message
    def remove(self, message):
        pos = self.findSubStr(message)
        if len(pos) != 0:
            self.removeIdx(pos[0])
            return True
        return False
    
    # Remove all instances of message from queue
    def removeAll(self, message):
        pos = self.findSubStr(message)
        if len(pos) == 0:
            return False
        for idx in pos:
            self.removeIdx(idx)
        return True

    # Return size of queue
    def size(self):
        return len(self.queue)

    # Find the array indeces of specific substrings
    def findSubStr(self, message):
        return [idx for idx, elem in enumerate(self.queue) if message in elem]

    # Count the instances of a substring
    def count(self, message):
        return len(self.findSubStr(message))

    # Return element at idx
    def at(self, idx):
        return self.queue[idx]

    # index search
    def index(self, searchTerm):
        return self.queue.index(searchTerm)