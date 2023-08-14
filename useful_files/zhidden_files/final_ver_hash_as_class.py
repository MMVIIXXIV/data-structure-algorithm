class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)]

    def show_hash_table(self):
        """Displays the contents of the hash table."""
        print('-------------------')
        for item_list in self.hash_table:
            print(item_list)
        print('-------------------')

    def hash_func(self, s):
        """Returns the hash value of the given string."""
        return hash(s) % self.table_size

    def insert(self, s, v):
        """Inserts a key-value pair into the hash table using chaining for collision handling."""
        k = self.hash_func(s)
        for j, _ in self.hash_table[k]:
            if j == s:
                return -1  # Key already exists
        self.hash_table[k].append((s, v))
        return 0  # Successful insertion

    def search(self, s):
        """Searches for a key and returns its associated value."""
        k = self.hash_func(s)
        for j, v in self.hash_table[k]:
            if j == s:
                return v
        return -1  # Key not found

    def delete(self, s):
        """Deletes a key and its associated value from the hash table."""
        k = self.hash_func(s)
        for i, (j, _) in enumerate(self.hash_table[k]):
            if j == s:
                del self.hash_table[k][i]
                return 0  # Successful deletion
        return -1  # Key not found


def main():
    table_size = 10  # Set table size here
    hash_table = HashTable(table_size)

    operations = [
        ["insert", "key1", 10],
        ["insert", "key2", 20],
        ["insert", "key3", 30],
        ["insert", "key1", 15],  # Insert with chaining
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


# class HashTable: - Defines the HashTable class that encapsulates the hash table and its methods.

# def __init__(self, table_size): - The constructor initializes a new HashTable instance with the specified table_size.

# def show_hash_table(self): - Displays the contents of the hash table. This method iterates through each bucket and prints the key-value pairs.

# def hash_func(self, s): - Returns the hash value of the given string s based on the hash table's table_size.

# def insert(self, s, v): - Inserts a new key-value pair into the hash table using chaining to handle collisions. It checks if the key already exists in the bucket before insertion.

# def search(self, s): - Searches for a key in the hash table and returns its associated value if found.

# def delete(self, s): - Deletes a key and its associated value from the hash table.

# def main(): - The main function that demonstrates the usage of the HashTable class. It creates a new HashTable instance, performs a sequence of operations (insertion, search, deletion), and displays the hash table after each operation.

# if __name__ == "__main__": - Ensures that the main function is executed only if the script is run directly, not imported as a module.




#ezxample

# The key-value pair ("key1", 10) is successfully inserted into the hash table.
# The hash table is displayed, showing the inserted key-value pair in the appropriate bucket.
# The key-value pair ("key2", 20) is inserted successfully, and the updated hash table is displayed.
# The key-value pair ("key3", 30) is inserted successfully, and the updated hash table is displayed.
# An attempt to insert ("key1", 15) fails since the key already exists in the same bucket, and the hash table remains unchanged.
# A search for "key1" returns the value 10.
# A search for "key4" fails as the key is not found.
# The key "key2" is deleted, and the updated hash table is displayed.
# An attempt to delete "key4" fails as the key is not found.
# The final state of the hash table is displayed.