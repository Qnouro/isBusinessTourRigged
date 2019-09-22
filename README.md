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

In order to check if the game is rigged, we are going to study the dice rolls. We are hence testing <a href="https://www.codecogs.com/eqnedit.php?latex=H&space;=&space;H_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H&space;=&space;H_0" title="H = H_0" /></a> against <a href="https://www.codecogs.com/eqnedit.php?latex=H&space;=&space;H_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H&space;=&space;H_1" title="H = H_1" /></a> where <a href="https://www.codecogs.com/eqnedit.php?latex=H_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_0" title="H_0" /></a>:"The dice are rigged" and <a href="https://www.codecogs.com/eqnedit.php?latex=H_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_1" title="H_1" /></a>: "The dice are not rigged".

We are using the Scipy stats library in order to make a t-test and calculate a two-tailed p-value for a model that contains 11 degrees of freedom.

In order to use it, the two sets must have similar variances.
## Results


![GitHub Logo](/businessTour/img/gathered_data.png)
*Game samples*

![GitHub Logo](/businessTour/img/real_values.png)
*Expected values*

variance of the game sample set:0.00235
variance of the excepted values set:0.00197  

Regarding the very close variances, we assume that the two sets have similar variances.

p_value:
0.9999999

## Conclusion
Due to the spectacularly high value of the p_value, we reject the <a href="https://www.codecogs.com/eqnedit.php?latex=H_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?H_0" title="H_0" /></a> hypothesis, and can conclude that the game is most-likely not rigged.
 

