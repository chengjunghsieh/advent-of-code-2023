# advent-of-code-2023

Tricks:

```python
def transpose(x: list[str]) -> list[str]:
  return list(zip(*x))

def rotate90(x: list[str]) -> list[str]:
  return list((map(lambda l: ''.join(reversed(l)), zip(*x))))
```


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

# Day 12

* DP
* use `functools::cache` for memorizing

# Day 13

[u/4HbQ solution](https://topaz.github.io/paste/#XQAAAQAvAQAAAAAAAAA4HMAC0B3AtL+oWviBxctH86JJ/6PHrH/ibLmvcCigiNSr3DJj/8ZvYRMK4yAj3KqAAi0HpH+1HI3c477ShjEEy5eU0rJZ5XPMYjUa7KUUSMAW1drkZO07jdwAFDkc4bNsMoNxYUsKIVSpdlovqUPejkc8NpWtBAgIWd7/9ZC4/XSwnbMYcblPFtJMKIF6yJqiVrhsUCTxX5zJZd/K0lmHVrZ/8Hi1ih/6gOHGvfXUkst4D1Vh+XV6LhD8OqPlRM7DQNvM8SKMBsBnnuE+BBYeFTWIuJIFP//B2RkA)

# Day 14

* Memorization and find cycle

# Day 16
[u/4HbQ solution](https://topaz.github.io/paste/#XQAAAQAUAwAAAAAAAAAziAOiE/kI+atcxglPNa1Z5ByKIiDHt58MHifgG2R3rf+zqKYQZv1B457oZ4kCsEABs+9eoKiNQRgfhGTI51bj3uRshO3PWkcO2ujzAaCpLjowdp1GKNTOnkukUGRQKdOcsHDROmva3wF9HKvBRmDVX57YyOReLWiXWu7VZ6BH+4I4+HYwrpO4f3Cnm0z1SibCaOiKz4eojGMOAGzZZpSzQOL3fz30dX5Pyz12ucW45Yuu+ZiaJ7UdH/MYB9mWGHziy8uujcM+VxQUCWPjkRQ0XdsUM3PC+CTKPYXP2Gyaq+wyME55uuGsNGBw46QrFtVC+Shv2NuT8LF2oxefM5bcWLHsbpmwLCIV0EqhAiT5KgU7RRDjVOGA4hLybRH7NlZSaFrNUASfRa+QEb2StcGlaaQnm5IpLIJ0ngBwFVo1XbqqDcxOKAMUfyPEs1EQR2JOm/9/+sQBjXgiCNWpr//6SPk0)

# Day 17

* usage of `heapq`
* vairant of Dijkstra
* State is `(position, direction)`
* when reaching a cell push the possibility from `min_step` to `max_step` then turn to next direction
