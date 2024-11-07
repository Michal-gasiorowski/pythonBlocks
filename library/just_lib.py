import asyncio
import motor
import motor_pair
from hub import button, sound, light_matrix, motion_sensor, light, port
import distance_sensor
import color_matrix
import force_sensor
import color
import orientation
import math
import random

async def dummyTask():
    timer.reset_timer()
    while True:
        await asyncio.sleep_ms(9999999)

class timerClass():
    def __init__(self):
        self.initial = None
    def get_time_ms(self, notUsed = None):
        return asyncio.ticks() - self.initial
    def reset_timer(self):
        self.initial = asyncio.ticks()
timer = timerClass()

class task_manager:
    def __init__(self):
        self.tasks = {}
        self.main_tasks = {}
        self.add_main_task('system_init', dummyTask())
    def add_main_task(self, task_id, coroutine):
        if task_id in self.main_tasks:
            raise ValueError("that main task already exist")    
        task = asyncio.create_task(coroutine)
        self.main_tasks[task_id] = task
    def add_task(self, task_id, coroutine):
        if task_id in self.main_tasks:
            raise ValueError("cannot add task under id that already existis in main tasks")
        if not task_id in self.tasks:
            task = asyncio.create_task(coroutine)
            self.tasks[task_id] = task
    def add_or_replace_task(self, task_id, coroutine):
        if task_id in self.main_tasks:
            raise ValueError("cannot add task under id that already existis in main tasks")
        if task_id in self.tasks:
            self.remove_task(task_id)
        task = asyncio.create_task(coroutine)
        self.tasks[task_id] = task
    def cancel_task(self, task_id):
        if task_id in self.main_tasks:
            raise ValueError("cannot remove main task")
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.cancel()
            del self.tasks[task_id]
    def cancel_all_except(self, task_ids_to_keep=None):
        if task_ids_to_keep is None:
            task_ids_to_keep = []
        elif isinstance(task_ids_to_keep, str):
            task_ids_to_keep = [task_ids_to_keep]
        tasks_to_cancel = [task_id for task_id in self.tasks if task_id not in task_ids_to_keep]
        for task_id in tasks_to_cancel:
            self.cancel_task(task_id)
    def remove_task(self, task_id):
        if task_id in self.main_tasks:
            raise ValueError("cannot remove main task")
        if task_id in self.tasks:
            del self.tasks[task_id]
    async def wait_for(self, task_ids):
        if isinstance(task_ids, str):
            task_ids = [task_ids]
        tasks_to_wait = [self.tasks[task_id] for task_id in task_ids if task_id in self.tasks]
        if tasks_to_wait:
            await asyncio.gather(*tasks_to_wait)
    async def run_all_tasks(self):
        all_tasks = list(self.tasks.values()) + list(self.main_tasks.values())
        await asyncio.gather(*all_tasks)
loop = task_manager()

def midi_to_hz(midi_note):
    frequency = 440 * 2 ** ((midi_note - 69) / 12)
    return round(frequency)
class sound_class():
    async def beep(self, frequency: int = 440, duration: int = 500, volume: int = 100, *, attack: int = 0, decay: int = 0, sustain: int = 100, release: int = 0, transition: int = 10, waveform: int = sound.WAVEFORM_SINE, channel: int = sound.DEFAULT):
        sound.beep(frequency, duration, volume, attack=attack, decay=decay, sustain=sustain, release=release, transition=transition, waveform=waveform, channel=channel)
        await asyncio.sleep_ms(duration)
    async def note(self, note: int = 60, duration: int = 500, volume: int = 100, *, attack: int = 0, decay: int = 0, sustain: int = 100, release: int = 0, transition: int = 10, waveform: int = sound.WAVEFORM_SINE, channel: int = sound.DEFAULT):
        sound.beep(midi_to_hz(note), duration, volume, attack=attack, decay=decay, sustain=sustain, release=release, transition=transition, waveform=waveform, channel=channel)
        await asyncio.sleep_ms(duration)
    def noteSync(self, note: int = 60, duration: int = 500, volume: int = 100, *, attack: int = 0, decay: int = 0, sustain: int = 100, release: int = 0, transition: int = 10, waveform: int = sound.WAVEFORM_SINE, channel: int = sound.DEFAULT):
        sound.beep(midi_to_hz(note), duration, volume, attack=attack, decay=decay, sustain=sustain, release=release, transition=transition, waveform=waveform, channel=channel)
    def stop(self):
        sound.beep(0,0,0)
_sound = sound_class()

async def wait_for_motor(port, *, extra: int = 0, skip = False):
    if skip:
        return
    if(extra > 0):
        await asyncio.sleep_ms(extra)  
    while motor.get_duty_cycle(port) == 0:
        await asyncio.sleep_ms(0)
    while not motor.get_duty_cycle(port) == 0:
        await asyncio.sleep_ms(0) 
class motor_class():
    def hold(self, choosen_stop, port):
        if choosen_stop == motor.HOLD:
            #motor.run_for_degrees(port, 0, 0, stop=motor.HOLD)
            motor.stop(port, stop=motor.HOLD)
    def filter_hold(self, choosen_stop):
        return choosen_stop if choosen_stop != motor.HOLD else motor.BRAKE
    async def run_for_time(self, port: int, duration: int, velocity: int, *, stop: int = motor.BRAKE, acceleration: int = 5000, deceleration: int = 5000):
        motor.stop(port)
        motor.run_for_time(port, duration, velocity, stop=self.filter_hold(stop), acceleration=acceleration, deceleration=deceleration)
        await wait_for_motor(port, extra=20)
        self.hold(stop, port)
    async def run_for_degrees(self, port: int, degrees: int, velocity: int, *, stop: int = motor.SMART_BRAKE, acceleration: int = 5000, deceleration: int = 5000):
        motor.stop(port)
        motor.run_for_degrees(port, degrees, velocity, stop=self.filter_hold(stop), acceleration=acceleration, deceleration=deceleration)
        await wait_for_motor(port, extra=20)
        self.hold(stop, port)
    async def run_to_absolute_position(self, port: int, position: int, velocity: int, *, direction: int, stop: int = motor.SMART_BRAKE, acceleration: int = 5000, deceleration: int = 5000):
        motor.stop(port)
        motor.run_to_absolute_position(port, position, velocity, direction=direction, stop=self.filter_hold(stop), acceleration=acceleration, deceleration=deceleration)
        await wait_for_motor(port, skip=motor.absolute_position(port) == position, extra=20)
        self.hold(stop, port)
    async def run_to_relative_position(self, port: int, position: int, velocity: int, *, stop: int = motor.SMART_BRAKE, acceleration: int = 5000, deceleration: int = 5000):
        motor.stop(port)
        motor.run_to_relative_position(port, position, velocity, stop=self.filter_hold(stop), acceleration=acceleration, deceleration=deceleration)
        await wait_for_motor(port, skip=motor.relative_position(port) == position, extra=20)
        self.hold(stop, port)
    def stop(self, port: int, *, stop: int = motor.BRAKE):
        motor.stop(port, stop=stop)   
_motor = motor_class()

class motor_pair_class():
    def __init__(self):
        self.pairs = [[0,0]]*3
        self.cm_per_360_deg = 0
        self.inch_per_360_deg = 0
    def hold(self, choosen_stop, pair):
        if choosen_stop == motor.HOLD:
            motor_pair.stop(pair, stop=motor.HOLD)
    def filter_hold(self, choosen_stop):
        return choosen_stop if choosen_stop != motor.HOLD else motor.BRAKE
    def pair(self, pair: int, left_motor: int, right_motor: int):
        motor_pair.pair(pair, left_motor, right_motor)
        self.pairs[pair] = [left_motor, right_motor]
    async def move_for_degrees(self, pair: int, degrees: int, steering: int, *, velocity: int = 180, stop: int = motor.BRAKE, acceleration: int = 2000, deceleration: int = 2000):
        motor_pair.stop(pair)
        motor_pair.move_for_degrees(pair, degrees, steering, velocity=velocity, stop=self.filter_hold(stop), acceleration=acceleration, deceleration=deceleration)
        await wait_for_motor(self.pairs[pair][0], extra=5)
        self.hold(stop, pair)
    async def move_for_time(self, pair: int, duration: int, steering: int, *, velocity: int = 180, stop: int = motor.BRAKE, acceleration: int = 2000, deceleration: int = 2000):
        motor_pair.stop(pair)
        motor_pair.move_for_time(pair, duration, steering, velocity=velocity, stop=self.filter_hold(stop), acceleration=acceleration, deceleration=deceleration)
        await wait_for_motor(self.pairs[pair][0], extra=5)
        self.hold(stop, pair)
    async def move_tank_for_degrees(self, pair: int, degrees: int, left_velocity: int, right_velocity: int, *, stop: int = motor.BRAKE, acceleration: int = 2000, deceleration: int = 2000):
        motor_pair.stop(pair)
        motor_pair.move_tank_for_degrees(pair, degrees, left_velocity, right_velocity, stop=self.filter_hold(stop), acceleration=acceleration, deceleration=deceleration)
        await wait_for_motor(self.pairs[pair][0], extra=5)
        self.hold(stop, pair)
    async def move_tank_for_time(self, pair: int, left_velocity: int, right_velocity: int, duration: int, *, stop: int = motor.BRAKE, acceleration: int = 2000, deceleration: int = 2000):
        motor_pair.stop(pair)
        motor_pair.move_tank_for_time(pair, left_velocity, right_velocity, duration, stop=self.filter_hold(stop), acceleration=acceleration, deceleration=deceleration)
        await wait_for_motor(self.pairs[pair][0], extra=5)
        self.hold(stop, pair)
    def cm_to_degrees(self, cm):
        return round((cm / self.cm_per_360_deg) * 360)
    def inch_to_degrees(self, inch):
        return round((inch / self.inch_per_360_deg) * 360)
    def set_cm_per_360_deg(self, cm):
        self.cm_per_360_deg = cm
    def set_inch_per_360_deg(self, inch):
        self.inch_per_360_deg = inch

_motor_pair = motor_pair_class()

class color_matrix_class():
    async def show(self, port: int, pixels: list[tuple[int, int]], duration: int):
        color_matrix.show(port, pixels)
        await asyncio.sleep_ms(duration)
        color_matrix.clear(port)
    def rotate_right(self, grid):
        face = [grid[i:i+3] for i in range(0, 9, 3)]
        rotated_face = [list(row) for row in zip(*face[::-1])]    
        return [item for row in rotated_face for item in row]
    def rotate_left(self, grid):
        face = [grid[i:i+3] for i in range(0, 9, 3)]
        rotated_face = [list(row) for row in list(zip(*face))[::-1]]
        return [item for row in rotated_face for item in row]
    def scale_pixels(self, pixels: list[tuple[int, int]], intensity: int):
        return [(x, round(y * intensity / 100)) for x, y in pixels]
_color_matrix = color_matrix_class()

class light_matrix_class():
    async def wait_for_light_matrix(self):
        def checkIfEmpty():
            for x in range(5):
                for y in range(5):
                    if light_matrix.get_pixel(x, y) != 0:
                        return False
            return True
        while not checkIfEmpty():
            await asyncio.sleep_ms(0)
        while checkIfEmpty():
            await asyncio.sleep_ms(0)
        while not checkIfEmpty():
            await asyncio.sleep_ms(0)
    async def write(self, text: str, intensity: int = 100, time_per_character: int = 500):
        light_matrix.write(text, intensity, time_per_character)
        await self.wait_for_light_matrix()
    async def show(self, pixels: list[int], duration: int):
        light_matrix.show(pixels)
        await asyncio.sleep_ms(duration)
        light_matrix.clear()
    async def show_image(self, image: int, duration: int):
        light_matrix.show_image(image)
        await asyncio.sleep_ms(duration)
        light_matrix.clear()
    def rotate_right(self):
        current_orientation = light_matrix.get_orientation()
        light_matrix.set_orientation(current_orientation + 1) if current_orientation < 3 else light_matrix.set_orientation(0)
    def rotate_left(self):
        current_orientation = light_matrix.get_orientation()
        light_matrix.set_orientation(current_orientation + -1) if current_orientation > 0 else light_matrix.set_orientation(3)
    def prepare_image(self, pixels: list[list[int]]):
        return [((pixel + 1) * 10) if pixel != 0 else 0 for pixel in sum(image, [])]
    def scale_pixels(self, pixels: list[int], intensity):
        return [round(pixel * intensity / 100) for pixel in pixels]
_light_matrix = light_matrix_class()

class waitClass:
    async def to_be(self, sensor, port, expected_value):
        while sensor(port) == expected_value:
            await asyncio.sleep_ms(0)
        while not sensor(port) == expected_value:
            await asyncio.sleep_ms(0)
    async def to_be_more(self, sensor, port, expected_value):
        while sensor(port) > expected_value:
            await asyncio.sleep_ms(0)
        while not sensor(port) > expected_value:
            await asyncio.sleep_ms(0)
    async def to_be_less(self, sensor, port, expected_value):
        while sensor(port) < expected_value:
            await asyncio.sleep_ms(0)
        while not sensor(port) < expected_value:
            await asyncio.sleep_ms(0)
    async def to_be_less_and_valid(self, sensor, port, expected_value):
        while sensor(port) < expected_value or sensor(port) == -1:
            await asyncio.sleep_ms(0)
        while not sensor(port) < expected_value or sensor(port) == -1:
            await asyncio.sleep_ms(0)
    async def to_not_be(self, sensor, port, expected_value):
        while sensor(port) == expected_value:
            await asyncio.sleep_ms(0)
    async def to_not_be_and_valid(self, sensor, port, expected_value):
        while sensor(port) == expected_value or sensor(port) == -1:
            await asyncio.sleep_ms(0)
wait = waitClass()

class eventsClass():
    def __init__(self):
        self.saved_values = [None] * 6
    async def when_program_starts(self, task_id, coroutine):
        loop.add_task(task_id, coroutine(task_id))
    async def when_custom_sensor(self, task_id, coroutine, sensor):
        while True:
            await sensor()
            loop.add_task(task_id, coroutine(task_id))
    async def when_sensor_is(self, task_id, coroutine, sensor, _port, value):
        while True:
            await wait.to_be(sensor, _port, value)
            loop.add_task(task_id, coroutine(task_id))
    async def when_sensor_is_more(self, task_id, coroutine, sensor, _port, value):
        while True:
            await wait.to_be_more(sensor, _port, value)
            loop.add_task(task_id, coroutine(task_id))
    async def when_sensor_is_less(self, task_id, coroutine, sensor, _port, value):
        while True:
            await wait.to_be_less(sensor, _port, value)
            loop.add_task(task_id, coroutine(task_id))
    async def when_sensor_is_less_and_valid(self, task_id, coroutine, sensor, _port, value):
        while True:
            await wait.to_be_less(sensor, _port, value)
            loop.add_task(task_id, coroutine(task_id))
    async def when_sensor_changed(self, task_id, coroutine, sensor, _port):
        if(self.saved_values[_port] == None):
            self.saved_values[_port] = sensor(_port)
        while True:
            await wait.to_not_be(sensor, _port, self.saved_values[_port])
            self.saved_values[_port] = sensor(_port)
            loop.add_task(task_id, coroutine(task_id))
    async def when_sensor_changed_and_valid(self, task_id, coroutine, sensor, _port):
        if(self.saved_values[_port] == None):
            self.saved_values[_port] = sensor(_port)
        while True:
            await wait.to_not_be_and_valid(sensor, _port, self.saved_values[_port])
            self.saved_values[_port] = sensor(_port)
            loop.add_task(task_id, coroutine(task_id))
events = eventsClass()

class distanceSensorClass():
    def distance_cm(self, port):
        distance = distance_sensor.distance(port)
        return round(distance / 10) if distance != -1 else -1
    def distance_inch(self, port):
        distance = distance_sensor.distance(port)
        return round(distance * 3.93701) if distance != -1 else -1
    def distance_percentage(self, port):
        distance = distance_sensor.distance(port)
        return round(distance / 2) if distance != -1 else -1
_distanceSensor = distanceSensorClass()

class motionSensorClass():
    def tilt_angles(self, index):
        return motion_sensor.tilt_angles()[index]
    def tilted(self, _notUsed):
        tilts = motion_sensor.tilt_angles()
        return tilts[1] < -130 or tilts[1] > 130 or tilts[2] < -130 or tilts[2] > 130
    def upside_down(self, _notUsed):
        tilts = motion_sensor.tilt_angles()
        return (tilts[2] > 1350 or tilts[2] < -1350) and (tilts[1] > -450 and tilts[1] < 450)
    def gesture(self, _notUsed):
        return motion_sensor.gesture()
    def stable(self, _notUsed):
        return motion_sensor.stable()
_motion_sensor = motionSensorClass()