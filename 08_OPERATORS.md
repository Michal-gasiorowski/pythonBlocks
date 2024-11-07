# Operators

# Table of contents

1. [random](#random)
2. [basic math (add, subtract, multiply, divide)](#basic-math-add-subtract-multiply-divide)
3. [compare (less than, equal, greater than)](#compare-less-than-equal-greater-than)
4. [logic (and, or, not)](#logic-and-or-not)
5. [is 0 in between -10 and 10 ?](#is-0-in-between--10-and-10-)
6. [join apple and banana](#join-apple-and-banana)
7. [letter 1 of apple](#letter-1-of-apple)
8. [length of apple](#length-of-apple)
9. [apple contains a ?](#apple-contains-a-)
10. [mod (remainder of division aka modulo)](#mod-remainder-of-division-aka-modulo)
11. [round](#round)
12. [advanced math](#advanced-math)

## pick random between 1 and 10

![alt text](/images/blocks/Operators_random.png)

```python
import random

random.randint(1, 10)
```

usage:

```python
random_number = random.randint(1, 10)
# random_number will be a random number between 1 and 10
# you can use this number in your code
```

### random boolean

```python
import random

random.choice([True, False])
```

### random from list

```python
import random

list = [1, 2, 3, 4, 5]
random.choice(list)
```

## basic math (add, subtract, multiply, divide)

![alt text](/images/blocks/Operators_math.png)

### add

```python
a + b
```

### subtract

```python
a - b
```

### multiply

```python
a * b
```

### divide

```python
a / b
```

## compare (less than, equal, greater than)

![alt text](/images/blocks/Operators_compare.png)

### less than

```python
a < b
```

### equal

```python
a == b
```

### greater than

```python
a > b
```

not available in word blocks:

### less than or equal

```python
a <= b
# in word blocks you have to use:
not a > b
```

### greater than or equal

```python
a >= b
# in word blocks you have to use:
not a < b
```

### not equal

```python
a != b
# in word blocks you have to use:
not a == b
```

## logic (and, or, not)

![alt text](/images/blocks/Operators_logic.png)

### and

```python
a and b
```

### or

```python
a or b
```

### not

```python
not a
```

example usage of logic operators:

```python
if my_variable == 1 and my_sensor() == 5:
    pass #your code here

if my_variable == 'foo' or my_sensor() == -1:
    pass #your code here

if not my_variable == 1:
    pass #your code here
```

## is 0 in between -10 and 10 ?

![alt text](/images/blocks/Operators_inBetween.png)

```python
-10 < 0 < 10
```

example usage:

```python
if -10 < my_variable < 10:
    pass #your code here
```

## join apple and banana

![alt text](/images/blocks/Operators_join.png)

```python
'apple' + 'banana'
#expected output: 'applebanana'
```

example usage:

```python
time = '15'
unit = ' seconds'

time_string = time + unit
#time_string will be '15 seconds'
```

joining numbers with strings:

```python
number = 15
unit = ' seconds'

time_string = str(number) + unit
#time_string will be '15 seconds'
```

## letter 1 of apple

![alt text](/images/blocks/Operators_letterOf.png)

if you don't know already, in programming, the first element of a list or anything that can be indexed is at position 0, not 1 ;):

```python
'apple'[0]
#expected output: 'a'
```

example usage:

```python
fruit = 'apple'
first_letter = fruit[0]
#first_letter will be 'a'
```

## length of apple

![alt text](/images/blocks/Operators_length.png)

```python
len('apple')
#expected output: 5
```

example usage:

```python
fruit = 'apple'
fruit_length = len(fruit)
#fruit_length will be 5
```

## apple contains a ?

![alt text](/images/blocks/Operators_contains.png)

```python
'a' in 'apple'
#expected output: True
```

example usage:

```python
fruit = 'apple'
if 'a' in fruit:
    pass #your code here
```

more typical usage:

```python
my_list = ['apple', 'banana', 'cherry']
if 'banana' in my_list:
    pass #your code here
```

## mod (remainder of division aka modulo)

![alt text](/images/blocks/Operators_mod.png)

```python
a % b
```

example usage:

```python
remainder = 10 % 3
#remainder will be 1
```

## round

![alt text](/images/blocks/Operators_round.png)

```python
round(3.14159)
#expected output: 3
```

example usage:

```python
pi = 3.14159
rounded_pi = round(pi)
#rounded_pi will be 3
```

## advanced math

![alt text](/images/blocks/Operators_advancedMath.png)

Note: there is a lot more stuff in the math module, you can check the [official documentation](https://docs.python.org/3/library/math.html) for more information.
And i think, that some might be quite useful for robotics, like `math.isclose()` for comparing floating point numbers or just inaccuracy of sensors :)

### abs (absolute value)

```python
abs(-5)
#expected output: 5
```

### floor (round down)

```python
import math

math.floor(3.9)
#expected output: 3
```

### ceiling (round up)

```python
import math

math.ceil(3.1)
#expected output: 4
```

### sqrt (square root)

```python
import math

math.sqrt(16)
#expected output: 4.0
```

### sin (sine)

```python
import math

math.sin(math.pi / 2)
#expected output: 1.0
```

### cos (cosine)

```python
import math

math.cos(0)
#expected output: 1.0
```

### tan (tangent)

```python
import math

math.tan(math.pi / 4)
#expected output: ...0.9999999999999999 ;) but it's 1.0
```

### asin (arc sine)

```python
import math

math.asin(1)
#expected output: 1.5707963267948966
```

### acos (arc cosine)

```python
import math

math.acos(1)
#expected output: 0.0
```

### atan (arc tangent)

```python
import math

math.atan(1)
#expected output: 0.7853981633974483
```

### ln (natural logarithm)

```python
import math

math.log(2.718281828459045)
#expected output: 1.0
```

### log (base 10 logarithm)

```python
import math

math.log10(100)
#expected output: 2.0
```

### e^ (exponential)

```python
import math

math.exp(1)
#expected output: 2.718281828459045
```

### 10^ (exponential base 10)

```python
import math

math.pow(10, 2)
#expected output: 100.0
```
