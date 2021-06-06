def Game(speed: number):
    Chaser.turn(Direction.RIGHT, randint(0, 90))
    Chaser.move(1)
    Chaser.if_on_edge_bounce()
    if Chaser.is_touching_edge():
        game.set_score(game.score() + 1)
    if Chaser.is_touching(player):
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
        MelodyOptions.ONCE)
        game.game_over()
    basic.pause(speed)

def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

player: game.LedSprite = None
Chaser: game.LedSprite = None
game.start_countdown(30000)
Chaser = game.create_sprite(0, 5)
player = game.create_sprite(2, 0)
player.turn(Direction.RIGHT, 90)
player.change(LedSpriteProperty.BRIGHTNESS, 50)

def on_forever():
    if edubitPotentioBit.compare_pot(PotCompareType.MORE_THAN, 800):
        Game(250)
    elif edubitPotentioBit.compare_pot(PotCompareType.MORE_THAN, 400):
        Game(500)
    else:
        Game(750)
basic.forever(on_forever)
