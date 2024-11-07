"""
This is example program, that shows overcomplicated way to comunicate events between threads, with events/flags combination.

When rate exceeds 2000ms or goes below 0ms, the heart stops beating and the sad face is shown.

Them, you can restart the heart by pressing any hub button.
"""

# paste pythonBlocks library here

"""#####################"""
"""#  YOUR CODE HERE   #"""
"""#####################"""

interval = 1000
has_finished = False

# engage beat event and wait for interval before trying to engage it again
# if interval is not in range, show sad face and play sound
# because we are completely removing this function when its not needed, 
# we dont have to do any 'await asyncio.sleep_ms(0)' magic here, to unblock other threads!
async def count_interval(task_id):
    global has_finished

    while True:
            if 0 < interval < 2000:
                loop.add_or_replace_task('beat', heart_beat('beat'))
                await asyncio.sleep_ms(interval)
            elif not has_finished:
                has_finished = True
                _sound.noteSync(60, 9999999, 100)
                light_matrix.show_image(light_matrix.IMAGE_SAD)
                loop.remove_task(task_id)
                return

# show heart image and play sound
# its dependent on caoun_interval function, so there is no logic needed here
async def heart_beat(task_id):
    global interval
    try:
        light_matrix.show_image(light_matrix.IMAGE_HEART)
        await _sound.note(60, round(interval / 2), 100)
        light_matrix.show_image(light_matrix.IMAGE_HEART_SMALL)
        loop.remove_task(task_id)

    except asyncio.CancelledError: pass

# restart the heart helper funcion
async def restart():
    global interval, has_finished

    light_matrix.clear()
    _sound.stop()
    await asyncio.sleep_ms(1500)

    # reset the interval and flag
    interval = 1000
    has_finished = False
    # adding main game loop task back when needed!
    loop.add_task('game_loop', count_interval('game_loop'))

# increment and decrement interval by 100
# those two are constantly watching for button press, so there is no need for any logic here
# flag has_finished is used to prevent from changing interval while heart is stopped
# if heart is stopped, it will restart it by calling restart function
async def increment(task_id):
    global has_finished, interval
    if not has_finished:
        interval += 100
    else:
        await restart()
    loop.remove_task(task_id)

async def decrement(task_id):
    global has_finished, interval
    if not has_finished:
        interval -= 100
    else:
        await restart()
    loop.remove_task(task_id)

"""#####################"""
"""# DEFINE MAIN TASKS #"""
"""#####################"""

async def mainLoop():
    # adding count_interval task to main loop
    loop.add_main_task("main_task", events.when_program_starts('game_loop', count_interval))
    # adding increment and decrement tasks to main loop
    loop.add_main_task('when_right_button', events.when_sensor_is('inc', increment, button.pressed, button.RIGHT, 0))
    loop.add_main_task('when_left_button', events.when_sensor_is('dec', decrement, button.pressed, button.LEFT, 0))

    # all those task are running in the main loop constantly and cannot be cancelled or removed
    # its equivalent of 'Events' block in word blocks
    await loop.run_all_tasks()

asyncio.run(mainLoop())