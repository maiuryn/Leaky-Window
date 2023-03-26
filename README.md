<h1>Leaky Window</h1>

## Inspiration
We wanted to build a small project that we could use to learn a little bit about computer vision. We thought about ways to incorporate it and were inspired by some of the simple games made using pygame.

## What it does
The goal of the game is for the player to cover up the leaking holes that appear on the screen. If the screen fills up with water, the game is over. The player's score is determined by the amount of time that they can last before the screen fills up.

## How we built it
We used python as our language of choice. We chose to use pygame as the game's engine and opencv to track hand movements on the webcam.

## Challenges we ran into
We couldn't test the program on multiple devices because of the lack of multiple webcams. We worked around this by assigning a small task to work on and to check back in once we finished that task.

## Accomplishments that we're proud of
We had an issue where the output visual of the webcam would show a different position from where the holes on the screen were, and we fixed it by mirroring and shifting the tracking position.

## What we learned
We were able to learn about how pygame's graphics engine works, and how to implement a computer vision model that could track movements. We also figured out how to track and update values that are updated on a frame by frame basis. This was a completely different way of thinking than the kinds of programs that we wrote before.
## What's next for Leaky window
We want to add additional modes and features that will make the game a lot more fun to play.
Here are some of the ideas that we had in mind:
- Adding a difficulty select menu
- Making the game restart after it ends
- Adding creatures and plants to distract and hinder the player
