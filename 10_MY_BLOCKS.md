# My Blocks

In word blocks, `My Blocks` are essentially python functions. They allow you to create a block of code that can be reused multiple times.

# Table of contents

1. [Define function](#define-function)
2. [Using function arguments](#using-function-arguments)
3. [Call function](#call-function)

## Async, await

By default, every block created within word blocks is `async` block. This means, that program will wait for the block to finish before continuing to the next block, if there are any functions that are `await`ed within the block.

In python ecosystem, if you create every function as `async`, you have to `await` every function call. This way, if there is anything to wait for inside you function, your program will do it.

However, if you create a function that is not `async`, you have to call it without `await` keyword. Doing so, you will not be able to `await` anything inside the function.

## Define function

![alt text](/images/blocks/MyBlocks_defineFunction.png)

```python
async def my_function(input: int or str, bool_input: bool):
    pass #your code here
```

Labels are not existing in python, in word blocks you can use them to make your code more readable.

However, in python you can be much more strict about what your arguments are expected to be. In the example above, `input` can be either `int` or `str`, and `bool_input` can be only `bool`. If you want to learn more about functions in general, i suggest you to read [this](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

## Using function arguments

![alt text](/images/blocks/MyBlocks_usingFunctionArguments.png)

```python
async def my_function(input: int or str, bool_input: bool):
    if bool_input:
        await _motor.run_for_degrees(port.A, input, 1000)
```

## Call function

![alt text](/images/blocks/MyBlocks_callFunction.png)

```python
await my_function(360, color_sensor.color(port.A) == color.RED)
```
