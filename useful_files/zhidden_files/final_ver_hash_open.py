# #Open Addressing:
# Open addressing is a family of collision resolution techniques where all elements are stored directly in the hash table itself, even if there is a collision.
# When a collision occurs, the algorithm searches for the next available slot in the table and inserts the element there.
# Linear Probing: In linear probing, if a collision occurs, the algorithm searches for the next available slot by incrementing the index until an empty slot is found.
# Quadratic Probing: Similar to linear probing, but the algorithm uses a quadratic function to determine the next slot to check after a collision.
# Double Hashing: In double hashing, the algorithm uses a second hash function to determine the interval between slot checks after a collision. This helps distribute elements more evenly.

from sys import stdin
##for lineear probing
class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def show_hash_table(self):
        """Displays the contents of the hash table."""
        print('-------------------')
        for item in self.hash_table:
            print(item)
        print('-------------------')

    def hash_func(self, s):
        """Returns the hash value of the given string."""
        return hash(s) % self.table_size

    def insert(self, s, v):
        """Inserts a key-value pair into the hash table using linear probing."""
        k = self.hash_func(s)
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                return -1  # Key already exists
            k = (k + 1) % self.table_size  # Move to the next slot using linear probing
        self.hash_table[k] = (s, v)  # Insert at the empty slot
        return 0  # Successful insertion

    def search(self, s):
        """Searches for a key and returns its associated value."""
        k = self.hash_func(s)
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                return self.hash_table[k][1]  # Return the value if key is found
            k = (k + 1) % self.table_size  # Move to the next slot using linear probing
        return -1  # Key not found

    def delete(self, s):
        """Deletes a key and its associated value from the hash table."""
        k = self.hash_func(s)
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                self.hash_table[k] = None  # Mark the slot as empty
                return 0  # Successful deletion
            k = (k + 1) % self.table_size  # Move to the next slot using linear probing
        return -1  # Key not found

def main():
    table_size = 10  # Set table size here
    hash_table = HashTable(table_size)

    operations = [
        ["insert", "key1", 10],
        ["insert", "key2", 20],
        ["insert", "key3", 30],
        ["insert", "key1", 15],  # Insert with linear probing
        ["search", "key1"],
        ["search", "key4"],
        ["delete", "key2"],
        ["delete", "key4"],
    ]

    for op in operations:
        if op[0] == "insert":
            result = hash_table.insert(op[1], op[2])
            if result == 0:
                print(f"Inserted ({op[1]}, {op[2]}) successfully.")
            else:
                print(f"Key '{op[1]}' already exists.")
            hash_table.show_hash_table()
        elif op[0] == "search":
            value = hash_table.search(op[1])
            if value != -1:
                print(f"Value for key '{op[1]}' is: {value}")
            else:
                print(f"Key '{op[1]}' not found.")
        elif op[0] == "delete":
            result = hash_table.delete(op[1])
            if result == 0:
                print(f"Deleted key '{op[1]}' successfully.")
            else:
                print(f"Key '{op[1]}' not found.")
            hash_table.show_hash_table()

if __name__ == "__main__":
    main()




#quardric probing
from sys import stdin

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def show_hash_table(self):
        """Displays the contents of the hash table."""
        print('-------------------')
        for item in self.hash_table:
            print(item)
        print('-------------------')

    def hash_func(self, s):
        """Returns the hash value of the given string."""
        return hash(s) % self.table_size

    def insert(self, s, v):
        """Inserts a key-value pair into the hash table using quadratic probing."""
        k = self.hash_func(s)
        i = 1
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                return -1  # Key already exists
            k = (k + i * i) % self.table_size  # Quadratic probing
            i += 1
        self.hash_table[k] = (s, v)
        return 0  # Successful insertion

    def search(self, s):
        """Searches for a key and returns its associated value."""
        k = self.hash_func(s)
        i = 1
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                return self.hash_table[k][1]
            k = (k + i * i) % self.table_size  # Quadratic probing
            i += 1
        return -1  # Key not found

    def delete(self, s):
        """Deletes a key and its associated value from the hash table."""
        k = self.hash_func(s)
        i = 1
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                self.hash_table[k] = None
                return 0  # Successful deletion
            k = (k + i * i) % self.table_size  # Quadratic probing
            i += 1
        return -1  # Key not found

def main():
    table_size = 10  # Set table size here
    hash_table = HashTable(table_size)

    operations = [
        ["insert", "key1", 10],
        ["insert", "key2", 20],
        ["insert", "key3", 30],
        ["insert", "key1", 15],  # Insert with quadratic probing
        ["search", "key1"],
        ["search", "key4"],
        ["delete", "key2"],
        ["delete", "key4"],
    ]

    for op in operations:
        if op[0] == "insert":
            result = hash_table.insert(op[1], op[2])
            if result == 0:
                print(f"Inserted ({op[1]}, {op[2]}) successfully.")
            else:
                print(f"Key '{op[1]}' already exists.")
            hash_table.show_hash_table()
        elif op[0] == "search":
            value = hash_table.search(op[1])
            if value != -1:
                print(f"Value for key '{op[1]}' is: {value}")
            else:
                print(f"Key '{op[1]}' not found.")
        elif op[0] == "delete":
            result = hash_table.delete(op[1])
            if result == 0:
                print(f"Deleted key '{op[1]}' successfully.")
            else:
                print(f"Key '{op[1]}' not found.")
            hash_table.show_hash_table()

if __name__ == "__main__":
    main()




#double hashing
from sys import stdin

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def show_hash_table(self):
        """Displays the contents of the hash table."""
        print('-------------------')
        for item in self.hash_table:
            print(item)
        print('-------------------')

    def hash_func(self, s):
        """Returns the primary hash value of the given string."""
        return hash(s) % self.table_size

    def hash_func_secondary(self, s):
        """Returns the secondary hash value of the given string."""
        return 1 + (hash(s) % (self.table_size - 1))  # Ensure it's non-zero and less than table size

    def insert(self, s, v):
        """Inserts a key-value pair into the hash table using double hashing."""
        k = self.hash_func(s)
        i = 1
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                return -1  # Key already exists
            k = (k + i * self.hash_func_secondary(s)) % self.table_size  # Double hashing
            i += 1
        self.hash_table[k] = (s, v)
        return 0  # Successful insertion

    def search(self, s):
        """Searches for a key and returns its associated value."""
        k = self.hash_func(s)
        i = 1
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                return self.hash_table[k][1]
            k = (k + i * self.hash_func_secondary(s)) % self.table_size  # Double hashing
            i += 1
        return -1  # Key not found

    def delete(self, s):
        """Deletes a key and its associated value from the hash table."""
        k = self.hash_func(s)
        i = 1
        while self.hash_table[k] is not None:
            if self.hash_table[k][0] == s:
                self.hash_table[k] = None
                return 0  # Successful deletion
            k = (k + i * self.hash_func_secondary(s)) % self.table_size  # Double hashing
            i += 1
        return -1  # Key not found
line_one=[x for x in input().split()]

def main():
    table_size = 10  # Set table size here
    hash_table = HashTable(table_size)

    operations = [
        ["insert", "key1", 10],
        ["insert", "key2", 20],
        ["insert", "key3", 30],
        ["insert", "key1", 15],  # Insert with double hashing
        ["search", "key1"],
        ["search", "key4"],
        ["delete", "key2"],
        ["delete", "key4"],
    ]

    for op in operations:
        if op[0] == "insert":
            result = hash_table.insert(op[1], op[2])
            if result == 0:
                print(f"Inserted ({op[1]}, {op[2]}) successfully.")
            else:
                print(f"Key '{op[1]}' already exists.")
            hash_table.show_hash_table()
        elif op[0] == "search":
            value = hash_table.search(op[1])
            if value != -1:
                print(f"Value for key '{op[1]}' is: {value}")
            else:
                print(f"Key '{op[1]}' not found.")
        elif op[0] == "delete":
            result = hash_table.delete(op[1])
            if result == 0:
                print(f"Deleted key '{op[1]}' successfully.")
            else:
                print(f"Key '{op[1]}' not found.")
            hash_table.show_hash_table()


if __name__ == "__main__":
    main()



#Linear Probing:

# Advantages:

# Simple to implement and requires minimal additional memory.
# Can be efficient when the load factor is low.
# Disadvantages:

# Susceptible to primary clustering (clustering of elements around the same hash index).
# Degraded performance as the load factor increases.
# Poor cache performance due to consecutive memory locations being used.
# Time Complexity:

# Normal Case: O(1)
# Best Case (No Collisions): O(1)
# Worst Case (Many Collisions): O(n) due to clustering
# Quadratic Probing:

# Advantages:

# Less susceptible to primary clustering compared to linear probing.
# Provides better distribution of elements than linear probing.
# Can perform well when load factor is moderate.
# Disadvantages:

# Secondary clustering can still occur.
# Quadratic probing does not guarantee that all slots will be visited.
# Time Complexity:

# Normal Case: O(1)
# Best Case (No Collisions): O(1)
# Worst Case (Many Collisions): O(n) due to secondary clustering
# Double Hashing:

# Advantages:

# Better distribution of elements compared to linear and quadratic probing.
# Less clustering, leading to more even distribution of elements.
# Generally provides better performance than linear and quadratic probing.
# Disadvantages:

# Slightly more complex to implement due to the need for a secondary hash function.
# May require more memory due to the secondary hash function.
# Time Complexity:

# Normal Case: O(1)
# Best Case (No Collisions): O(1)
# Worst Case (Many Collisions): O(n) in rare cases, but generally performs well due to less clustering

# In summary, linear probing is the simplest to implement but can suffer from clustering, which affects worst-case performance.
#  Quadratic probing is a slight improvement over linear probing in terms of clustering, but it may still encounter secondary clustering.
#  Double hashing offers the best distribution of elements and is generally more efficient, although it requires a secondary hash function.