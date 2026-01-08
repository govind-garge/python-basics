# List in python

my_list=[1,2,3,4,5,6,7,8]

print("type of list:", type(my_list))

#change list item
my_list[7]=1

print(my_list)

# Slicing values from array same as string
print("Slicing values from list:", my_list[0:4])

#list count
print("count of list :", len(my_list))

#list sorting
print("list sorting :")
my_list.sort(reverse=True)
print(my_list)

#List functions

# L.append(item) : Adds a single item to the end of the list.
# L.insert(index, item) : Inserts an item at the specified index.
# L.extend(iterable) : Appends all items from an iterable (like another list) to the end of the list.

# L.remove(item) : Removes the first occurrence of the specified item. Raises ValueError if not found.
# L.pop(index) : Removes and returns the element at the specified index. If no index is given, it removes the last item.
# L.clear() : Removes all items from the list, leaving it empty.

# L.count(item) : Returns the number of times an item appears in the list.
# L.index(item) : Returns the lowest index at which the item appears. Raises ValueError if not found.

# L.sort() : Sorts the list in place (modifies the original list) alphabetically or numerically.
# L.reverse() : Reverses the order of the elements in the list in place.
# L.copy() : Returns a shallow copy of the list (a new list with the same elements).

####################### Tuples in phython #################################

# list and tuples are same but list is mutable(changable) and tuple is immutable(non changable)

my_tuple=(1,2,3,4,5,6,7,8)

print("type of tuple:", type(my_tuple))
