# Movement

## Pairing

In word blocks, you can only set one pair of motors to become `movement motors`. In python, you can have three separate pairs, and pass them to `motor_pair` methods each time as argument.

IMPORTANT: if you want to `await _underscore` stuff works here, you have to pair your motors with `_motor_pair.pair()` (underscored) method!

## Velocities:

Value ranges depends on motor type:

- Small motor (essential): `-660` to `660`
- Medium motor: `-1110` to `1110`
- Large motor: `-1050` to `1050`

## Direction:

- If degrees are positive, motor will rotate clockwise, if negative, counter clockwise.
- If velocity is positive, motor will rotate forward, if negative, backward.
- So, having both values negative will cancel each other out and motor will move clockwise.

# Table of contents

1. [set movement motors to](#set-movement-motors-to)
2. [set 1 motor rotation to](#set-1-motor-rotation-to)
3. [move for](#move-for)
4. [start moving](#start-moving)
5. [move direction for](#move-direction-for)
6. [start moving direction](#start-moving-direction)
7. [stop moving](#stop-moving)
8. [set movement speed to](#set-movement-speed-to)
9. [set movement motors brake](#set-movement-motors-brake)
10. [set movement acceleration to](#set-movement-acceleration-to)
11. [start moving at speed (tank)](#start-moving-at-speed-tank)

## set movement motors to

![alt text](/images/blocks/Movement_setMovementMotorsTo.png)

```python
_motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
```

first argument is pair number (0, 1 or 2 or `motor_pair.PAIR_1`, `motor_pair.PAIR_2` or `motor_pair.PAIR_3`), second and third are ports of motors.

## set 1 motor rotation to

![alt text](/images/blocks/Movement_setMotorRotationTo.png)

### cm

```python
_motor_pair.set_cm_per_360_deg(17.5)
```

### inch

```python
_motor_pair.set_inch_per_360_deg(6.9)
```

## move for

![alt text](/images/blocks/Movement_moveFor.png)

### degrees

```python
degree = 360
velocity = 1000
await _motor_pair.move_for_degrees(motor_pair.PAIR_1, degree, 0, velocity=velocity)
# not await version
motor_pair.move_for_degrees(motor_pair.PAIR_1, degree, 0, velocity=velocity)
```

### rotations

```python
rotations = 10
velocity = 1000
await _motor_pair.move_for_degrees(motor_pair.PAIR_1, rotations * 360, 0, velocity=velocity)
# not await version
motor_pair.move_for_degrees(motor_pair.PAIR_1, rotations * 360, 0, velocity=velocity)
```

### seconds

```python
duration = 2000
velocity = 1000
await _motor_pair.move_for_time(motor_pair.PAIR_1, duration, 0, velocity=velocity)
# not await version
motor_pair.move_for_time(motor_pair.PAIR_1, duration, 0, velocity=velocity)
```

### cm

```python
cm = 100
velocity = 1000
await _motor_pair.move_for_degrees(motor_pair.PAIR_1, _motor_pair.cm_to_degrees(cm), 0, velocity=velocity)
# not await version
motor_pair.move_for_degrees(motor_pair.PAIR_1, _motor_pair.cm_to_degrees(cm), 0, velocity=velocity)
```

note: you have to set proper value first with `_motor_pair.set_cm_per_360_deg()` method

### inch

```python
inch = 10
velocity = 1000
await _motor_pair.move_for_degrees(motor_pair.PAIR_1, _motor_pair.inch_to_degrees(inch), 0, velocity=velocity)
# not await version
motor_pair.move_for_degrees(motor_pair.PAIR_1, _motor_pair.inch_to_degrees(inch), 0, velocity=velocity)
```

note: you have to set proper value first with `_motor_pair.set_inch_per_360_deg()` method

## start moving

![alt text](/images/blocks/Movement_startMoving.png)

```python
motor_pair.move(motor_pair.PAIR_1, 0)
```

if you want to move backward, set velocity to negative value

```python
motor_pair.move(motor_pair.PAIR_1, velocity= -1000)
```

## move direction for

![alt text](/images/blocks/Movement_moveDirectionFor.png)

Thats the same as [move for](#move-for), but with direction parameter set not to 0:

```python
rotations = 10
velocity = 1000
steering = 30
await _motor_pair.move_for_degrees(motor_pair.PAIR_1, rotations * 360, steering, velocity=velocity)
# not await version
motor_pair.move_for_degrees(motor_pair.PAIR_1, rotations * 360, 0, velocity=velocity)
```

`steering` parameter is a value from `-100` to `100`, where `-100` is full left, `0` is straight and `100` is full right.

## start moving direction

![alt text](/images/blocks/Movement_startMovingDirection.png)

thats the same as [start moving](#start-moving), but with direction parameter set not to 0:

```python
motor_pair.move(motor_pair.PAIR_1, 30)
```

`steering` parameter is a value from `-100` to `100`, where `-100` is full left, `0` is straight and `100` is full right.

## stop moving

![alt text](/images/blocks/Movement_stopMoving.png)

```python
motor_pair.stop(motor_pair.PAIR_1)
```

## set movement speed to

![alt text](/images/blocks/Movement_setMovementSpeedTo.png)

It might not get much sense, since we can pass velocity to every motor function, but it is here for completeness:

```python
pair_1_speed = 1000

async def my_func(task_id):
    global pair_1_speed
    pair_1_speed = pair_1_speed * 0.75 # set speed to 75% of initial value
    await _motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0, velocity=pair_1_speed)
```

You can also store and change speed locally:

```python
async def my_func(task_id):
    pair_1_speed = 750
    await _motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0, velocity=pair_1_speed)
```

## set movement motors brake

![alt text](/images/blocks/Movement_setMovementMotorsBrake.png)

in python, you can pass stop value to almost every motor function, including motor.stop(). If you really want, you can also make it global, like in (set speed to)[#set-speed-to] example.

```python
await _motor_pair.run_for_degrees(motor_pair.PAIR_1, 360, 1000, stop=motor.BRAKE)
```

possible `stop` values are: `motor.COAST`, `motor.BREAK`, `motor.HOLD`, `motor.CONTINUE`, `motor.SMART_COAST`, `motor.SMART_BRAKE`

## set movement acceleration to

![alt text](/images/blocks/Movement_setMovementAccelerationTo.png)

again, in python you can pass `acceleration` value to almost every motor function:

```python
await _motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0, velocity=1000, acceleration=5000)
```

there is also `deceleration` parameter:

```python
await _motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0, velocity=1000, acceleration=5000, deceleration=5000)
```

## start moving at speed (tank)

![alt text](/images/blocks/Movement_startMovingAtSpeed.png)

```python
left_velocity = 1000
right_velocity = -1000
motor_pair.move_tank(motor_pair.PAIR_1, left_velocity, right_velocity)
```

There is also `move_tank_for_degrees` and `move_tank_for_time` methods, not available in word blocks, that works the same as `move_for_degrees` and `move_for_time`, but for tank movement:

### degrees

```python
degree = 360
left_velocity = 1000
right_velocity = -1000
await _motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degree, left_velocity, right_velocity)
# not await version
motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, degree, left_velocity, right_velocity)
```

### seconds

```python
duration = 2000
left_velocity = 1000
right_velocity = -1000
await _motor_pair.move_tank_for_time(motor_pair.PAIR_1, duration, left_velocity, right_velocity)
# not await version
motor_pair.move_tank_for_time(motor_pair.PAIR_1, duration, left_velocity, right_velocity)
```
