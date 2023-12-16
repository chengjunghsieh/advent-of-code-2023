# advent-of-code-2023


## Day 07

* Usage of `str`'s `translate` and `maketrans`
* Heuristic to calculate hand's score
  * https://www.reddit.com/r/adventofcode/comments/18cnzbm/comment/kcc4azi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
  * ie. [entropy](https://www.reddit.com/r/adventofcode/comments/18cnzbm/comment/kccov05/)


# Day 10

Part 2:

> say you have an enclosed shape, and you want to color every pixel inside of it. How do you know if a given pixel is inside the shape or not? Well, it turns out: if you shoot a ray in any direction from the pixel and it crosses the boundary an odd number of times, it's inside. if it crosses an even number of times, it's outside. Works for all enclosed shapes, even self-intersecting and non-convex ones.
>
> It does, however, interact badly if your ray and one of the edges of the shape is collinear, so you have to be clever about it for this problem.

> Part 2: If we consider the closed loop as an integral polygon then [Pick's theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem) relates the area of the closed loop (which can be calculated using the [shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula)), the number of integer points on the boundary of the closed loop (which is just the length of the close loop), and the number of integer points in the interior of the loop (which is the answer).