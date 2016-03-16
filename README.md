Mission Pinball Framework Examples
==================================

<img align="right" height="200" src="mpf-examples-logo.png"/>

This GitHub repository contains example configuration, demos, and tutorial files for the Mission Pinball Framework. It's
a separate repo from the main MPF project so you can download this folder to an easily-accessible location.

The examples here are synchronized to work with the corresonding branches in MPF and the MPF-MC. (e.g. the "master"
branch of mpf-examples works with the master branch of mpf, the dev branch works with the dev branch, etc.)

If you're new to MPF, start with the tutorial at http://missionpinball.com/docs/tutorial.

More details about MPF are here: https://missionpinball.com/mpf/

[![Coverage Status](https://coveralls.io/repos/missionpinball/mpf-examples/badge.svg?branch=dev&service=github)](https://coveralls.io/github/missionpinball/mpf-examples?branch=dev)
[![Build Status](https://travis-ci.org/missionpinball/mpf-examples.svg?branch=dev)](https://travis-ci.org/missionpinball/mpf-examples)

Note that the branch of this repo corresponds to the branch of MPF. (e.g. the 'master' branch of examples here should
work with the master branch of MPF, the dev with the dev, etc.)


Description of Examples
=======================
The following folders contain helpful things and learning examples you can use as you create your own machine and learn
MPF.

mc_demo
-------
A "slide show" demo showing off the features of the MPF Media Controller. You can run this and hit the right and left
arrow keys to step through the slides, and you can check out the config source to see how to do these things in your own
game.

starter_game
------------
A template you can use as a starting point for your own game. This is purely optional. Use it. Or not.

tutorial(s)
-----------
The tutorial folder (and all the folders that start with the name "tutorial") are companion files which you can use to
follow along with the step-by-step tutorial at https://missionpinball.com/tutorial.

wpc_template
--------------------
Contains a template config which you can use as a starting point for a WPC-era machine.


Real Machine Examples
=====================
We've used MPF on lots of physical machines, including WPC-era, Stern SAM, System 11, and some older machines. Each
folder here contains some kind of config for a real machine. None of these are complete, and in fact many are nothing
more than the hardware config files, but they might be helpful if you have one of these machines or just to see how
different things are setup in MPF.

Note that no copyrighted information or intellectual property from the original pinball manufacturer or any original
license holder is in any of these folders. There are no reproductions of original games here, rather, these projects
contain sample MPF code and configs that can run on original hardware.

aztec
-----
Configuration for a 1976 Williams Aztec machine. This is the "portable pinball" machine you might have seen in the FAST
Pinball booth at a show.

big_shot
--------
Configuration for a 1974 Gottlieb Big Shot EM machine which was converted to P-ROC and MPF for the Pinball Expo 2014.
More info about this project is [here](https://missionpinball.com/blog/category/games/big-shot-em-conversion/).

bullseye
--------
Configuration for a 1986 Grand Products 301/Bulls Eye machine (originally sold as a conversion kit for early 1980s Bally
machines).

demo_man
--------
Configuration for a 1994 Williams Demolition Man machine. This is one of the machines we use to test MPF on, so it's
kept pretty up-to-date. More info on this project is [here](https://missionpinball.com/blog/category/games/building-demo-man/).

hurricane
---------
Configuration for a 1991 Williams Hurricane machine. This is a good example of a pre-fliptronics config as well as an
early solid-state / "pre trough" config.

indy
----
Configuration for a 1994 Williams Indian Jones: The Pinball Adventure machine. This is another dev machine we use for
MPF, and it's kept fairly up-to-date.

jd
--
Configuration for a 1993 Williams Judge Dredd machine. This was one of the early machines we used to develop MPF.

jokerz
------
Configuration for a 1989 Williams Jokerz machine. This folder pretty much just contains the hardware config, but it's an
example of a System 11 machine using Snux's System 11 interface board.

pinbot
------
Configuration for a 1986 Williams PIN*BOT machine. This folder pretty much just contains the hardware config, but it's
another example of a System 11 machine using Snux's System 11 interface board.

stle
----
Configuration for a 2013 Stern Star Trek. This config demonstrates a Stern SAM machine being controlled by a P-ROC.
([Demo Video](https://www.youtube.com/watch?v=q7IE3rzp-88))

sttng
-----
Configuration for a 1993 Williams Star Trek: The Next Generation machine.

License
=======
All of these examples are released via the MIT license (same as MPF), which means you can do pretty much anything you
want with them. Feel free to use anything you find here for your own game. You don't have to ask permission, or pay us,
or even give us credit. Just make an awesome game!!
