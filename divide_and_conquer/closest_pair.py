"""
Problem:
Given an array of points P = [(x1,y1),(x2,y2), ..., (xn,yn)].
Point i has coordinate x ith and y ith.
Find the closest pair of points in an array and its distance
Example:
find_closest_pair([(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (1, 1), (-900, 3), (100, 3)])
-> ((2,3), (3,4))
"""
import math

Point = tuple[int, int]


def calculate_distance_sqr(point1: Point, point2: Point) -> float:
    """calculate eucidean distance between 2 points
    calculate_distance_sqr([1,2],[2,4]) -> 2.236067
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def column_base_sort(points: list[Point], column: int = 0) -> list[Point]:
    return sorted(points, key=lambda point: point[column])


def find_closest_pair(points: list[Point]) -> tuple[Point, Point]:
    Px = column_base_sort(points, 0)
    Py = column_base_sort(points, 1)
    return _recurs_find_closest_pair(Px, Py)


def _recurs_find_closest_pair(Px: list[Point], Py: list[Point]) -> tuple[Point, Point]:
    n_point = len(Px)

    if n_point <= 3:
        return brute_force(Px)

    middle = n_point // 2
    # the points in Qx, Qy are same, but Qx is sorted by x, Qy is sorted by y
    Qx, Qy = Px[:middle], []
    # the same with Rx, Ry
    Rx, Ry = Px[middle:], []

    x_threshold = Qx[-1][0]
    for point in Py:
        if (point[0] <= Qx[-1][0]):
            Qy.append(point)
        else:
            Ry.append(point)

    lp1, lp2 = _recurs_find_closest_pair(Qx, Qy)
    rp1, rp2 = _recurs_find_closest_pair(Rx, Ry)

    dl = calculate_distance_sqr(lp1, lp2)
    dr = calculate_distance_sqr(rp1, rp2)

    d = min(dl, dr)

    sp1, sp2 = _find_closest_pair_split(Py, x_threshold, d)

    if sp1:
        return sp1, sp2
    elif dl <= dr:
        return lp1, lp2
    else:
        return rp1, rp2


def _find_closest_pair_split(points, x_threshold, delta: float) -> tuple[Point, Point]:
    lower_bound, upper_bound = x_threshold - delta, x_threshold + delta

    Sy = list(filter(lambda point: lower_bound <=
                     point[0] <= upper_bound, points))

    p1, p2 = None, None

    min_dist = delta

    for i in range(len(Sy) - 1):
        for j in range(i + 1, min(8, len(Sy) - i)):
            dist = calculate_distance_sqr(points[i], points[j])
            if (dist < min_dist):
                p1, p2 = points[i], points[j]
                min_dist = dist
    return p1, p2


def brute_force(points: list[Point]) -> tuple[Point, Point]:
    if len(points) <= 1:
        return (None, None)
    min_dist = math.inf
    res1, res2 = points[0], points[1]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            new_dist = calculate_distance_sqr(points[i], points[j])
            if (new_dist < min_dist):
                res1, res2 = points[i], points[j]
                min_dist = new_dist
    return res1, res2


if __name__ == "__main__":
    ps1 = [(2, 3), (12, 30), (40, 50), (5, 1)]
    print(find_closest_pair(ps1))  # ((2,3),(5,1))
    ps2 = [(2, 3), (12, 30), (40, 50), (5, 1),
           (12, 10), (3, 4), (1, 1), (-900, 3), (100, 3)]
    print(find_closest_pair(ps2))  # ((2,3),(3,4))
    ps3 = [(1, 1), (1, 1), (42, 12), (1, 4), (9, -3)]
    print(find_closest_pair(ps3))  # ((1,1),(1,1))
