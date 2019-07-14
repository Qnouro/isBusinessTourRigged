# Is Business Tour Rigged ?

# Table of Contents
1. [About](#About)
2. [Theory](#Theory)
3. [Results](#Results)
4. [Conclusion](Conclusion)

## About

Business Tour is a free monopoly-like, and many people find that the game is scripted & not random.

The game board being small, it might be the reason people feel that it is rigged.

This repo aims to check the dice rolls and verify if the game is rigged or not.

## Theory

In order to check if the game is rigged, we are going to study the dice rolls. We are hence testing $H=H_0$ against $H = H_1$ where $H_0$ is "The dice are rigged" against $H_1$ which is "The dices aren't rigged".

We are using the Scipy stats library in order to make a t-test and calculate a two-tailed p-value for a model that contains 11 degrees of freedom.

## Results

Game samples
![GitHub Logo](/businessTour/img/gathered_data.png)

Expected values
![GitHub Logo](/businessTour/img/real_values.png)

p_value:
0.9999999

## Conclusion

 

