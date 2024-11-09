# Motors

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

1. [run for](#run-for)
2. [go to position (absolute)](#go-to-position-absolute)
3. [go to position (relative)](#go-to-position-relative)
4. [start motor](#start-motor)
5. [stop motor](#stop-motor)
6. [set speed to](#set-speed-to)
7. [power (value)](#power-value)
8. [position (absolute, value)](#position-absolute-value)
9. [position (relative, value)](#position-relative-value)
10. [speed (value)](#speed-value)
11. [set relative position to](#set-relative-position-to)
12. [set motors brake](#set-motors-brake)
13. [set acceleration to](#set-acceleration-to)

## run for

![alt text](/images/blocks/Motors_runFor.png)

### degrees

```python
degree = 360
velocity = 1000
await _motor.run_for_degrees(port.A, degree, velocity)
# not await version
motor.run_for_degrees(port.A, degree, velocity)
```

### rotations

```python
rotations = 2
velocity = 1000
await _motor.run_for_degrees(port.A, rotations * 360, velocity)
# not await version
motor.run_for_degrees(port.A, rotations * 360, velocity)
```

### seconds

```python
miliseconds = 2000
velocity = 1000
await _motor.run_for_time(port.A, miliseconds, velocity)
# not await version
motor.run_for_time(port.A, miliseconds, velocity)
```

## go to position (absolute)

![alt text](/images/blocks/Motors_goToPositionAbsolute.png)

```python
position = 180
velocity = 1000
await _motor.run_to_absolute_position(port.A, position, velocity, direction=motor.SHORTEST_PATH)
# not await version
motor.run_to_absolute_position(port.A, position, velocity, direction=motor.SHORTEST_PATH)
```

possible `direction` values are: `motor.SHORTEST_PATH`, `motor.LONGEST_PATH`, `motor.CLOCKWISE`, `motor.COUNTERCLOCKWISE`

## go to position (relative)

![alt text](/images/blocks/Motors_goToPositionRelative.png)

```python
position = 180
velocity = 1000
await _motor.run_to_relative_position(port.A, position, velocity)
# not await version
motor.run_to_relative_position(port.A, position, velocity)
```

## start motor

![alt text](/images/blocks/Motors_startMotor.png)
![alt text](/images/blocks/Motors_startMotor2.png)

```python
velocity = 1000
motor.run(port.A, velocity)
```

## stop motor

![alt text](/images/blocks/Motors_stopMotor.png)

```python
motor.stop(port.A)
```

## set speed to

![alt text](/images/blocks/Motors_setSpeedTo.png)

It might not get much sense, since we can pass velocity to every motor function, but it is here for completeness:

```python
motor_A_speed = 1000

async def my_func(task_id):
    global motor_A_speed
    motor_A_speed = motor_A_speed * 0.75 # set speed to 75% of initial value

    motor.run(port.A, motor_A_speed) # run motor A with 75% 'gloval' speed
```

You can also store and change speed locally:

```python
async def my_func(task_id):
    motor_A_speed = 750
    motor.run(port.A, motor_A_speed) # run motor A with 75% 'local' speed
```

## power (value)

![alt text](/images/blocks/Motors_powerValue.png)

if you created global variable for motor speed, you can access it like this:

```python
my_new_variable = motor_A_speed
```

## position (absolute, value)

![alt text](/images/blocks/Motors_positionAbsoluteValue.png)

```python
motor.absolute_position(port.A)
```

usage:

```python
position = motor.absolute_position(port.A)
# do something with position variable
```

## position (relative, value)

![alt text](/images/blocks/Motors_positionRelativeValue.png)

```python
motor.relative_position(port.A)
```

## speed (value)

![alt text](/images/blocks/Motors_speedValue.png)

```python
motor.velocity(port.A)
```

## set relative position to

![alt text](/images/blocks/Motors_setRelativePositionTo.png)

```python
motor.reset_relative_position(port.A, 0)
```

## set motors brake

![alt text](/images/blocks/Motors_setMotorsBrake.png)

in python, you can pass `stop` value to almost every motor function, including `motor.stop()`. If you really want, you can also make it global, like in (set speed to)[#set-speed-to] example.

```python
await _motor.run_for_degrees(port.A, 360, 1000, stop=motor.BRAKE)
```

possible `stop` values are: `motor.COAST`, `motor.BREAK`, `motor.HOLD`, `motor.CONTINUE`, `motor.SMART_COAST`, `motor.SMART_BRAKE`

## set acceleration to

![alt text](/images/blocks/Motors_setAccelerationTo.png)

again, in python you can pass `acceleration` value to almost every motor function:

```python
motor.run(port.A, 1000, acceleration=5000)
```

there is also `deceleration` parameter:

```python
motor.run(port.A, 1000, acceleration=5000, deceleration=5000)
```

Possible values are from `0` to `10000` for both `acceleration` and `deceleration`.

Note: besides that `spike app` states, that default is `1000`, it is not true. Default is more like `5000` for both acceleration and deceleration, if you dont pass it.
