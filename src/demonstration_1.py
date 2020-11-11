"""
Your task is create your own HashTable without using a built-in library.

Your HashTable needs to have the following functions:

- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.

Example:

```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self):
    # define the array and its finite size 
        self.array = [None] * 20
        


    def put(self, key, value):
    # use baked in hash() function to hash the key
        hash_key = hash(key) 
    # map the hashed key to an index in the array 
        index = hash_key % len(self.array)
    # put the value in the array at that index 
        self.array[index] = value


    def get(self, key):
    # return the value of the index at the index of the key 
        hash_key = hash(key)
    # hash the key, map it to the index 
        index = hash_key % len(self.array)
    # handling instance where there is no item in the index 
        if self.array[index] is None:
            return -1
    # return the value at that index
        return self.array[index]


    def remove(self, key: int) -> None:
        hash_key = hash(key)
        index = hash_key % len(self.array)
        self.array[index] = None


