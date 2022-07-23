
# 1. What exactly is []?
"""It is an empty list"""

# 2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
# third value? (Assume [2, 4, 6, 8, 10] are in spam.)
import copy

"""
spam = [2,4,6,8,10]
spam[2] = "Hello"
"""

#3. spam = ['a','b','c','d']
"""What is the value of spam[int(int((3*2); * 2) / 11)]?"""
"""Sol: d"""

#4.What is the value of spam[-1]?
"""Sol: d"""

# 5. 5. What is the value of spam[:2]?
"""Sol : ab"""

# bacon = [3.14, cat, 11, cat, True]
#6. What is the value of bacon.index('cat')?
"""
Sol: 1
"""

#7.How does bacon.append(99) change the look of the list value in bacon?
"""
bacon = [3.14, cat, 11, cat, True, 99]
"""

#8. How does bacon.remove('cat') change the look of the list in bacon?
"""
bacon = [3.14, 11, True,cat, 99]
"""

#9. What are the list concatenation and list replication operators?

"""
List concatenation : "+" operator
List replication : "*" operator
"""

#10.What is difference between the list methods append() and insert()?

"""
insert(): This function inserts the values at the particular location
l.insert(0,2) = Inserts 2 at 0th index
append(): This function adds the value at the end of the list
l,append(2) = Appends at the end of the list
"""

# 11. What are the two methods for removing items from a list?
"""
l.remove()
l.pop()
"""

#12. Describe how list values and string values are identical.
"""
Solution:
li = [1,2,3,4]
s = "1234"
print(s[0],li[0])

In the above example, the list values and string values can be extracted
from the same indices.
They have the same values
"""
#13. What is the difference between tuples and lists?

"""Lists are mutable and tuples are immutable."""

# 14. How do you type a tuple value that only contains the integer 42?
"""

Solution:
t1 = (1,23,42,34,7)

"""

#15. How do you get a list values tuple form? How do you get a tuple values list form?

"""
l = [1,2,3,4]
t1 = tuple(l)
l1 = list(t1)
"""

#16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
"""
t = (1,2,[4,5,6],7,8)
They can be tuples
"""

#17. How do you distinguish between copy.copy() and copy.deepcopy()?

"""
l = [1,2,3]
d = l.copy()
d1 = l.deepcopy()
print(d)
l.append(4)
print(d)
print(id(l),id(d), id(d1))

In shallow copy, any changes in the value of d will make changes in the value of l
In deepcopy, any changes in the value of d will not change the original list that is l

"""
import copy
l = [1,2,3]
d = l.copy()
d1 = l.deepcopy()
print(d)
l.append(4)
print(d)
print(id(l),id(d), id(d1))




