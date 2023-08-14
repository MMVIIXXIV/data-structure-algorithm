from sys import stdin

#Reading Operations: The script reads operations from the standard input (stdin) and processes each operation.
#  Each line is split into a list, and if the line has more than two elements, the third element is converted to an integer.


def show_hash_table(hash_table):
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s, table_size):
    # return the hash value
    return hash(s) % table_size
#Hash Function: The hash_func function calculates the hash value of a given string s using the built-in hash function 
# and then takes the modulo of the hash value with the table size to get the index for the hash table.



def insert(hash_table, s, v, table_size):
    k = hash_func(s, table_size)
    for j, _ in hash_table[k]:
        if j == s:
            return -1  # Already exists
    hash_table[k].append((s, v))
    return 0  # Successful insertion
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table
# Insertion: The insert function takes a string s and a value v as input. 
# It calculates the hash value of the string, determines the bucket (index) in the hash table, and appends a tuple (s, v) to the appropriate bucket.
# It returns 0 on successful insertion and -1 if the string is already present in the hash table.




def search(hash_table, s, table_size):
    k = hash_func(s, table_size)
    for j, v in hash_table[k]:
        if j == s:
            return v
    return -1  # Not found
    # return value of the key or
    # return -1 if s does not exists in hash table

# Search: The search function takes a string s as input.
# It calculates the hash value of the string, iterates through the items in the corresponding bucket of the hash table, and returns the associated value v if the string is found.
# If the string is not found, it returns -1.



def delete(hash_table, s, table_size):
    k = hash_func(s, table_size)
    for i, (j, _) in enumerate(hash_table[k]):
        if j == s:
            del hash_table[k][i]
            return 0  # Successful deletion
    return -1  # Not found
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table

# Deletion: The delete function takes a string s as input.
#  It calculates the hash value of the string, searches for the string in the corresponding bucket of the hash table, and removes the item if found. 
# It returns 0 on successful deletion and -1 if the string is not present in the hash table.




# operations = []
# for line in stdin:
#     line = line.split()
#     if len(line) > 2:
#         line[2] = int(line[2])
#     operations.append(line)
# print(operations)


# table_size = 10    # set table size here
# hash_table = [[] for i in range(table_size)]





# for op in operations:
#     # op[0] is "insert" or "search" or "delete"
#     if op[0] == "insert":
#         insert(op[1], op[2])    //result = insert(hash_table, op[1], op[2], table_size)
#         show_hash_table()
#     elif op[0] == "search":
#         print(op[1])
#         print(search(op[1]))
#     elif op[0] == "delete":
#         delete(op[1])
#         show_hash_table()
# Processing Operations: The script then processes each operation read from stdin.
#  For each operation, it calls the appropriate function (insert, search, or delete) based on the operation type.
# It also calls show_hash_table after each insert or delete operation to display the updated hash table.





#this cant stand with collision
# def main():
#     table_size = 10  # set table size here
#     hash_table = [[] for _ in range(table_size)]

#     operations = [
#         ["insert", "key1", 10],
#         ["insert", "key2", 20],
#         ["insert", "key3", 30],
#         ["insert", "key3", 38],
#         ["search", "key1"],
#         ["search", "key4"],
#         ["delete", "key2"],
#         ["insert", "key1", 15],
#         ["delete", "key4"],
#     ]

#     for op in operations:
#         if op[0] == "insert":
#             result = insert(hash_table, op[1], op[2], table_size)
#             if result == 0:
#                 print(f"Inserted ({op[1]}, {op[2]}) successfully.")
#             else:
#                 print(f"Key '{op[1]}' already exists.")
#             show_hash_table(hash_table)
#         elif op[0] == "search":
#             value = search(hash_table, op[1], table_size)
#             if value != -1:
#                 print(f"Value for key '{op[1]}' is: {value}")
#             else:
#                 print(f"Key '{op[1]}' not found.")
#         elif op[0] == "delete":
#             result = delete(hash_table, op[1], table_size)
#             if result == 0:
#                 print(f"Deleted key '{op[1]}' successfully.")
#             else:
#                 print(f"Key '{op[1]}' not found.")
#             show_hash_table(hash_table)

# if __name__ == "__main__":
#     main()



#this can handle collisons
def main():
    table_size = 10  # set table size here
    hash_table = [[] for _ in range(table_size)]

    operations = [
        ["insert", "key1", 10],
        ["insert", "key2", 20],
        ["insert", "key3", 30],
        ["insert", "key4", 40],  # Collision with 'key1'
        ["insert", "key5", 50],  # Collision with 'key1' and 'key4'
        ["search", "key1"],
        ["search", "key4"],
        ["delete", "key2"],
        ["delete", "key4"],
    ]

    for op in operations:
        if op[0] == "insert":
            result = insert(hash_table, op[1], op[2], table_size)
            if result == 0:
                print(f"Inserted ({op[1]}, {op[2]}) successfully.")
            else:
                print(f"Key '{op[1]}' already exists.")
            show_hash_table(hash_table)
        elif op[0] == "search":
            value = search(hash_table, op[1], table_size)
            if value != -1:
                print(f"Value for key '{op[1]}' is: {value}")
            else:
                print(f"Key '{op[1]}' not found.")
        elif op[0] == "delete":
            result = delete(hash_table, op[1], table_size)
            if result == 0:
                print(f"Deleted key '{op[1]}' successfully.")
            else:
                print(f"Key '{op[1]}' not found.")
            show_hash_table(hash_table)

if __name__ == "__main__":
    main()




def explanation_of_all():
    
    #Sure, I'd be happy to explain the key functions and lines of code in the hash table implementation with chaining that you provided. 

    # 1. **Function: `show_hash_table(hash_table)`**
    #    This function is responsible for displaying the contents of the hash table.
    #  It iterates through each bucket in the `hash_table` and prints the items stored in each bucket.
    # This function is useful for visualizing the state of the hash table after each operation.



    # 2. **Function: `hash_func(s, table_size)`**
    #    This function calculates the hash value of a given string `s` using the built-in `hash` function. 
    # The hash value is then modulo'd with `table_size` to determine the index (bucket) in the hash table where the key-value pair should be stored.



    # 3. **Function: `insert(hash_table, s, v, table_size)`**
    #    The `insert` function takes the `hash_table`, a key `s`, a value `v`, and the `table_size` as input. 
    #   It calculates the hash value of the key and determines the bucket (index) where the key-value pair should be inserted.
    #  It checks if the key already exists in the bucket. If it does, it returns -1 to indicate that the key is already present.
    # Otherwise, it appends the key-value pair to the bucket and returns 0 to indicate successful insertion.
    #collision
    # When inserting a new key-value pair, this function calculates the hash value of the key s and determines the bucket (index) in the hash_table where the pair should be stored.
    # It then iterates through the existing key-value pairs in the same bucket to check if the key already exists. If it does, a collision occurs.
    # Instead of overwriting the existing key-value pair, the new pair is appended to the existing bucket, creating a chain of key-value pairs.



    # 4. **Function: `search(hash_table, s, table_size)`**
    #    The `search` function takes the `hash_table`, a key `s`, and the `table_size` as input.
    #  It calculates the hash value of the key and looks through the corresponding bucket to find the key.
    #  If the key is found, it returns the associated value. If the key is not found, it returns -1.
    # #colliosion
    # When searching for a key s, the search function calculates the hash value of the key and looks through the corresponding bucket in the hash_table.
    #     If the key is found in the bucket, it returns the associated value. 
    # If multiple key-value pairs exist in the same bucket due to collisions, the function will iterate through the chain to find the correct key-value pair.



    # 5. **Function: `delete(hash_table, s, table_size)`**
    #    The `delete` function takes the `hash_table`, a key `s`, and the `table_size` as input.
    #  It calculates the hash value of the key and iterates through the corresponding bucket to find the key.
    #  If the key is found, it removes the key-value pair from the bucket and returns 0 to indicate successful deletion. If the key is not found, it returns -1.
    #collision
    #When deleting a key s, the delete function calculates the hash value of the key and iterates through the corresponding bucket in the hash_table.
    #  If the key is found in the bucket, the function removes the associated key-value pair from the bucket.
    #  If there are multiple key-value pairs in the same bucket due to collisions, the function searches the chain to locate and delete the correct pair.



    # 6. **Function: `main()`**
    #    The `main` function is the entry point of the script.
    #  It initializes the hash table, defines a list of operations, and iterates through each operation.
    #  Depending on the operation type (insert, search, delete), it calls the appropriate function and displays the hash table after each operation.



    # 7. **`if __name__ == "__main__":` block**
    #    This block of code ensures that the `main` function is executed only if the script is run directly (not imported as a module). 
    # It's a common best practice in Python to include this block for creating executable scripts.



    # The lines in the `operations` list represent the sequence of operations you want to perform on the hash table, including inserting, searching, and deleting key-value pairs.
    #  The script processes each operation and updates the hash table accordingly.

    # Overall, this implementation demonstrates the basics of a hash table with chaining for handling collisions. It provides a clear example of how key-value pairs are stored, searched, and deleted within a hash table.
    pass


def timecomplexity():
    pass
    # The time complexity of various operations in a hash table implementation with chaining depends on several factors, including the size of the hash table (table_size), the number of elements (n) stored in the hash table, and the distribution of keys and values. Here's a breakdown of the time complexity for each operation:

    # Insertion (insert function):

    # Best Case: O(1) - If there are no collisions and the hash function evenly distributes keys, insertion can be constant time.
    # Average Case: O(1 + α) - In a well-distributed hash table with chaining, where α (load factor) is the average number of elements per bucket,
    #  insertion can be considered constant time with a small factor due to possible collision resolution.
    # Worst Case: O(n) - In the worst case, when all keys hash to the same bucket and create a long chain, insertion time degrades to linear time.
    # Search (search function):

    # Best Case: O(1) - If there are no collisions and the desired key is in the first position of its bucket, search can be constant time.
    # Average Case: O(1 + α) - Similar to insertion, the average case is constant time with a small factor due to possible collisions.
    # Worst Case: O(n) - In the worst case, when all keys hash to the same bucket, and a long chain forms, search time degrades to linear time.
    # Deletion (delete function):

    # Best Case: O(1) - If there are no collisions and the desired key is in the first position of its bucket, deletion can be constant time.
    # Average Case: O(1 + α) - Similar to insertion and search, the average case is constant time with a small factor due to possible collisions.
    # Worst Case: O(n) - In the worst case, when all keys hash to the same bucket, and a long chain forms, deletion time degrades to linear time.


def seperate_chaining():
    # Separate chaining is a collision resolution technique where each bucket of the hash table contains a linked list or another data structure to handle multiple key-value pairs that hash to the same index.
    # This approach effectively creates chains of elements in the same bucket.
    # its the above method
    pass


