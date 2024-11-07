# Light Blocks

# Table of Contents

1. [turn on for seconds](#turn-on-for-seconds)
2. [turn on](#turn-on)
3. [write](#write)
4. [turn off pixels](#turn-off-pixels)
5. [set pixel brightness to](#set-pixel-brightness-to)
6. [set pixel at to](#set-pixel-at-to)
7. [rotate](#rotate)
8. [set orientation](#set-orientation)
9. [set Centre Button Light to](#set-centre-button-light-to)
10. [distance sensor light up](#distance-sensor-light-up)
11. [color matrix turn on for seconds](#color-matrix-turn-on-for-seconds)
12. [color matrix turn on](#color-matrix-turn-on)
13. [color matrix turn off pixels](#color-matrix-turn-off-pixels)
14. [color matrix set pixel brightness to](#color-matrix-set-pixel-brightness-to)
15. [color matrix set pixel at to](#color-matrix-set-pixel-at-to)
16. [color matrix rotation](#color-matrix-rotation)

## turn on for seconds

![alt text](/images/blocks/Light_turnOnFor.png)

It will light up all the lights for 1 second.

```python
await _light_matrix.show([100] * 25, 1000)
```

Approach, that uses extra `.prepare_image` method, which will transform easy to visualize list into list that can be used by `show` method.

```python
image=[
    [9,9,9,9,9],
    [7,7,7,7,7],
    [5,5,5,5,5],
    [3,3,3,3,3],
    [1,1,1,1,1],
]

await _light_matrix.show(_light_matrix.prepare_image(image), 2000)
```

Note: in this approach, in our `image` we are using values from 0 (off) to 9 (full brightness)

### smily face example:

```python
image=[
    [9,9,0,9,9],
    [9,9,0,9,9],
    [0,0,0,0,0],
    [9,0,0,0,9],
    [0,9,9,9,0],
]
```

### built in images

```python
await _light_matrix.show_image(light_matrix.IMAGE_HEART, 2000)
```

## turn on

![alt text](/images/blocks/Light_turnOn.png)

```python
light_matrix.show([100] * 25)
```

note: you can also use `_light_matrix.prepare_image()` method to prepare image here

### built in images

```python
light_matrix.show_image(light_matrix.IMAGE_HEART)
```

## write

![alt text](/images/blocks/Light_write.png)

```python
await _light_matrix.write('Hello')
```

- optional, second parameter is `light intensity`, which is set to 100 by default
- optional, third parameter is `time_per_character` which is set to 500 by default

## turn off pixels

![alt text](/images/blocks/Light_turnOffPixels.png)

```python
light_matrix.clear()
```

## set pixel brightness to

![alt text](/images/blocks/Light_setPixelBrightnessTo.png)

What it does in word blocks, is setting brightness of all pixels to be multiplied by given percentage in subsequent blocks. You can replicate this behaviour with this utility method:

```python
prepared_image = _light_matrix.prepare_image(image)
dimmed_image = _light_matrix.scale_pixels(prepared_image, 50) # 50% brightness

light_matrix.show(dimmed_image)
```

## set pixel at to

![alt text](/images/blocks/Light_setPixelAtTo.png)

```python
light_matrix.set_pixel(0, 0, 100)
```

rembemer, that we are using 0 for first row and first column and 4 for last row and last column (as apposed to 1-5 in word blocks)

## rotate

![alt text](/images/blocks/Light_rotate.png)

### right

```python
_light_matrix.rotate_right()
```

### left

```python
_light_matrix.rotate_left()
```

## set orientation

![alt text](/images/blocks/Light_setOrientation.png)

```python
light_matrix.set_orientation(orientation.UP)
```

possible values are: `orientation.UP`, `orientation.DOWN`, `orientation.LEFT`, `orientation.RIGHT`

## set Centre Button Light to

![alt text](/images/blocks/Light_setCentreButtonLightTo.png)

```python
light.color(0, color.RED)
```

to turn off the light, pass 0 as color argument

you can also change bluetooth light color!

```python
light.color(1, color.RED)
```

## distance sensor light up

![alt text](/images/blocks/Light_distanceSensorLightUp.png)

```python
distance_sensor.show(port.A, [100]*4)
```

second parameter is list of 4 values, that will be used to light up the individual lights on the distance sensor. Those values are from 0 to 100

you can also light up individual light on the distance sensor with `.show_pixel` method, get given light value with `.get_pixel` method and clear the lights with `.clear` method

## color matrix turn on for seconds

![alt text](/images/blocks/Light_colorMatrixTurnOnFor.png)

```python
await _color_matrix.show(port.A, [(color.RED, 10)] * 9, 2000)
```

second parameter is list of `[color, brightness]` pairs, for all 9 lights on the color matrix. Brightness is from 0 (off) to 10 (full brightness)

## color matrix turn on

![alt text](/images/blocks/Light_colorMatrixTurnOn.png)

```python
color_matrix.show(port.A, [(color.RED, 10)] * 9)
```

## color matrix turn off pixels

![alt text](/images/blocks/Light_colorMatrixTurnOffPixels.png)

```python
color_matrix.clear(port.A)
```

## color matrix set pixel brightness to

![alt text](/images/blocks/Light_colorMatrixSetPixelBrightnessTo.png)

What it does in word blocks, is setting brightness of all pixels to be multiplied by given percentage in subsequent blocks. You can replicate this behaviour with this utility method:

```python
pixels = [(color.RED, 10)] * 9
dimmed_pixels = _color_matrix.scale_pixels(pixels, 50) # 50% brightness

color_matrix.show(port.A, dimmed_pixels)
```

## color matrix set pixel at to

![alt text](/images/blocks/Light_colorMatrixSetPixelAtTo.png)

```python
color_matrix.set_pixel(port.A, 0, 0, (color.RED, 10))
```

## color matrix rotation

![alt text](/images/blocks/Light_colorMatrixRotation.png)

`color_matrix` does not provide any utilities for its orientation and rotation, so in order to not complicate the pythonBlocks API to much, ive just created two utility methods, that will rotate list of 9 elements, that represent the lights on the color matrix right or left:

### right

```python
_color_matrix.rotate_right(list_of_9_color_tuples)
```

### left

```python
_color_matrix.rotate_left(list_of_9_color_tuples)
```

i dont think that there is a need for more complex rotation methods, but its possible to achieve (with .get_pixel, internal class memory and every color_matrix method abstracted inside color_matrix_class, that is going to use that data), maybe i'll add them in the future ;)
