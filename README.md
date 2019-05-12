FlagSort
========

A script to sort the terrible "United States of Europe Flag" by color.

Motivation
--------

This is a small project inspired by [a post](https://www.reddit.com/r/eyehurtingflags/comments/bbpylz/lord_help_us_all/eklg0cw?utm_source=share&utm_medium=web2x) on the r/eyehurtingflags subreddit. Being a big fan of those animated sorting videos myself, I decided to try and make one myself.

The colors are sorted by HSV and QuickSort is used as the actual algorithm.

Libraries Used
-------
* [Pillow](https://pillow.readthedocs.io/en/stable/) for initial image processing
* [Pygame](https://www.pygame.org) for animation rendering

Other Sources
------
* Modified version of iterative QuickSort implementation from [GeeksForGeeks](https://www.geeksforgeeks.org/iterative-quick-sort/)
* Color sorting options and explanation from [Alan Zucconi](https://www.alanzucconi.com/2015/09/30/colour-sorting/)
