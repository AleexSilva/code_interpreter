### **Code**
```python
from collections import defaultdict, deque
from heapq import heappushpop, heapify, heappop, heappush
import math
from functools import cmp_to_key
from itertools import accumulate, combinations, permutations
from operator import add, sub, mul, truediv, mod, floordiv

def generate_authors(books):
    """Generate authors from a list of books"""
    
    yield from {book.get("author") for book in books if book.get("author")}
```

### **Explanation**
This function generates all the unique authors found in a list of books.

Here's how it works:

1. `yield from` is used to delegate part of a generator's execution to another generator.
2. `{book.get("author") for book in books if book.get("author")}` is a generator expression that iterates over each book in the `books` list, and yields the author field if it exists in any book.

The `.get()` method is used instead of `.get('author')` to avoid KeyError if an author does not exist in a book. The `.get()` function returns None if the author key does not exist instead of throwing an error.

The entire generator expression can be thought of as: "for each book in `books`, yield the author name for this book".

### **Code Improvement**
No possible improvement