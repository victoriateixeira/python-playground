def study_schedule(permanence_period, target_time):
    time_frequency = 0
    for period in permanence_period:
        (start_time, end_time) = period
        if (
            type(start_time) is not int
            or type(end_time) is not int
            or type(target_time) is not int
        ):
            return None
        if start_time <= target_time <= end_time:
            time_frequency += 1

    return time_frequency
