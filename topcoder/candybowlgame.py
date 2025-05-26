import math


def total_combinations(c: int, k: int) -> int:
    assert c >= k
    return int(math.factorial(c) / (math.factorial(k) * math.factorial((c - k))))


def generate_distributions(initial_bowls: list[int], extra_candies: int) -> list[list[int]]:
    """
    Takes a starting distribution 'initial_bowls' and generates all possible distributions
    after adding all extra candies.

    Candies are indistinguishable so we want to avoid outputting duplicate combinations. The
    number of combinations is given by C(E + N - 1, N - 1).

    General formula for binomial coefficient is n! /(k!(n-k)!) combinatons.

    There are two approaches:
    1. Add all candies to first bowl and then move over to the right. Requires backtracking
    2. Add one at a time and build up to the left
    """

    start = initial_bowls[:]
    start[0] += extra_candies
    yield from generate_distributions_alternative(extra_candies, start, current_idx=0)


def generate_distributions_alternative(
    movable_candies: int, bowls: list[int], current_idx: int = 0
) -> list[int]:
    if current_idx >= len(bowls) - 1:
        yield bowls[:]
        return

    # Try moving 0, 1, 2, ..., candies_left from current bowl to next bowl
    for move_count in range(movable_candies + 1):
        bowls[current_idx] -= move_count
        bowls[current_idx + 1] += move_count

        yield from generate_distributions_alternative(move_count, bowls, current_idx + 1)

        bowls[current_idx] += move_count
        bowls[current_idx + 1] -= move_count

    
if __name__ == "__main__":
    for c in generate_distributions([0, 0, 0], 6):
        print(c)