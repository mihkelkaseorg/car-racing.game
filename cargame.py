import os
import csv
from time import sleep
import time
from track import track_1
from track import track_2
from car import car_1
from car import car_2
from datetime import datetime
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def clear():
    _ = os.system("cls")


def start_race():
    start = round(time.time(), ndigits=2)
    time.sleep(1)
    track_1.length.insert(0, car_1.symbol)
    track_2.length.insert(0, car_2.symbol)
    for i in range(len(track_1.length)):
        current_position = track_1.length.index(car_1.symbol)
        current_position_2 = track_2.length.index(car_2.symbol)
        next_position = current_position + car_1.acceleration
        next_position_2 = current_position_2 + car_2.acceleration
        track_1.length.pop(current_position)
        track_2.length.pop(current_position_2)
        track_1.length.insert(next_position, car_1.symbol)
        track_2.length.insert(next_position_2, car_2.symbol)
        print(*track_1.length, sep="")
        print(*track_2.length, sep="")
        sleep(1)
        if track_1.length[17] == car_1.symbol and track_2.length[17] == "|":
            clear()
            end = round(time.time(), ndigits=2)
            time_1 = end - start
            print(f"Car 1 won with the time: {time_1}\nRace Finished!")
            with open("score-board.csv", 'a', newline="") as f:
                writer = csv.writer(f)
                writer.writerow([f"{car_1.mark} won race with the time: {time_1} at {date} against {car_2.mark}"])
            break
        elif track_2.length[17] == "O" and track_1.length[17] == "|":
            clear()
            end = round(time.time(), ndigits=2)
            time_1 = end - start
            print(f"Car 2 won with the time: {time_1}\nRace Finished!")
            with open("score-board.csv", 'a', newline="") as f:
                writer = csv.writer(f)
                writer.writerow([f"{car_2.mark} won race with the time: {time_1} at {date} against {car_1.mark}"])
            break
        elif car_1.symbol == track_1.length[17] and car_2.symbol == track_2.length[17]:
            clear()
            end = round(time.time(), ndigits=2)
            time_1 = end - start
            print(f"TIE between car 1 and car 2 with the time: {time_1}!\nRace Finished!")
            with open("score-board.csv", 'a', newline="") as f:
                writer = csv.writer(f)
                writer.writerow([f"There was a tie between {car_1.mark} and {car_2.mark}"
                                 f" with the time: {time_1} at {date}"])
            break


while True:
    clear()
    print("==========WELCOME TO THE==============NEED FOR SPEED TERMINAL RACE==========================")
    sleep(1)
    option = input("""Choose the option (type option number)
    1 - Start race
    2 - See score-board
    3 - Quit the game
    Enter option here: """)
    if option == "1":
        while True:
            print(f"""
            WELCOME! ENJOY WATCHING THE RACE!
            X is a {car_1.color} {car_1.mark} and it is driving on track {car_1.track}
            O is a {car_2.color} {car_2.mark} and it is driving on track {car_2.track}
            """)
            sleep(2)
            print("The race starts in: ")
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
            sleep(1)
            print("GO!")
            start_race()
            another = input("Would you like to watch another race? (yes/no): ")
            if another == "yes":
                track_1.length = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
                track_2.length = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
                continue
            if another == "no":
                break
            else:
                print("wrong input")
                break

    elif option == "2":
        with open("score-board.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    elif option == "3":
        quit()
    else:
        print("wrong input")

    while True:
        want_more = input("Do you want to continue? (yes/no): ")
        if want_more == "yes":
            track_1.length = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
            track_2.length = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
            break
        elif want_more == "no":
            quit()
        else:
            print("Invalid Input")
            continue