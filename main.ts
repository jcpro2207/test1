function Game (speed: number) {
    Chaser.turn(Direction.Right, randint(0, 90))
    Chaser.move(1)
    Chaser.ifOnEdgeBounce()
    if (Chaser.isTouchingEdge()) {
        game.setScore(game.score() + 1)
    }
    if (Chaser.isTouching(player)) {
        music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
        game.gameOver()
    }
    basic.pause(speed)
}
input.onButtonPressed(Button.A, function () {
    player.move(-1)
})
input.onButtonPressed(Button.B, function () {
    player.move(1)
})
let player: game.LedSprite = null
let Chaser: game.LedSprite = null
game.startCountdown(30000)
Chaser = game.createSprite(0, 5)
player = game.createSprite(2, 0)
player.turn(Direction.Right, 90)
player.set(LedSpriteProperty.Brightness, 50)
basic.forever(function () {
    if (edubitPotentioBit.comparePot(PotCompareType.MoreThan, 800)) {
        Game(250)
    } else if (edubitPotentioBit.comparePot(PotCompareType.MoreThan, 400)) {
        Game(500)
    } else {
        Game(750)
    }
})
