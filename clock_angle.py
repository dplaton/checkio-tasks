
HOUR_ANGLE = 360 / float(12)
MINUTE_ANGLE = 360 / float(60)

def clock_angle(time):

    split_time = map(int,time.split(":"))

    min_hand=split_time[1]
    hr_hand=split_time[0] if split_time[0] < 12 else split_time[0] - 12

    min_angle = min_hand * MINUTE_ANGLE
    hr_angle = (hr_hand * HOUR_ANGLE) + (min_hand * (HOUR_ANGLE / 60))

    angle = abs(min_angle - hr_angle)
    return angle if angle <= 180 else 360 - angle


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
