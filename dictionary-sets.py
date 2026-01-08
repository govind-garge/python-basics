###################### Dictionary in Python ##########################################

# you can diclare empty dictionary, and then assign the value
my_dic ={}
my_dic["name"]="Govind"

# or declare it with information
my_dictionary = {
    "name": "Govind",
    "City": "Pune",
    "mobile":9999999999,
    "list":[1,2,3,4,5,6,7],
    "sub_dictionaty":{
        "name":"sub dictionary"
    }
}

print("type of Dictionary:", type(my_dictionary))

print("Dictionary:", my_dictionary)

print("Dictionary:", my_dictionary["name"])

print("Get Dictionary item:", my_dictionary.get("name"))

print("Dictionary:", my_dictionary["sub_dictionaty"]["name"])

my_dictionary["name"] = "Garge"
print("Dictionary Mutable:", my_dictionary["name"])

my_dictionary.update({"name":"Govind"})

print("Dictionary Mutable:", my_dictionary["name"])


# Dictionaty methods

# dict.clear() : Removes all items (key:value pairs) from the dictionary.
# dict.copy() : Returns a shallow copy of the dictionary.

# dict.fromkeys(keys, value) : Creates a new dictionary with specified keys and an optional common value.

# dict.get(key) : Returns the value for the specified key. Returns None if the key is not found (instead of raising an error).
# dict.get(key, default) : Returns the value for the specified key. Returns the optional 'default' value if the key is not found.

# dict.items() : Returns a view object (a list-like structure) of the dictionary's key-value pairs as tuples (key, value).
# dict.keys() : Returns a view object of all the keys in the dictionary.
# dict.values() : Returns a view object of all the values in the dictionary.

# dict.pop(key) : Removes the item with the specified key and returns its value. Raises a KeyError if the key is not found.
# dict.popitem() : Removes and returns the last inserted key:value pair as a tuple (key, value). Raises KeyError if the dictionary is empty.

# dict.setdefault(key) : Returns the value of the specified key. If the key is not present, it inserts the key with the value None.
# dict.setdefault(key, default) : Returns the value of the key. If the key is not present, it inserts the key with the specified 'default' value.

# dict.update(iterable) : Inserts items from another dictionary or from an iterable of key:value pairs into the current dictionary.

########################### Set in Python ####################################

# Set are mutable but the elements of set is immutable and we can't add list or dictionary in set as it is mutable 
# Sets are unordered collections of unique elements

my_set = set() #declare empty set

my_set = {1,2,3, 4.5, "any string"}

print("Type of Set in python:", type(my_set))
print("Set in python:", my_set)

# Set functions in python

# set.add(item) : Adds a single item to the set. If the item is already present, nothing happens.
# set.update(iterable) : Adds elements from an iterable (like a list, tuple, or another set) to the set.

# set.remove(item) : Removes the specified item from the set. Raises a KeyError if the item is not found.
# set.discard(item) : Removes the specified item from the set. Does nothing if the item is not found (no error).
# set.pop() : Removes and returns an arbitrary (random) element from the set. Raises KeyError if the set is empty.
# set.clear() : Removes all elements from the set.

# set.union(other_set) : Returns a NEW set containing all items from both sets (equivalent to set1 | set2).
# set.intersection(other_set) : Returns a NEW set containing ONLY the items present in both sets (equivalent to set1 & set2).
# set.difference(other_set) : Returns a NEW set containing items ONLY present in the first set, not the second (equivalent to set1 - set2).
# set.symmetric_difference(other_set) : Returns a NEW set containing items present in EITHER set, but NOT both (equivalent to set1 ^ set2).

# set.issubset(other_set) : Returns True if all elements of the set are present in the other_set (set1 <= set2).
# set.issuperset(other_set) : Returns True if all elements of the other_set are present in the set (set1 >= set2).
# set.isdisjoint(other_set) : Returns True if the two sets have NO elements in common.

# set.copy() : Returns a shallow copy of the set.
