# Events Blocks

Events blocks in word blocks works like this: if event happened, do something on separate thread in parallel. But its not that simple, because those are also waiting for the condition to CHANGE, that means, if the condition stays true, its not going to retriger the instructions. Also, across one stack, its not going to retriger instructions if condition happned to change to true during operations. All that has been taken into account in the following implementations.

If you want to understand how its done, more generic example that is not hidden behind that much of fasade, can be found in this [when block](#when-something) section.

# Table of contents

1. [When program starts](#when-program-starts)
2. [When colour is](#when-colour-is)
3. [When force sensor](#when-force-sensor)
4. [When distance sensor](#when-distance-sensor)
5. [When tilted](#when-tilted)
6. [When is up](#when-is-up)
7. [When gesture is](#when-gesture-is)
8. [When button is](#when-button-is)
9. [When timer reaches](#when-timer-reaches)
10. [When (something)](#when-something)
11. [When i receive message](#when-i-receive-message)
12. [Broadcast message](#broadcast-message)
13. [Broadcast message and wait](#broadcast-message-and-wait)

- [Extras](#extras)
- [API](#api)

## notes:

- task and main_tasks identifiers can be anything, but unique
- if you add task under id that already exists, task is ignored
- if you replace task under id that already exists, task is cancelled then reinvoked
- if you are not going to cancel tasks, you can remove `when_cancelled` and `try/except` part of the implementation

## how to implement:

- all events are implemented the same way, all you have to do is paste one line of code, that is coresponding to desired mode
- [when program starts](#when-program-starts) shows full code implementation

## when program starts

![alt text](/images/blocks/Events_whenProgramStarts.png)

```python
async def my_func(task_id):
    def when_cancelled():
        pass #stop every possible async task here

    try:
        pass #your code
        loop.remove_task(task_id) #remove task when finished (if its finite)
    except asyncio.CancelledError: when_cancelled()

"""invoke task itself in mainLoop funcion"""
async def mainLoop():
    #initial tasks
    loop.add_main_task("when_program_starts", events.when_program_starts('my_func', my_func))

    await loop.run_all_tasks()

asyncio.run(mainLoop())
```

Multiple blocks example:

```python
async def mainLoop():
    #initial tasks
    loop.add_main_task("when_program_starts", events.when_program_starts('my_func', my_func))
    loop.add_main_task("another one", events.when_program_starts('some_stuff', some_function))
    loop.add_main_task("third one", events.when_program_starts('foo', bar))

    await loop.run_all_tasks()

asyncio.run(mainLoop())
```

## when colour is

![alt text](/images/blocks/Events_whenColourIs.png)

```python
loop.add_main_task("when_color_sensor_color", events.when_sensor_is('my_func', my_func, color_sensor.color, port.A, color.RED))
```

`events.when_sensor_is` expects: `task_id`, `function to invoke`, `what sensor to use`, `sensor port`, `expected value`

## when force sensor

![alt text](/images/blocks/Events_whenForceSensor.png)

### pressed:

```python
loop.add_main_task("when_force_sensor_pressed", events.when_sensor_is('my_func', my_func, force_sensor.pressed, port.A, 1))
```

### released:

```python
loop.add_main_task("when_force_sensor_released", events.when_sensor_is('my_func', my_func, force_sensor.pressed, port.A, 0))
```

### hard-pressed:

```python
loop.add_main_task("when_force_sensor_hard_pressed", events.when_sensor_is_more('my_func', my_func, force_sensor.force, port.A, 50))
```

`events.when_sensor_is_more` expects: `task_id`, `function to invoke`, `what sensor to use`, `sensor port`, `expected value`

### pressure changed:

```python
loop.add_main_task("when_force_sensor_pressure_changed", events.when_sensor_changed('my_func', my_func, force_sensor.force, port.A))
```

`events.when_sensor_changed` expects: `task_id`, `function to invoke`, `what sensor to use`, `sensor port`

## when distance sensor

![alt text](/images/blocks/Events_distanceSensor.png)

### closer than:

percentage:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is_less_and_valid('my_func', my_func, _distanceSensor.distance_percentage, port.A, 8))
```

cm:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is_less_and_valid('my_func', my_func, _distanceSensor.distance_cm, port.A, 8))
```

inch:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is_less_and_valid('my_func', my_func, _distanceSensor.distance_inch, port.A, 8))
```

### farther than:

percentage:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is_more('my_func', my_func, _distanceSensor.distance_percentage, port.A, 8))
```

cm:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is_more('my_func', my_func, _distanceSensor.distance_cm, port.A, 8))
```

inch:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is_more('my_func', my_func, _distanceSensor.distance_inch, port.A, 8))
```

### exactly at:

percentage:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is('my_func', my_func, _distanceSensor.distance_percentage, port.A, 8))
```

cm:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is('my_func', my_func, _distanceSensor.distance_cm, port.A, 8))
```

inch:

```python
loop.add_main_task("when_distance_sensor_closer", events.when_sensor_is('my_func', my_func, _distanceSensor.distance_inch, port.A, 8))
```

## when tilted

![alt text](/images/blocks/Events_whenTilted.png)

### forward:

```python
loop.add_main_task("when_tilted_forward", events.when_sensor_is_more('my_func', my_func, _motion_sensor.tilt_angles, 1, 130))
```

### backward:

```python
loop.add_main_task("when_tilted_backward", events.when_sensor_is_less('my_func', my_func, _motion_sensor.tilt_angles, 1, -130))
```

### right:

```python
loop.add_main_task("when_tilted_right", events.when_sensor_is_more('my_func', my_func, _motion_sensor.tilt_angles, 2, 130))
```

### left:

```python
loop.add_main_task("when_tilted_right", events.when_sensor_is_less('my_func', my_func, _motion_sensor.tilt_angles, 2, -130))
```

### tilted (any direction):

```python
loop.add_main_task("when_tilted", events.when_sensor_is('my_func', my_func, _motion_sensor.tilted, 0, True))
```

### not tilted (any direction):

```python
loop.add_main_task("when_not_tilted", events.when_sensor_is('my_func', my_func, _motion_sensor.tilted, 0, False))
```

## when is up

note: basically, this is the same as `when tilted *somewhere*`, but breakpoint value is in the middle, which is `450` out of `900` instead of `130`. There is one more option, not covered by `when tilted` which is `when bottom is up`, which you can implement like this:

![alt text](/images/blocks/Events_whenIsUp.png)

```python
loop.add_main_task("when_bottom_is_up", events.when_sensor_is('my_func', my_func, _motion_sensor.upside_down, 0, True))
```

## when gesture is

![alt text](/images/blocks/Events_whenGestureIs.png)

### shaken:

```python
loop.add_main_task("when_gesture_is", events.when_sensor_is('my_func', my_func, _motion_sensor.gesture, 0, motion_sensor.SHAKEN))
```

### other gestures:

other possible values are: `motion_sensor.TAPPED`, `motion_sensor.DOUBLE_TAPPED`, `motion_sensor.FALLING` and `motion_sensor.UNKNOWN` which corresponds to 'no gesture'

## when button is

![alt text](/images/blocks/Events_whenButtonIs.png)

### left:

pressed:

```python
loop.add_main_task("when_left_button_is_pressed", events.when_sensor_is_more('my_func', my_func, button.pressed, button.LEFT, 0))
```

released:

```python
loop.add_main_task("when_left_button_is_released", events.when_sensor_is('my_func', my_func, button.pressed, button.LEFT, 0))
```

### right:

pressed:

```python
loop.add_main_task("when_right_button_is_pressed", events.when_sensor_is_more('my_func', my_func, button.pressed, button.RIGHT, 0))
```

released:

```python
loop.add_main_task("when_right_button_is_released", events.when_sensor_is('my_func', my_func, button.pressed, button.RIGHT, 0))
```

## when timer reaches

![alt text](/images/blocks/Events_whenTimerIs.png)

```python
loop.add_main_task("when_timer_reaches", events.when_sensor_is_more('my_func', my_func, timer.get_time_ms, 0, 10000))
```

note: `timer.get_time_ms` is a function that returns current time in milliseconds, so you have to set breakpoint in milliseconds as well

## when (something)

![alt text](/images/blocks/Events_whenSomething.png)

```python
loop.add_main_task("when_something", events.when_custom_sensor('my_func', my_func, custom_sensor))
```

Thats a little bit more complicated, and we cannot create a block for every possible combination of sensors and values, so you have to create your own function that will wait till desired measurements/state. In our case, lets try to implement something like this:

![alt text](/images/blocks/Events_whenSomethingExample.png)

How it works in word blocks:

- If its tilted forward `AND` left hub button is pressed, do something
- If `BOTH` of this conditions remain `True` after task is done, do not retrigger the task
- If `ANY` of these conditions change to `False`, and then again both are `True`, retrigger the task

```python
async def custom_sensor():
    #block task thread, if both conditions are met initially,
    #after the program starts or after previous task invoke
    while _motion_sensor.tilt_angles(1) > 130 and button.pressed(button.LEFT) > 0:
        await asyncio.sleep_ms(0)

    #if at least one condition is no longer met, thread is released,
    #and now we can wait for both conditions to be met again:
    while not (_motion_sensor.tilt_angles(1) > 130 and button.pressed(button.LEFT) > 0):
        await asyncio.sleep_ms(0)
```

## when i receive message

![alt text](/images/blocks/Events_whenIReceive.png)

This one is interesting. In this ecosystem, we are not based on messages (events), but we are doing something opposite - we are adding whole tasks to the queue, that is working in parallel. So, instead of waiting for a message, function can be added directly to the queue by another function. Lets try to implement something like this in python blocks:

![alt text](/images/blocks/Events_whenIReceiveExample.png)

```python
async def my_func(task_id):
    def when_cancelled():
        pass #stop every possible async task here

    try:
        pass #your code
        loop.remove_task(task_id) #remove task when finished (if its finite)
    except asyncio.CancelledError: when_cancelled()

async def my_main_func(task_id):
    asyncio.sleep_ms(1000) #wait 1 second
    loop.add_or_replace_task("my_func", my_func("my_func")) #add task to the queue, 'broadcast' message to invoke my_func

async def mainLoop():
    loop.add_main_task("when_program_starts", events.when_program_starts('my_main_func', my_main_func))

    await loop.run_all_tasks()

asyncio.run(mainLoop())
```

### simple implementation

Note:

- if you are not going to cancel tasks, you can remove `when_cancelled` and `try/except` part of the implementation
- if you dont need to remove finite tasks from the queue, you can remove `loop.remove_task(task_id)` line, and also remove `task_id` from `my_func` function arguments

```python
async def my_func():
    pass #your code

async def my_main_func(task_id):
    asyncio.sleep_ms(1000) #wait 1 second
    loop.add_or_replace_task("my_func", my_func()) #add task to the queue, 'broadcast' message to invoke my_func

async def mainLoop():
    loop.add_main_task("when_program_starts", events.when_program_starts('my_main_func', my_main_func))

    await loop.run_all_tasks()

asyncio.run(mainLoop())
```

### one message to trigger multiple tasks

Because how the ecosystem is designed, its not possible to do that. Instead, you can either create task that will invoke multiple functions, or you can simply invoke multiple functions in one task. Here is a simple solution for that:

![alt text](/images/blocks/Events_whenIReceiveExample2.png)

```python
async def my_func():
    pass #your code

async def my_another_function():
    pass #your code

async def my_main_func(task_id):
    asyncio.sleep_ms(1000) #wait 1 second
    loop.add_or_replace_task("my_func", my_func()) #add task to the queue, 'broadcast' message to invoke my_func
    loop.add_or_replace_task("my_another_function", my_another_function()) #both tasks wait for same 'message' so here we are adding second one


async def mainLoop():
    loop.add_main_task("when_program_starts", events.when_program_starts('my_main_func', my_main_func))

    await loop.run_all_tasks()

asyncio.run(mainLoop())
```

### add_task vs add_or_replace_task

In word blocks, when program meets `broadcast block`, every block that is listening to that message is going to be invoked, and if its already running, its going to be `retriggered`. This is why we need to use `add_or_replace_task`, and also why we need to add whole `when_cancelled` and `try/except` part of the implementation. BUT, if you want to change that behaviour, its possible!

- you can manually set what heppens when task is cancelled/retriggered in `when_cancelled` function
- you can use `add_task` instead of `add_or_replace_task` if you want to avoid retriggering tasks, instead letting them finish
- you can programaically add same tasks under differnet `task_id` if you want to multiply the "effect" of the message

## broadcast message

![alt text](/images/blocks/Events_broadcast.png)

```python
loop.add_or_replace_task("my_func", my_func())
```

Refer to [when i receive message](#when-i-receive-message) for more information about how to use this block correctly.

## broadcast message and wait

![alt text](/images/blocks/Events_broadcastAndWait.png)

```python
loop.add_or_replace_task("my_func", my_func("my_func"))
await loop.wait_for("my_func")
```

### wait for multiple tasks

If you are triggering multiple tasks under single 'message', you can wait for all of them to finish by providing list of `task_id`'s:

```python
loop.add_or_replace_task("my_func", my_func("my_func"))
loop.add_or_replace_task("my_another_func", my_another_func("my_another_func"))
await loop.wait_for(["my_func", "my_another_func"])
```

The benefit of having tasks under different `ids` rather under single message is, that you can for example wait for only some of them to finish, or you can wait for them in different order- by waitig for one, do something, then wait for another one.

# Extras

Here you can find some ideas for additional blocks, that cannot be implemented in word blocks, but we can do that in python blocks ;)

## when color sensor has changed

```python
loop.add_main_task("when_color_sensor_color", events.when_sensor_changed_and_valid('my_func', my_func, color_sensor.color, port.A))
```

## when button is pressed for more than x seconds

```python
loop.add_main_task("when_button_pressed_for_1_second", events.when_sensor_is_more('my_func', my_func, button.pressed, button.LEFT, 1000))
```

## more to come

maybe

# API

## events

### when_program_starts

- `task_id` - unique identifier
- `function` - function to invoke

```python
events.when_program_starts(task_id, function)
```

### when_sensor_is

- `task_id` - unique identifier
- `function` - function to invoke
- `sensor` - sensor to use
- `port` - sensor port
- `value` - expected value (exact)

```python
events.when_sensor_is(task_id, function, sensor, port, value)
```

### when_sensor_is_more

- `task_id` - unique identifier
- `function` - function to invoke
- `sensor` - sensor to use
- `port` - sensor port
- `value` - expected value to be more than

```python
events.when_sensor_is_more(task_id, function, sensor, port, value)
```

### when_sensor_is_less

- `task_id` - unique identifier
- `function` - function to invoke
- `sensor` - sensor to use
- `port` - sensor port
- `value` - expected value to be less than

```python
events.when_sensor_is_less(task_id, function, sensor, port, value)
```

### when_sensor_is_less_and_valid

- `task_id` - unique identifier
- `function` - function to invoke
- `sensor` - sensor to use
- `port` - sensor port
- `value` - expected value to be less than and valid (not -1)

```python
events.when_sensor_is_less_and_valid(task_id, function, sensor, port, value)
```

### when_sensor_changed

- `task_id` - unique identifier
- `function` - function to invoke
- `sensor` - sensor to use
- `port` - sensor port

this method stores previous value of the sensor internally, and if it changes, it invokes the function

```python
events.when_sensor_changed(task_id, function, sensor, port)
```

### when_sensor_changed_and_valid

- `task_id` - unique identifier
- `function` - function to invoke
- `sensor` - sensor to use
- `port` - sensor port

this method stores previous value of the sensor internally, and if it changes, it invokes the function, but only if the value is valid (not -1)

```python
events.when_sensor_changed_and_valid(task_id, function, sensor, port)
```

### when_custom_sensor

- `task_id` - unique identifier
- `function` - function to invoke
- `custom_sensor` - custom function that waits for desired measurements/state, see [when (something)](#when-something) for more information

```python
events.when_custom_sensor(task_id, function, custom_sensor)
```

## loop

### add_main_task

- `task_id` - unique identifier
- `coroutine` - reference to the main task

if task under `task_id` already exists, program will raise an error

```python
loop.add_main_task(task_id, coroutine)
```

### add_task

- `task_id` - unique identifier
- `coroutine` - reference to the main task

if task under `task_id` already exists, it is going to be ignored
if task under `task_id` already exists as main_task, program will raise an error

```python
loop.add_task(task_id, coroutine)
```

### add_or_replace_task

- `task_id` - unique identifier
- `coroutine` - reference to the main task

if task under `task_id` already exists, it is going to be cancelled and reinvoked
this will also execute `when_cancelled` function if it exists under exception block
if task under `task_id` already exists as main_task, program will raise an error

```python
loop.add_or_replace_task(task_id, coroutine)
```

### remove_task

- `task_id` - unique identifier

if task under `task_id` already exists as main_task, program will raise an error

```python
loop.remove_task(task_id)
```

### cancel_task

- `task_id` - unique identifier

this will remove task AND execute `when_cancelled` function if it exists under exception block
if task under `task_id` already exists as main_task, program will raise an error

```python
loop.cancel_task(task_id)
```

### wait_for

- `task_id` - unique identifier

single task:

```python
await loop.wait_for(task_id)
```

multiple tasks:

```python
await loop.wait_for([task_id1, task_id2])
```

### run_all_tasks

thats the main loop, that is running all tasks in parallel, that needs to be added at the end of the main function

```python
await loop.run_all_tasks()
```
