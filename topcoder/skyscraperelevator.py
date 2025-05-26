

def simulate(floors: int, people: list[int]) -> int:
    running_sum = 0
    elevator_position = 0
    
    for destination_floor in people:
        time_by_stairs = 20 * destination_floor
        time_by_elevator = elevator_position + destination_floor

        if time_by_stairs < time_by_elevator:
            running_sum += time_by_stairs
        else:
            running_sum += time_by_elevator
            elevator_position = destination_floor
    
    return running_sum


if __name__ == "__main__":
    print(simulate(47000, [19, 1, 1000]))
    print(simulate(1000000, [1000000, 1000000, 1000000, 7, 500000]))

    test_people = [564066, 28, 899, 118046, 1751493, 224, 59, 48213, 1, 3760703, 74405, 11, 3492, 4895554, 227542, 8977, 129400, 19967, 3673, 183925, 1369931, 257446, 100, 85328, 22220, 50, 278697, 92, 9933, 8187, 67131, 3608673, 53, 95910, 5, 3, 28402, 24401, 7574, 3946, 30262, 3, 7297, 4112, 65027, 1691143, 16240, 470, 4302722, 566, 9057, 20751, 39721, 440, 10, 3645, 147550, 53883, 108, 66775, 884, 362, 2, 14, 10, 15, 27022, 1375, 6820, 1, 1621, 2, 4, 9, 16090, 4358, 3182591, 78, 8248521, 1, 2552, 113857, 14265, 5983, 16309, 314278, 5, 799, 3650332, 329, 3584, 2, 19, 308]
    assert simulate(9273694, test_people) == 109585802

