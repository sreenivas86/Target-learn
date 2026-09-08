# Hashing Pattern

## 1. What is it?

Hashing is a technique used to store and retrieve data quickly using a **Hash Map (`dict`)** or **Hash Set (`set`)**.

The main advantage is fast lookup.

```text
Hash Map:
Key → Value

"apple"  → 3
"banana" → 5
"orange" → 2
```

```text
Hash Set:
Value

apple
banana
orange
```

Average time for lookup, insertion, and deletion:

```text
O(1)
```

---

## 2. When to use?

Use hashing when the problem requires:

* Fast lookup
* Checking whether an element exists
* Finding duplicates
* Counting frequencies
* Finding a pair/complement
* Storing previously seen elements
* Mapping one value to another
* Grouping similar elements

Common keywords:

```text
"duplicate"
"frequency"
"count"
"seen before"
"exists"
"unique"
"pair"
"complement"
"mapping"
"occurrences"
```

---

## 3. How to identify the pattern

Ask yourself:

```text
Do I need to quickly find something
I have already seen?
             │
             ▼
           YES
             │
             ▼
        Think Hashing
```

### Use `set` when:

You only need to know:

> "Does this value exist?"

Example:

```text
Have I seen 7 before?
```

Use:

```python
seen = set()
```

### Use `dict` when:

You need information associated with a value.

Examples:

```text
Number → Frequency
Number → Index
Character → Count
Character → Character
```

Use:

```python
data = {}
```

### Recognition rule

```text
Existence        → Set
Frequency        → Dictionary
Index lookup     → Dictionary
Mapping          → Dictionary
Previously seen  → Set / Dictionary
Complement       → Dictionary
Grouping         → Dictionary
```

---

## 4. Brute Force Approach

Without hashing, we may repeatedly search through the existing elements.

Example:

```text
nums = [4, 7, 2, 7]
```

To find a duplicate:

```text
4 → compare with remaining elements
7 → compare with remaining elements
2 → compare with remaining elements
7 → duplicate found
```

For every element, we may scan many other elements.

### Complexity

```text
Time  : O(n²)
Space : O(1)
```

The problem is repeated searching.

---

## 5. Optimized Approach

Use a hash set or hash map to remember elements that have already been processed.

Example:

```text
nums = [4, 7, 2, 7]
```

Process each element:

```text
             4
             │
        Already seen?
             │
            NO
             │
             ▼
        Add to Set

Set = {4}
```

Next:

```text
             7
             │
        Already seen?
             │
            NO
             │
             ▼
        Add to Set

Set = {4, 7}
```

Next:

```text
             2
             │
        Already seen?
             │
            NO
             │
             ▼
        Add to Set

Set = {4, 7, 2}
```

Next:

```text
             7
             │
        Already seen?
             │
            YES
             │
             ▼
          Duplicate
```

### Complexity

```text
Time  : O(n) average
Space : O(n)
```

We trade additional memory for faster lookup.

---

## 6. Pseudocode

### General Hashing Pattern

```text
CREATE hash structure

FOR each element:
    
    IF element exists in hash structure:
        
        PROCESS / RETURN ANSWER
    
    ELSE:
        
        STORE element

RETURN result
```

### Frequency Counting

```text
CREATE empty hash map

FOR each element:
    
    IF element exists:
        increase its frequency
    
    ELSE:
        initialize frequency to 1

RETURN hash map
```

### Complement Pattern — Two Sum

```text
CREATE empty hash map

FOR each element:
    
    required = target - current_element
    
    IF required exists in hash map:
        RETURN answer
    
    STORE current_element
```

---

## 7. Python Template

### Hash Set

```python
seen = set()

for value in nums:

    if value in seen:
        # duplicate found
        pass

    seen.add(value)
```

### Frequency Dictionary

```python
frequency = {}

for value in nums:
    frequency[value] = frequency.get(value, 0) + 1
```

### Hash Map for Index Lookup

```python
seen = {}

for i, value in enumerate(nums):

    if value in seen:
        # value already exists
        pass

    seen[value] = i
```

---

## 8. Time & Space Complexity

| Operation | Average | Worst Case |
| --------- | ------: | ---------: |
| Search    |    O(1) |       O(n) |
| Insert    |    O(1) |       O(n) |
| Delete    |    O(1) |       O(n) |

For most DSA interview problems, consider hash lookup as:

```text
Average Time → O(1)
```

Therefore, processing `n` elements usually becomes:

```text
Time  → O(n)
Space → O(n)
```

---

## 9. Example / Dry Run

### Problem

Given:

```text
nums = [2, 7, 11, 15]
target = 9
```

Find two numbers whose sum is `9`.

### Idea

For every number:

```text
required = target - current
```

#### Step 1

Current:

```text
2
```

Required:

```text
9 - 2 = 7
```

Is `7` in the hash map?

```text
NO
```

Store:

```text
2 → index 0
```

Hash Map:

```text
┌──────────────┐
│ 2 → index 0  │
└──────────────┘
```

#### Step 2

Current:

```text
7
```

Required:

```text
9 - 7 = 2
```

Check hash map:

```text
2 → index 0
```

Found!

Therefore:

```text
2 + 7 = 9
```

Answer:

```text
[0, 1]
```

### Pattern

```text
Current value
      │
      ▼
Calculate required value
      │
      ▼
Check Hash Map
      │
   ┌──┴──┐
   │     │
 Found  Not Found
   │     │
   ▼     ▼
Answer  Store current
```

---

## 10. Common Mistakes

### Mistake 1: Using a list for repeated lookup

```python
if value in list:
```

Searching a list takes:

```text
O(n)
```

A set/dictionary provides average:

```text
O(1)
```

---

### Mistake 2: Storing the current value before checking

For problems such as Two Sum, check the required value first.

Correct order:

```text
1. Calculate required value
2. Check hash map
3. Store current value
```

---

### Mistake 3: Confusing Set and Dictionary

```text
Set:
{1, 2, 3}

Dictionary:
{1: 10, 2: 20, 3: 30}
```

Set → existence

Dictionary → key + information

---

### Mistake 4: Forgetting duplicate handling

Always think about:

```text
What happens if the same value appears multiple times?
```

---

### Mistake 5: Ignoring space complexity

Hashing improves time but normally requires additional memory.

```text
Time  ↓
Space ↑
```

This is the common trade-off.

---

## 11. Similar Problems

### Beginner

* Contains Duplicate
* Two Sum
* Valid Anagram
* Ransom Note
* Jewels and Stones

### Intermediate

* Group Anagrams
* Happy Number
* Isomorphic Strings
* Word Pattern
* Longest Consecutive Sequence
* Contains Duplicate II

### Advanced / Combination Patterns

* Top K Frequent Elements
* Subarray Sum Equals K
* Longest Substring Without Repeating Characters
* Minimum Window Substring

Important combinations:

```text
Hashing + Sliding Window
Hashing + Prefix Sum
Hashing + Heap
Hashing + Two Pointers
```

---

## 12. Real-World Use

Hashing is heavily used in software systems.

### Database / Application Lookup

```text
User ID → User Details
```

Instead of searching every user, use a key for fast lookup.

### Caching

```text
Request Key → Cached Result
```

Example:

```text
"user:101" → User information
```

### Authentication / Sessions

```text
Session ID → User Session
```

### Frequency Analysis

Used for:

```text
Log analysis
Word frequency
Event counting
API request counting
```

### Distributed Systems

Hashing is also used in:

```text
Caching
Partitioning
Load distribution
Deduplication
Data lookup
```

---

## 13. Key Takeaway

Remember these rules:

```text
Fast lookup?
      ↓
   Hashing
```

```text
Need existence?
      ↓
     Set
```

```text
Need key → value?
      ↓
    Dictionary
```

```text
Need frequency?
      ↓
 Frequency Map
```

```text
Need previously seen values?
      ↓
   Set / Map
```

```text
Need complement?
      ↓
 Hash Map
```

### One-minute interview explanation

> Hashing is a technique for storing data in a hash map or hash set so that we can perform lookup efficiently. In Python, `dict` and `set` are commonly used for hashing. I use a set when I only need to check existence, and a dictionary when I need to associate a key with information such as frequency or index. Hashing usually reduces repeated-search problems from O(n²) to O(n) time at the cost of O(n) additional space.

| If the problem says / asks...        | Think                    | Use            |
| ------------------------------------ | ------------------------ | -------------- |
| Does this element exist?             | Fast existence check     | `set`          |
| Have I seen this before?             | Track previous elements  | `set`          |
| Find duplicates                      | Track visited values     | `set`          |
| Count frequency / occurrences        | Frequency counting       | `dict`         |
| Find a pair with target sum          | Complement lookup        | `dict`         |
| Find `target - current`              | Complement pattern       | `dict`         |
| Store value → index                  | Fast index lookup        | `dict`         |
| Store character → count              | Character frequency      | `dict`         |
| Group similar elements               | Key-based grouping       | `dict`         |
| Find unique elements                 | Frequency / existence    | `set` / `dict` |
| Contiguous subarray + target sum     | Prefix Sum + Hashing     | `dict`         |
| Longest substring without duplicates | Sliding Window + Hashing | `set` / `dict` |
| Top K frequent elements              | Frequency + Heap         | `dict` + Heap  |
