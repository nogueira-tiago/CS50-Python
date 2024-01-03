class Jar:
    def __init__(self, capacity = 12) :
        if not isinstance(capacity, int) or capacity< 0:
            raise ValueError("Capacity can't be negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size
    
    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit can't be negative.")
        
        if self._size + n > self._capacity:
            raise ValueError("Jar capacity exceeded.")
        
        self._size += n
        
    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit can't be negative.")
        
        if n > self._size:
            raise ValueError("No cookie to withdraw.")
        
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size