def is_tolerable(notes: list[int]) -> bool:
    """ 
    If the notes are stunning or tolerable.
    If at most no notes should be changed
    """
    count = 0
    min_val = notes[0]
    for i in notes[1:]:
        if i > min_val:
            count += 1
        else:
            min_val = min(i, min_val)
        
        if count > 1:
            return False
    return True


def count(values: list[int], target_value: int) -> int:
    """ Returns total number of valid distributions """
    notes = [0] * len(values)
    all_solutions = solve(values, target_value, 0, notes)
    return sum(is_tolerable(solution) for solution in all_solutions)


def solve(values: list[int], remainder: int, curr_index: int, notes: list[int]) -> list[int]:
    """ Likely to benefit from memo as couple of ways to reach this state with (curr_index, remainder) and number of distributions """
    # We have found a solution
    if remainder == 0:
        return [notes]
    
    # We have some value left but notes cannot complete it.
    if remainder != 0 and curr_index >= len(notes):
        return []
    
    # negative remainder
    if remainder <= 0:
        return []
    
    curr_value = values[curr_index]
    max_notes = remainder // curr_value
    new_notes = notes[:]
    all_solutions = []
    for n in range(max_notes + 1):
        new_remainder = remainder - n * curr_value
        if new_remainder < 0:
            break 
        
        new_notes[curr_index] += n
        solution = solve(values, new_remainder, curr_index + 1, new_notes)
        if solution:
            all_solutions.extend([i[:] for i in solution])

        new_notes[curr_index] -= n

    return all_solutions


    



if __name__ == "__main__":
    print(is_tolerable([1, 1, 2, 2]))
    print(count([1, 1], 7))
    print(count([1, 1, 1], 5))