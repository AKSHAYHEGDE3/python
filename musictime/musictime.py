from pygame import mixer
from datetime import datetime
from time import time

def music(file,stop_it):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stop_it:
            mixer.music.stop()
            break

def log(msg):
    with open("anime.txt","a") as op:
        op.write(f"{msg}{datetime.now()}\n")


initial_time_n=time()
initial_time_bc=time()
initial_time_aot=time()
naruto_time=30
bc_time=150
aot_time=300

while True:
    if time() - initial_time_n > naruto_time:
        print("start watching naruto and if finished type watchedn")
        music("naruto.mp3","watchedn")
        initial_time_n=time()
        log("watched naruto at ")

    if time() - initial_time_bc > bc_time:
        print("start watching black clover and if finished type watchedbc")
        music("black clover.mp3","watchedbc")
        initial_time_bc=time()
        log("watched black clover at ")

    if time() - initial_time_aot > aot_time:
        print("start watching aot and if finished type watchedaot")
        music("aot.mp3","watchedaot")
        initial_time_aot=time()
        log("watched aot at ")

        
