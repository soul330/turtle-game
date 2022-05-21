import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.tracer(0)

player = Player()
car_manager = CarManager()

game_screen.listen()
game_screen.onkey(player.move_up, "Up")
game_screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    game_screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    scoreboard = Scoreboard()

    # Detecting collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Decting the crossing
    if player.crossed_the_across():
        player.go_to_start()
        car_manager.next_level()
        scoreboard.increase_level()





game_screen.exitonclick()


