"""
You have to prepare for a hiking trip. There are a knapsack and a list of food.
Each food has its own value (representing calories) and weight.
The knapsack cannot take more than w weight. Meanwhile, you want to consume as much
calories as possible during the hiking trip.

Which food to put into the knapsack?

Given:
avail: maximum weight knapsack can carry
items: a list of food to consider

Return:
(total, chosen_items)
total: total number of calories in a given knapsack
chosen_items: list of food that are chosen to put into the knapsack

Approach: Use search tree / decision tree implementation for brute-force approach
With any items, we can have 2 options: to take or not to take that item.
Both choices form a binary tree, the left child is the result
when we take that item, the right child is the result when we do not take.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Food:
    name: str
    value: int
    weight: int


def max_val(items: list[Food], avail: int) -> tuple[int, list[Food]]:
    """Given list of food to consider and maximum weight knapsack can carry
    Get a list of food to put inside a knapsack so that we get maximum value/calories in total

    Args:
        items: list of food to consider
        avail: maximum weight knapsack can carry
    Return:
        total: total value/calories of chosen food
        chosen_items: a list of food to put into a knapsack
    """
    if len(items) == 0 or avail == 0:
        return (0, [])
    elif items[0].weight > avail:
        # Explore right branch only
        return max_val(items[1:], avail)
    else:
        next_item = items[0]

        # Explore left branch
        with_val, with_to_take = max_val(items[1:], avail - next_item.weight)
        with_val += next_item.value

        # Explore right branch
        without_val, without_to_take = max_val(items[1:], avail)

        # Choose better branch
        if with_val > without_val:
            return (with_val, with_to_take + [next_item])
        else:
            return (without_val, without_to_take)


def build_menu(food_infos: list[tuple[str, int, int]]) -> list[Food]:
    """Generate list of Food from tuple"""
    return list(map(lambda info: Food(info[0], info[1], info[2]), food_infos))


if __name__ == "__main__":
    menu = build_menu(
        [
            ("wine", 89, 123),
            ("beer", 90, 154),
            ("pizza", 95, 258),
            ("burger", 100, 354),
            ("fries", 90, 365),
            ("cola", 79, 150),
            ("apple", 50, 95),
            ("donut", 10, 195),
        ]
    )
    print(max_val(menu, 750))  # (353, ...)
