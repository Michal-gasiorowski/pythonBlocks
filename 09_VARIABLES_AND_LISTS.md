# Variables and lists

If you dont know how to interact with variables and lists in python, but you know how to do it in word blocks, here is a simple reference to help you out.

# Table of contents

1. [make a variable](#make-a-variable)
2. [print a variable](#print-a-variable)
3. [set variable to](#set-variable-to)
4. [change variable by](#change-variable-by)
5. [global vs local variables](#global-vs-local-variables)
6. [make a list](#make-a-list)
7. [add to list](#add-to-list)
8. [delete from list](#delete-from-list)
9. [delete all of](#delete-all-of)
10. [insert at](#insert-at)
11. [replace item with](#replace-item-with)
12. [item of](#item-of)
13. [item # of](#item-num-of)
14. [length of](#length-of)
15. [contains](#contains)

## make a variable

![alt text](/images/blocks/Variables_makeAVariable.png)

```python
new_variable = 0
```

## print a variable

```python
print(new_variable)
```

## set variable to

![alt text](/images/blocks/Variables_setVariableTo.png)

```python
new_variable = 5
```

## change variable by

![alt text](/images/blocks/Variables_changeVariableBy.png)

```python
new_variable += 1
```

## global vs local variables

```python
global_variable = 0

def my_function():
    local_variable = 0
    global global_variable
    global_variable += 1
    local_variable += 10
    print(global_variable) # expect 1
    print(local_variable) # expect 10
```

Note: global variables are variables that are defined outside of a function, and can be accessed by any function. Local variables are variables that are defined inside of a function, and can only be accessed by that function. In order to change a global variable inside of a function, you must declare it as global.

## make a list

![alt text](/images/blocks/Lists_makeAList.png)

```python
new_list = []
```

## add to list

![alt text](/images/blocks/Lists_addToList.png)

```python
new_list.append('thing')
print(new_list) # expect ['thing']
```

## delete from list

![alt text](/images/blocks/Lists_deleteFromList.png)

```python
new_list = [1, 2, 3, 4, 5]
new_list.pop(0) # remove the first element
print(new_list) # expect [2, 3, 4, 5]
```

## delete all of

![alt text](/images/blocks/Lists_deleteAllOf.png)

```python
new_list = [1, 2, 3, 4, 5]
new_list.clear()
print(new_list) # expect []
```

## insert at

![alt text](/images/blocks/Lists_insertAt.png)

```python
new_list = [1, 2, 3, 4, 5]
new_list.insert(0, 'thing') # insert 'thing' at index 0 (1st element)
print(new_list) # expect ['thing', 1, 2, 3, 4, 5]
```

## replace item with

![alt text](/images/blocks/Lists_replaceItemWith.png)

```python
new_list = [1, 2, 3, 4, 5]
new_list[0] = 'thing' # replace the first element with 'thing'
print(new_list) # expect ['thing', 2, 3, 4, 5]
```

## item of

![alt text](/images/blocks/Lists_itemOf.png)

```python
new_list = [1, 2, 3, 4, 5]
first_element = new_list[0]
print(first_element) # expect 1
```

## item # of

![alt text](/images/blocks/Lists_itemNumOf.png)

```python
new_list = [1, 2, 'thing', 4, 5]
index_of_thing = new_list.index('thing')
print(index_of_thing) # expect 2
```

## length of

![alt text](/images/blocks/Lists_lengthOf.png)

```python
new_list = [1, 2, 3, 4, 5]
length = len(new_list)
print(length) # expect 5
```

## contains

![alt text](/images/blocks/Lists_contains.png)

```python
new_list = [1, 2, 3, 4, 5]
contains_thing = 'thing' in new_list
print(contains_thing) # expect False
```
