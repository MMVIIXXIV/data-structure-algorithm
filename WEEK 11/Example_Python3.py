
# Python 3 class

class item:
    def __init__(self):
        self.p = None

x = [None]*5
for i in range(5):
    x[i] = item()
    x[i].index = i
    x[i].key = i+10
for i in range(5):
    print(x[i].index, x[i].key, x[i].p)

# -------------------------------------

# Python 3 tuple

y = []
for i in range(5):
    y.append((i, i*2, i*3))
print(y)

# -------------------------------------

# Sorting x based on the key value of each item

def itemKey(a):
    return a.key

x.sort(key = itemKey, reverse=True)
for i in range(5):
    print(x[i].index, x[i].key, x[i].p)

# -------------------------------------

# Sorting y based on the 3rd element of each tuple

def tupleKey(a):
    return a[2]

y.sort(key = tupleKey, reverse=True)
print(y)


'''Certainly! This code demonstrates the use of lists and tuples in Python and how to sort them based on specific criteria. Let's break it down step by step:

1. **Class Definition**:
   - In the first part, a class named `item` is defined. This class has a constructor (`__init__`) method, which initializes instances of the class with three attributes: `p`, `index`, and `key`. However, it doesn't set any initial values for these attributes.

2. **Creating a List of Class Instances**:
   - An empty list `x` is created to store instances of the `item` class. It is initialized as a list of `None` values with a length of 5.
   - A loop runs from 0 to 4, creating instances of the `item` class and assigning them to the `x` list. Each instance has its `index` attribute set to the loop index `i`, and its `key` attribute set to `i + 10`.

   ```python
   x = [item(), item(), item(), item(), item()]
   for i in range(5):
       x[i] = item()
       x[i].index = i
       x[i].key = i + 10
   ```

3. **Printing Attributes of Class Instances**:
   - After creating the instances, another loop prints the `index`, `key`, and `p` attributes of each item in the `x` list. Since the `p` attribute is not set in the constructor or the loop, it will be printed as `None` for each item.

   ```python
   for i in range(5):
       print(x[i].index, x[i].key, x[i].p)
   ```

4. **Creating a List of Tuples**:
   - In the second part of the code, an empty list `y` is created. This list is meant to store tuples.
   - A loop runs from 0 to 4, appending tuples to the `y` list. Each tuple consists of three elements: `i`, `i * 2`, and `i * 3`. So, `y` will contain tuples like `(0, 0, 0)`, `(1, 2, 3)`, and so on.

   ```python
   y = []
   for i in range(5):
       y.append((i, i * 2, i * 3))
   ```

5. **Sorting `x` and `y`**:
   - In the last part of the code, two functions, `itemKey` and `tupleKey`, are defined. These functions are used as key functions for sorting `x` and `y`, respectively.
   - `itemKey` takes an object of the `item` class as an argument and returns its `key` attribute.
   - `tupleKey` takes a tuple as an argument and returns its third element (index 2).
   - The `sort` method is used to sort the `x` list based on the `key` attribute in reverse order (highest to lowest), using the `itemKey` function as the key function.

   ```python
   x.sort(key=itemKey, reverse=True)
   ```

   - Similarly, the `y` list is sorted based on the third element of each tuple, in reverse order, using the `tupleKey` function as the key function.

   ```python
   y.sort(key=tupleKey, reverse=True)
   ```

   - Finally, the sorted `x` and `y` lists are printed.

   ```python
   for i in range(5):
       print(x[i].index, x[i].key, x[i].p)
   print(y)
   ```

In summary, this code demonstrates the creation and manipulation of lists of class instances and tuples. It also shows how to sort these lists based on specific attributes or elements using custom key functions.'''

