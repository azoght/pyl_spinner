# Press Your Luck!
![](https://img.shields.io/badge/made%20with-pygame%20v2.0dev6-yellowgreen)

<div style="text-align:center"><img src="https://vignette.wikia.nocookie.net/gameshows/images/9/94/Press_Your_Luck_2019_Logo.png/revision/latest?cb=20190510203222" alt="Press Your Luck Logo: https://vignette.wikia.nocookie.net/gameshows/images/9/94/Press_Your_Luck_2019_Logo.png/revision/latest?cb=20190510203222" width="450" height="300"/></div>


A pygame program that behaves like the classic 80s game show "Press Your Luck" (which was rebooted again in 2019).

---
## How to play

Click "Start Spin", wait, and click "Stop Spin" when you think you've landed on your lucky prize!

This game uses **the power of random** to generate prizes. Land on a blue square and you win some money, but land on a *whammy* and your money goes down to zero! Like the original game's rules say, if you get four Whammies, your game stops. "Game over!" will be printed on the console.

The number of spins you get in a game is also random (unlike the original game where you answer questions to earn spins) and your spin count will show up on screen. You can hack this by changing the spins variable in main.py.

Because I had problems with toggling while coding this project, there are two seperate buttons to start and stop spinning.

The final prize of the game in dollars won't be printed on the pygame window, but rather on the Python console.

---
## Random number generation system based on probability

When landing on a blue square, the minimum prize is $1000 and the maximum prize is $1000000 (a __million__ dollars!).

The random prize generation system works in a way that you have a bigger chance of winning smaller amounts of money, as well as a 25% chance of getting a whammy.

To do this, the handy-dandy random number generator outputs a number between 1 and 1000 many times a second, until the stop button is clicked. If the output is 750, the reward will be set to a million. If less, the reward will be 1000 minimum and 500000 maximum. If more, a Whammy is generated! Here's the full function:
```python
def spinReward() -> int:
    r = random.randint(1,1000)
    if r >= 1 and r <= 369:
        return 1000
    if r >= 370 and r <= 559:
        return 2000
    if r >= 560 and r <= 659:
        return 2500
    if r >= 660 and r <= 704:
        return 5000
    if r >= 705 and r <= 725:
        return 10000
    if r >= 725 and r <= 734:
        return 20000
    if r >= 735 and r <= 739:
        return 25000
    if r >= 740 and r <= 743:
        return 50000
    if r >= 744 and r <= 745:
        return 100000
    if r >= 746 and r <= 747:
        return 250000
    if r >= 748 and r <= 749:
        return 500000
    if r == 750:
        return 1000000
    else:
        return 0
```
### BONUS: Whammy GIF!

Unlike the original, only one Whammy animation is used: a GIF I borrowed from the Internet, but must give David Frangioso the credit for (Frangioso is behind all the Whammy art I've inserted to this program).

I made a function that plays this Whammy GIF, really quickly:

```python
def playGif(frames: [], frame: int, x: int, y: int):
    global s
    s = False
    fn = "files/ezgif-2-890a93be7cdd-gif-im/" + frames[frame][0]
    img = pg.image.load(fn)
    for a in range(frames[frame][1] * 50):
        window.blit(img, (x,y))
    s = True
```
*Note: pg is my nickname for the pygame package in this program.*

## All you need is Pygame!
The *random* package is built-in, so the only package you'll need to download to run this program sucessfully is *pygame*. To install through terminal:
```bash
pip install pygame 2.0.0.dev6
```

---
#### Who's ready to _press their luck_? Try playing along with the game when it airs Sunday nights @ 9.
