"""
You have to prepare for a hiking trip. There are a knapsack and a list of food.
Each food has its own value (representing calories) and weight.
The knapsack cannot take more than w weight. Meanwhile, you want to consume as much
calories as possible during the hiking trip. In this problem, you can take a fraction
of an item.

Which food to put into the knapsack?

Given:
avail: maximum weight knapsack can carry
items: a list of food to consider

Return:
(total, chosen_items)
total: total number of calories in a given knapsack
chosen_items: list of food that are chosen to put into the knapsack

Approach: Use greedy approach. This may not return the most optiomal solution,
but it can return local optimimal solution.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Food:
    name: str
    value: int
    weight: int


def build_menu(food_infos: list[tuple[str, int, int]]) -> list[Food]:
    """Generate list of Food from tuple"""
    return list(map(lambda info: Food(info[0], info[1], info[2]), food_infos))


def greedy(items: list[Food], avail: int) -> tuple[float, list[Food]]:
    sorted_items = sorted(
        items, key=lambda food: food.value / food.weight, reverse=True
    )

    chosen_items: list[Food] = []

    total_value, total_weight = 0.0, 0

    for food in sorted_items:
        if total_weight >= avail:
            break
        added_weight = min(food.weight, avail - total_weight)
        total_weight += added_weight
        added_value = (added_weight / food.weight) * food.value
        total_value += added_value
        chosen_items.append(Food(food.name, added_value, added_weight))

    return (total_value, chosen_items)


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
    print(greedy(menu, 750))  # sort by value
