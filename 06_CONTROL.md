# Control Blocks

# Table of Contents

1. [wait x seconds](#wait-x-seconds)
2. [repeat x times](#repeat-x-times)
3. [forever](#forever)
4. [if then](#if-then)
5. [if, else](#if-else)
6. [if, else if, else (nested)](#if-else-if-else-nested)
7. [wait until](#wait-until)
8. [repeat until](#repeat-until)
9. [stop other stacks](#stop-other-stacks)
10. [stop](#stop)

## wait x seconds

![alt text](/images/blocks/Control_waitSeconds.png)

block thread for x milliseconds

```python
await asyncio.sleep_ms(1000)
```

## repeat x times

![alt text](/images/blocks/Control_repeat.png)

```python
for i in range(10):
    pass #your code here
```

## forever

![alt text](/images/blocks/Control_forever.png)

```python
while True:
    pass #your code here
```

## if then

![alt text](/images/blocks/Control_if.png)

```python
if True: #your condition here instead of True
    pass #your code here
```

## if, else

![alt text](/images/blocks/Control_ifElse.png)

```python
if True: #your condition here instead of True
    pass #your code here
else:
    pass #your code here
```

### if, else if, else (nested)

```python
if True: #your condition here instead of True
    pass #your code here
elif False: #your condition here instead of False
    pass #your code here
    #you can have as many elif as you want, each with a new condition
else:
    pass #your code here
    #you can have only one or none else statement
```

## wait until

![alt text](/images/blocks/Control_waitUntil.png)

```python
while True: #your condition here instead of True
    await asyncio.sleep_ms(0)
```

## repeat until

![alt text](/images/blocks/Control_repeatUntil.png)

```python
while True: #your condition here instead of True
    pass #your code here
```

## stop other stacks

![alt text](/images/blocks/Control_stopOtherStacks.png)

```python
loop.cancel_all_except(task_id)
```

`task_id` is the id of the task that you want to keep running, which in this case is the task that called this function.
You can pass `string` or list of `string` as `task_id`. You can also call that function without any argument to stop all tasks, but keep in mind that you have to do that from main task, otherwise it will raise an exception and exit the program by trying to cancel itself.

## stop

![alt text](/images/blocks/Control_stop.png)

### this stack

```python
loop.remove_task(task_id) #remove task from task queue
when_cancelled() #execute when_cancelled (if defined)
return #exit function
```

note: we cannot use loop.cancel_task(task_id) here, because calling it inside the function that we want to cancel will raise an exception and exit the program

### all

if called from main task:

```python
loop.cancel_all_except() #no argument, cancel all tasks
```

if called from other (non-main) tasks:

```python
loop.cancel_all_except(task_id) #cancel all tasks except the one that called this function
loop.remove_task(task_id) #remove task from task queue
when_cancelled() #execute when_cancelled (if defined)
return #exit function
```

### and exit program

```python
raise SystemExit
```
