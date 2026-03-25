"""Simple sorting utility for this project."""

from typing import Iterable, List


def sort_numbers(values: Iterable[int], reverse: bool = False) -> List[int]:
    """Return a sorted list of integers.

    Args:
        values: Any iterable of integers.
        reverse: When True, sorts in descending order.

    Returns:
        A newly sorted list.
    """
    return sorted(values, reverse=reverse)


if __name__ == "__main__":
    sample = [5, 1, 9, 3, 7]
    print("原始数据:", sample)
    print("升序:", sort_numbers(sample))
    print("降序:", sort_numbers(sample, reverse=True))
