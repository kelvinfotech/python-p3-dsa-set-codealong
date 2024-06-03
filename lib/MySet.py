class MySet:
    def __init__(self, initial=None):
        """Initialize the set with an optional initial list of values"""
        self.dictionary = {}
        if initial:
            for item in initial:
                self.dictionary[item] = True

    def add(self, item):
        """Add an item to the set"""
        self.dictionary[item] = True

    def delete(self, item):
        """Remove an item from the set if it exists"""
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        """Check if an item is in the set"""
        return item in self.dictionary

    def size(self):
        """Return the number of items in the set"""
        return len(self.dictionary)

    def clear(self):
        """Remove all items from the set"""
        self.dictionary.clear()

    def __str__(self):
        """Return a string representation of the set"""
        items = ','.join(map(str, self.dictionary.keys()))
        return f'MySet: {{{items}}}'