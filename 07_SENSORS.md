# Sensors Blocks

In word blocks, there is a quite big difference of how sensors behave as those azure sensors blocks, compared to yellow events blocks. When you are using them as events trigger, sensor will not retriger the event, until the sensor values changes to falsy and then back to truthy. In sensor block variant, if sensor stays true in for example `while loop`, it will keep triggering the event indefinitely.

In pythonBlocks, you can achieve both behaviors, but here we are going to cover the 'sensor block' variants.

# Table of contents

1. [color sensor is](#color-sensor-is)
2. [color sensor (value)](#color-sensor-value)
3. [color sensor reflection is](#color-sensor-reflection-is)
4. [color sensor reflection (value)](#color-sensor-reflection-value)
5. [color sensor RGBI](#color-sensor-rgbi)
6. [force sensor is](#force-sensor-is)
7. [prassure in](#prassure-in)
8. [distance sensor is](#distance-sensor-is)
9. [distance sensor (value)](#distance-sensor-value)
10. [is tilted](#is-tilted)
11. [when is up](#when-is-up)
12. [when gesture is](#when-gesture-is)
13. [gesture (value)](#gesture-value)
14. [angle (value)](#angle-value)
15. [set yaw angle to 0](#set-yaw-angle-to-0)
16. [acceleration (value)](#acceleration-value)
17. [angular velocity (value)](#angular-velocity-value)
18. [set sensor orientation to](#set-sensor-orientation-to)
19. [orientation (value)](#orientation-value)
20. [is button pressed](#is-button-pressed)
21. [timer (value)](#timer-value)
22. [reset timer](#reset-timer)

## color sensor is

![alt text](/images/blocks/Sensors_colorIs.png)

```python
color_sensor.color(port.A) == color.RED
```

usage:

```python
if color_sensor.color(port.A) == color.RED:
    pass #your code here
```

## color sensor (value)

![alt text](/images/blocks/Sensors_colorValue.png)

```python
color_sensor.color(port.A)
```

usage:

```python
color_variable = color_sensor.color(port.A)
```

## color sensor reflection is

![alt text](/images/blocks/Sensors_colorReflection.png)

```python
color_sensor.reflection(port.A) < 50
```

- You can use any comparison operator [comparison operator](/8_OPERATORS.md/#compare-less-than-equal-greater-than) here.
- Value is in range 0 (black, no light reflected) to 100 (white, all light reflected).

## color sensor reflection (value)

![alt text](/images/blocks/Sensors_colorReflectionValue.png)

```python
color_sensor.reflection(port.A)
```

## color sensor RGBI

![alt text](/images/blocks/Sensors_colorRGBI.png)

There is one more mode, that is not present in word blocks, and that is RGBI mode:

```python
color_sensor.rgbi(port.A)
```

which returns tuple `[red: int, green: int, blue: int, intensity: int]`. So, if you want just `red` value, you can do:

```python
color_sensor.rgbi(port.A)[0]
```

## force sensor is

![alt text](/images/blocks/Sensors_forceIs.png)

### pressed:

```python
force_sensor.pressed(port.A) == 1
```

### released:

```python
force_sensor.pressed(port.A) == 0
```

### hard pressed:

```python
force_sensor.force(port.A) > 50
```

## prassure in

![alt text](/images/blocks/Sensors_forceValue.png)

### percentage:

```python
force_sensor.force(port.A)
```

### newton:

```python
round(force_sensor.force(port.A) / 10)
```

## distance sensor is

![alt text](/images/blocks/Sensors_distanceIs.png)

### closer than:

percentage:

```python
_distanceSensor.distance_percentage(port.A) < 15
```

cm:

```python
_distanceSensor.distance_cm(port.A) < 15
```

inch:

```python
_distanceSensor.distance_inch(port.A) < 15
```

### farther than:

percentage:

```python
_distanceSensor.distance_percentage(port.A) > 15
```

cm:

```python
_distanceSensor.distance_cm(port.A) > 15
```

inch:

```python
_distanceSensor.distance_inch(port.A) > 15
```

### exactly at:

percentage:

```python
_distanceSensor.distance_percentage(port.A) == 15
```

cm:

```python
_distanceSensor.distance_cm(port.A) == 15
```

inch:

```python
_distanceSensor.distance_inch(port.A) == 15
```

## distance sensor (value)

![alt text](/images/blocks/Sensors_distanceValue.png)

### percentage:

```python
_distanceSensor.distance_percentage(port.A)
```

### cm:

```python
_distanceSensor.distance_cm(port.A)
```

### inch:

```python
_distanceSensor.distance_inch(port.A)
```

### mm:

```python
distanceSensor.distance(port.A)
```

## is tilted

![alt text](/images/blocks/Sensors_tilted.png)

### forward:

```python
_motion_sensor.tilt_angles(1) > 130
```

### backward:

```python
_motion_sensor.tilt_angles(1) < -130
```

### right:

```python
_motion_sensor.tilt_angles(2) > 130
```

### left:

```python
_motion_sensor.tilt_angles(2) < -130
```

### tilted (any direction):

```python
_motion_sensor.tilted(0) == True
```

### not tilted (any direction):

```python
_motion_sensor.tilted(0) == False
```

## when is up

note: basically, this is the same as `when tilted *somewhere*`, but breakpoint value is in the middle, which is `450` out of `900` instead of `130`. There is one more option, not covered by `when tilted` which is `when bottom is up`, which you can implement like this:

![alt text](/images/blocks/Sensors_up.png)

```python
_motion_sensor.upside_down(0) == True
```

## when gesture is

![alt text](/images/blocks/Sensors_gesture.png)

### shaken:

```python
motion_sensor.gesture() = motion_sensor.SHAKEN
```

### other gestures:

other possible values are: `motion_sensor.TAPPED`, `motion_sensor.DOUBLE_TAPPED`, `motion_sensor.FALLING` and `motion_sensor.UNKNOWN` which corresponds to 'no gesture'

## gesture (value)

![alt text](/images/blocks/Sensors_gestureValue.png)

```python
motion_sensor.gesture()
```

## angle (value)

![alt text](/images/blocks/Sensors_angleValue.png)

### pitch:

```python
_motion_sensor.tilt_angles(1)
```

### roll:

```python
_motion_sensor.tilt_angles(2)
```

### yaw:

```python
_motion_sensor.tilt_angles(0)
```

## set yaw angle to 0

![alt text](/images/blocks/Sensors_setYaw.png)

```python
motion_sensor.reset_yaw(0)
```

## acceleration (value)

![alt text](/images/blocks/Sensors_accelerationValue.png)

```python
motion_sensor.acceleration(False) # tuple of 3 values
motion_sensor.acceleration(False)[0] # x value
motion_sensor.acceleration(False)[1] # y value
motion_sensor.acceleration(False)[2] # z value
```

pass `True` as argument to get acceleration as raw, unfiltred values

## angular velocity (value)

![alt text](/images/blocks/Sensors_angularVelocityValue.png)

```python
motion_sensor.angular_velocity(False) # tuple of 3 values
motion_sensor.angular_velocity(False)[0] # x value
motion_sensor.angular_velocity(False)[1] # y value
motion_sensor.angular_velocity(False)[2] # z value
```

pass `True` as argument to get angular velocity as raw, unfiltred values

## set sensor orientation to

![alt text](/images/blocks/Sensors_setOrientation.png)

```python
motion_sensor.set_yaw_face(motion_sensor.FRONT)
```

possible values are: `motion_sensor.FRONT`, `motion_sensor.BACK`, `motion_sensor.LEFT`, `motion_sensor.RIGHT`, `motion_sensor.TOP` and `motion_sensor.BOTTOM`

## orientation (value)

![alt text](/images/blocks/Sensors_orientationValue.png)

```python
motion_sensor.get_yaw_face()
```

## is button pressed

![alt text](/images/blocks/Sensors_buttonIs.png)

### left:

pressed:

```python
button.pressed(button.LEFT) > 0
```

released:

```python
button.pressed(button.LEFT) == 0
```

### right:

pressed:

```python
button.pressed(button.RIGHT) > 0
```

released:

```python
button.pressed(button.RIGHT) == 0
```

## timer (value)

![alt text](/images/blocks/Sensors_timerValue.png)

returns time in milliseconds (in word blocks it is in seconds)

```python
timer.get_time_ms()
```

## reset timer

![alt text](/images/blocks/Sensors_resetTimer.png)

```python
timer.reset_timer()
```
