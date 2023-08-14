from sys import stdin


# Read the sequence of operations to be operated on the hash table



# Read the sequence of operations to be operated on the hash table
# operations = []
# for line in stdin:
#     line = line.split()
#     if len(line) > 2:
#         line[2] = int(line[2])
#     operations.append(line)



print("Enter operations in the format: insert key value, search key, delete key")
print("Enter 'quit' to stop input.")
operations = []
while True:
    user_input = input()
    if user_input.lower() == 'quit':
        break
    line = user_input.strip().split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)




table_size = 10    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')
 
print(show_hash_table())
print(hash_table)

def hash_func(s):
    # return the hash value
    hash = 0
    for char in s:
        hash += ord(char)
    return hash % table_size



def insert(s, v):
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table
    if search(s) != -1:
        return -1
    else:
        hash_val = hash_func(s)
        l = hash_table[hash_val]
        l.append((s,v))
        return 0


def search(s):
    # return value of the key or
    # return -1 if s does not exists in hash table
    hash_val = hash_func(s)
    l= hash_table[hash_val]
    for i in range(len(l)):
        # if l[0] == s:
        #     return l[1]
        if l[i][0] == s:
            return l[i][1]
    return -1

def delete(s):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table
    if search(s) == -1:
        return -1
    else:
        hash_val = hash_func(s)
        l = hash_table[hash_val]
        for i in range(len(l)):
            if l[i][0] == s:
                return l[i][1]
            return 0


# The main program to execute the sequence of operations
# for op in operations:
#     # op[0] is "insert" or "search" or "delete"
#     if op[0] == 'insert':
#         insert(op[1],op[2])
#     elif op[0] == 'search':
#         search(op[1])
#     elif op[0] == 'delete':
#         delete(op[1])
#     else:
#         pass

# print(show_hash_table())

for op in operations:
    # op[0] is "insert" or "search" or "delete"
    if op[0] == 'insert':
        result = insert(op[1], op[2])
        if result == -1:
            print(f"{op[1]} is already in the hash table.")
    elif op[0] == 'search':
        result = search(op[1])
        if result == -1:
            print(f"{op[1]} not found in the hash table.")
        else:
            print(f"{op[1]} found with value: {result}")
    elif op[0] == 'delete':
        result = delete(op[1])
        if result == -1:
            print(f"{op[1]} not found in the hash table.")
        else:
            print(f"{op[1]} deleted with value: {result}")
    else:
        pass

show_hash_table()