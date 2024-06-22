import time
from colorama import init, Fore

init(autoreset=True)


red_light_first = 0
green_light_first = 0
yellow_light_first = 0


red_light_second = 1
green_light_second = 1
yellow_light_second = 1

# Отображение состояния первого светофора
def display_lights_first():
    if red_light_first:
        print(Fore.RED + "Красный для коров")
    if green_light_first:
        print(Fore.GREEN + "Зелёный для коров")
    if yellow_light_first:
        print(Fore.YELLOW + "Жёлтый")

# Отображение состояния второго светофора
def display_lights_second():
    if red_light_second:
        print(Fore.RED + "Красный для овец")
    if green_light_second:
        print(Fore.GREEN + "Зелёный для овец")
    if yellow_light_second:
        print(Fore.YELLOW + "Жёлтый")


def traffic_lights():
    global red_light_first, green_light_first, yellow_light_first
    global red_light_second, green_light_second, yellow_light_second

    while True:
        red_light_first = 1
        green_light_first = 0
        yellow_light_first = 0
        red_light_second = 0
        green_light_second = 1
        yellow_light_second = 0
        display_lights_first()
        display_lights_second()
        time.sleep(15)


        red_light_first = 0
        green_light_first = 0
        yellow_light_first = 1
        red_light_second = 0
        green_light_second = 0
        yellow_light_second = 1
        display_lights_first()
        display_lights_second()
        time.sleep(5)


        red_light_first = 0
        green_light_first = 1
        yellow_light_first = 0
        red_light_second = 1
        green_light_second = 0
        yellow_light_second = 0
        display_lights_first()
        display_lights_second()
        time.sleep(15)


        red_light_first = 0
        green_light_first = 0
        yellow_light_first = 1
        red_light_second = 0
        green_light_second = 0
        yellow_light_second = 1
        display_lights_first()
        display_lights_second()
        time.sleep(5)


"""Значения переменных: "0" - секция светофора выключена, "1" - секция светофора включена"""

if __name__ == "__main__":
    traffic_lights()