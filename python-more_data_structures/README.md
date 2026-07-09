This chapter describes some things you’ve learned about already in more detail, and adds some new things as well.

5.1. More on Lists
The list data type has some more methods. Here are all of the methods of list objects:

list.append(value, /)
Add an item to the end of the list. Similar to a[len(a):] = [x].

list.extend(iterable, /)
Extend the list by appending all the items from the iterable. Similar to a[len(a):] = iterable.

list.insert(index, value, /)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(value, /)
Remove the first item from the list whose value is equal to value. It raises a ValueError if there is no such item.

list.pop(index=-1, /)
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()
Remove all items from the list. Similar to del a[:].

list.index(value[, start[, stop]])
Return zero-based index of the first occurrence of value in the list. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(value, /)
Return the number of times value appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
