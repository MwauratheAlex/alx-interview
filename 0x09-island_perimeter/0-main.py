#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

    test_cases = [
        # Single land cell
        (
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            4
        ),
        # Long vertical island
        (
            [
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            8
        ),
        # Larger island with complex shape
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0]
            ],
            24
        ),
        # No island (all water)
        (
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            0
        ),
    ]

    for i, (grid, expected) in enumerate(test_cases, 1):
        result = island_perimeter(grid)
        print(f"Test case {i}: {'Passed' if result == expected else 'Failed'}")
        print(f"Expected: {expected}, Got: {result}\n")
