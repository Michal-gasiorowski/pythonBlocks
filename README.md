![alt text](/images/logo.png)

# pythonBlocks

Small library that allows to implement word blocks functionality within python in lego spike hub v3

# Features

- It covers all the blocks from the official lego spike app
- You have to add ~150 lines of minified code to your project and you are ready
- It hides all the complexity of the hub/sensor/motors/events interactions and allows you to focus on the logic
- It adds some abstractions, that are needed to implement the word blocks in python without any additional code
- It works with spike hub v3, no need to install any additional software/firmware on the hub, downgrade or hack anything
- Documentation shows every block from the official app, and how to implement it in pythonBlocks
- It imports everything that you probably need, so you don't have to worry about it
- It might be good for educational purposes, as it translates the blocks from the official app to python code

# Installation

1. Copy the content of [full_program_minified.py](/library/full_program_minified.py) to your project
2. Done

If you want to use un-minified version, you can copy the content of [full_program.py](/library/full_program.py) instead. Its over 300 lines of code, but if you want to understand how it works, extend it or modify it, it will be easier to read.

You can allways minify it back afterwords, using some online minifier, like [this one](https://python-minifier.com/)

# Blocks documentation

1. [Motors](/01_MOTORS.md)
2. [Movement](/02_MOVEMENT.md)
3. [Light](/03_LIGHT.md)
4. [Sound](/04_SOUND.md)
5. [Events](/05_EVENTS.md)
6. [Control](/06_CONTROL.md)
7. [Sensors](/07_SENSORS.md)
8. [Operators](/08_OPERATORS.md)
9. [Variables and lists](/09_VARIABLES_AND_LISTS.md)
10. [My Blocks](/10_MY_BLOCKS.md)

# Example programs

1. [Reflex game](/examples/reflexGame.py)
2. [Heart beat](/examples/heartBeat.py)

more to come ;)

# Table of contents

1. [Usage](#usage)
2. [asyncio and await](#asyncio-and-await)
3. [other underscored methods](#other-underscored-methods)
4. [What next / contributing](#what-next--contributing)
5. [Change log](#change-log)

# Usage

After you copied the code to your project, you can start using it right away. Lets see how actual program looks like:

```python
"""#####################"""
"""#  YOUR CODE HERE   #"""
"""#####################"""

async def my_func(task_id):
    def when_cancelled():
        pass #stop every possible async task here

    try:
        pass #your code here
        loop.remove_task(task_id) #remove task from the queue (if its finite)

    except asyncio.CancelledError: when_cancelled()

"""#####################"""
"""# DEFINE MAIN TASKS #"""
"""#####################"""

async def mainLoop():
    loop.add_main_task("main_task", events.when_program_starts('task_1', my_func))

    await loop.run_all_tasks()

asyncio.run(mainLoop())
```

Thats the basic structure of the program. How its different from the official app?

- We are using asyncio library to handle async tasks instead of runloop, due to its limitations
- If we want to use all functionalities, we have to define `when_cancelled` function inside every function, that is going to be used as task
- We also have to use `try/except` block to catch `asyncio.CancelledError` exception, and call `when_cancelled` function inside it
- We need to use `loop.remove_task(task_id)` to remove the task from the queue, if its finite (otherwise, it will be not possible to call it again once its finished)

## asyncio and await

Some methods that are native to Spike hub v3, like `motor.run_for_degrees` or `motor.run_to_relative_position` can be `awaited`. The problem is, that its not working with `asyncio` - instead, lego is using its own `runloop` to handle async tasks of their own. In order to make it work with `asyncio`, we have call `underscored` variants of those methods, like `_motor.run_for_degrees` or `_motor.run_to_relative_position` every time we need to await for it.

```python
async def my_func(task_id):
    def when_cancelled():
        motor.stop(port.A) #stop motor A when task is cancelled. We don't need to use underscored version of motor.stop, since its not awaited
        print("task cancelled")

    try:
        await _motor.run_for_degrees(port.A, 360, 1000) #underscored version of motor.run_for_degrees, that can be awaited
        print("task finished")
        loop.remove_task(task_id) #remove task from the queue after its finished

    except asyncio.CancelledError: when_cancelled() #call when_cancelled function when task is cancelled
```

## other underscored methods

There are also other underscored methods, that are created not to be awaited, but to extend the functionality and creates some boilerplate code implementation for you. Refer to the block documentation to see how to use them.

# What next / contributing

I probably might add some other abstractions, that goes beyond the official app, depending on the feedback. If you have any suggestions, feel free to create an issue or a pull request.

# Change log

- 0.0.1 - Initial beta release
