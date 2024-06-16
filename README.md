# blackjack_simulator

This blackjack simulator uses relatively basic python code to simulate a player playing the optimal strategy for a game of blackjack. This particular code assumes that the blackjack game is following these rules:
- There is an infinite number of cards (we do not assume a finite number of decks)
- The dealer stands on soft 17
- A blackjack pays 3 to 2 (unless the player split aces)
- The player can double
- The player can split equal cards as many times as they'd like
- The player can only split aces once, and can only receive one additional card for each ace
- The player cannot surrender
- The player plays the *optimal strategy*
- The player bets $10 per hand

The code has been seperated into the following 4 python files:
- **blackjack_functions.py**: This is where all the necessary functions are created, such as the logic behind splitting cards, how to receive an extra card, etc.
- **blackjack_simulation.py**: This simply ties in together all the black jack functions into one massive function that simulates 1 hand of blackjack
- **blackjack_multiple_simulations.py**: This enables us to run the black_simulation file as many times as we'd like
- **analysis.py**: This takes the csv files that were generated in the previous file and allows us to run our analyses and plot graphs.

## How can anyone run this code?

If you are interested in running this code, there are a few modifications that you'll need to do.

In the **blackjack_multiple_simulations.py** file between lines 42 to 48, you'll have to uncomment those lines and save them as whatever you'd like. This will save the simulation that you ran in a csv file so that you can analyze it in the next step.

Once the above is done, go to the **analysis.py** file and change the file path names in lines 7 to 10 with the file path of the csv files that were just generated. This will allow you to actually do the necessary analyses.

## Check out the article posted on hashnode!

Feel free to check out my analysis on mathieutorchia.com, where I explain the logic behind the code as well as the insights gained from it.
