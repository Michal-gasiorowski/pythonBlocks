"""
This is example program, that shows overcomplicated way to comunicate events between threads, with events/flags combination.

After countdown, program waits for 1-10 seconds to show lights + sound, then waits for button left or right button press

If user pressed button in time, the time is shown on the light matrix and the game restarts.

If user pressed the button too early, the sad face is shown and the game restarts.
"""

# paste pythonBlocks library here

"""#####################"""
"""#  YOUR CODE HERE   #"""
"""#####################"""

# global flags
is_game_running = False
waiting_for_input = False

#count down and set is_game_running to True
async def start_game(task_id):
    light.color(0, 0)
    light.color(1, 0)
    light_matrix.write('3')
    await asyncio.sleep_ms(1000)
    light_matrix.write('2')
    await asyncio.sleep_ms(1000)
    light_matrix.write('1')
    await asyncio.sleep_ms(1000)
    light_matrix.clear()

    loop.remove_task(task_id)
    # launch actual game
    loop.add_task('the_game', the_game('the_game'))

# actual game
async def the_game(task_id):  
    # when ended up prematurely, do this
    def when_cancelled():
        light.color(0, color.RED)
        light_matrix.show_image(light_matrix.IMAGE_SAD)
        print('game lost!')
    
    try:
        global is_game_running, waiting_for_input

        timer.reset_timer()
        is_game_running = True
        randomTime = random.randint(1000,9999)
        
        # wait untill timer reaches randomTime
        while timer.get_time_ms() < randomTime:
            await asyncio.sleep_ms(0)

        # enable 'win' inputs
        waiting_for_input = True
        
        # reset timer to measure time reaction
        timer.reset_timer()
        
        # show some indications, that we are waiting for user input
        light_matrix.show([100]*25)
        _sound.noteSync(60, 99999, 100)

        # this task can be removed
        loop.remove_task(task_id)
    except asyncio.CancelledError: when_cancelled()
    
async def stop_game(task_id):
    global is_game_running, waiting_for_input
    
    # react only if game is running
    if is_game_running:
        # show win_screen if program reaches randomTime
        if waiting_for_input:
            loop.add_task('win', win_screen('win', timer.get_time_ms()))
        # if stopped too early, show loose_screen
        else:
            loop.add_task('loose', loose_screen('loose'))
    
    # task is done, can be removed
    loop.remove_task(task_id)

# show time after winning and restart the game
async def win_screen(task_id, time):
    _sound.stop()
    light.color(0, color.GREEN)
    await _light_matrix.write(str(time))
    await asyncio.sleep_ms(1000)
    restart()
    loop.remove_task(task_id)

# show loose screen and restart the game
async def loose_screen(task_id):
    loop.cancel_task('the_game')
    await _sound.note(60, 500, 100)
    await asyncio.sleep_ms(500)
    await _sound.note(60, 500, 100)
    await asyncio.sleep_ms(500)
    restart()
    loop.remove_task(task_id)

# restart game helper
def restart():
    global is_game_running, waiting_for_input
    is_game_running = False
    waiting_for_input = False
    loop.add_or_replace_task("start_game_task", start_game("start_game_task"))

"""#####################"""
"""# DEFINE MAIN TASKS #"""
"""#####################"""

async def mainLoop():
    # start the game
    loop.add_main_task("main_task", events.when_program_starts('start_game_task', start_game))
    # add watcher for both buttons
    loop.add_main_task('wait_for_right_button', events.when_sensor_is_more('stop', stop_game, button.pressed, button.RIGHT, 0 ))
    loop.add_main_task('wait_for_left_button', events.when_sensor_is_more('stop', stop_game, button.pressed, button.LEFT, 0 ))

    await loop.run_all_tasks()

asyncio.run(mainLoop())