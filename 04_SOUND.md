# Sound

In python, you really can only use 'beep' sound, so we are not going to cover many of word blocks in this section, since those are part of spike app and not the hub itself.

# Table of contents

1. [play beep for seconds](#play-beep-for-seconds)
2. [play beep for seconds (in hz)](#play-beep-for-seconds-in-hz)
3. [start playing beep](#start-playing-beep)
4. [start playing beep (in hz)](#start-playing-beep-in-hz)
5. [stop all sounds](#stop-all-sounds)
6. [volume](#volume)

## play beep for seconds

![alt text](/images/blocks/Sound_playBeepFor.png)

```python
await _sound.note(60, 200, 100)
```

required parameters: (`note`: int = 60, `duration`: int = 500, `volume`: int = 100)

- duration is in milliseconds
- note is in midi note format
- volume is in percentage

## play beep for seconds (in hz)

```python
await _sound.beep(440, 200, 100)
```

required parameters: (`frequency`: int = 440, `duration`: int = 500, `volume`: int = 100)

## start playing beep

![alt text](/images/blocks/Sound_startBeep.png)
![alt text](image.png)

```python
_sound.noteSync(60, 99999999, 100)
```

there is no infinite duration for beep, so we are using a very large number instead

## start playing beep (in hz)

```python
sound.beep(440, 99999999, 100)
```

there is no infinite duration for beep, so we are using a very large number instead

## stop all sounds

![alt text](/images/blocks/Sound_stopAllSounds.png)

```python
_sound.stop()
```

You can also use `sound.stop()` instead, but its very buggy: it hangs the hub when invoked in quick succession.

## volume

![alt text](/images/blocks/Sound_setVolume.png)

I dont really se a point in using this, since you can set volume in every sound block, but if you really want to implement this, here is how:

```python
sound_volume = 100

async def my_func(task_id):
    global sound_volume
    sound_volume = 50 # set volume to 50%
    sound_volume += 10 # increase volume by 10%

    _sound.note(60, 200, sound_volume) # play sound with new 'global' volume
```

You can also store volume in variable locally:

```python
async def my_func(task_id):
    sound_volume = 100
    sound_volume = 50 # set volume to 50%
    sound_volume += 10 # increase volume by 10%

    _sound.note(60, 200, sound_volume) # play sound with new 'local' volume
```
