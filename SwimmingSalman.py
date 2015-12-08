# configuration
INCREMENT_AMOUNT = .05

# constants
XAVIER_LAPS = 15

# derived values
range1 = range(1,int(XAVIER_LAPS/INCREMENT_AMOUNT))
for i in range(0, len(range1)):
    val = range1[i]
    range1[i] = ((val-1)*INCREMENT_AMOUNT) + 1

# 2.15
range2 = range(2140, 2160)
for i in range(0, len(range2)):
    range2[i] = range2[i] / 1000.0

# 2.143
range3 = range(21420, 21440)
for i in range(0, len(range3)):
    range3[i] = range3[i] / 10000.0

# 2.1428-2.1429
range4 = range(214280, 214290)
for i in range(0, len(range4)):
    range4[i] = range4[i] / 100000.0

# 2.14286
range5 = range(2142850, 2142870)
for i in range(0, len(range5)):
    range5[i] = range5[i] / 1000000.0

# 2.142857
range6 = range(21428560, 21428580)
range6 = [x / 10000000.0 for x in range6]

# 2.1428571
range7 = range(214285700, 214285720)
range7 = [x / 100000000.0 for x in range7]

# 2.14285714
range8 = range(2142857130, 2142857150)
range8 = [x / 1000000000.0 for x in range8]

# 2.142857143
range9 = range(21428571420, 21428571440)
range9 = [x / 10000000000.0 for x in range9]

# 2.1428571429
range10 = range(214285714280, 214285714300)
range10 = [x / 100000000000.0 for x in range10]

yusuf_laps_range = range10



class Swimmer():
    def __init__(self, initialposition, speed, initialdirection, poolsize):
        self.initialposition = initialposition
        self.speed = speed
        self.initialdirection = initialdirection
        self.poolsize = poolsize

        # speed is an arbitrary value referring to pool units per 30 seconds
        # where poolsize is the size of the pool in pool units
        # so, convert to laps per minute
        pool_units_per_30_seconds = speed
        pool_units_per_60_seconds = speed * 2
        laps_per_60_seconds = float(pool_units_per_60_seconds) / poolsize
        self.lpm = laps_per_60_seconds
    def getPositionAndDirection(self, time_in_seconds):
        elapsed_minutes = time_in_seconds / 60.0
        laps_completed = self.lpm * elapsed_minutes
        full_laps_completed = int(laps_completed)
        partial_additional = laps_completed - full_laps_completed
        odd_full_laps_completed = (full_laps_completed % 2) == 1
        direction_change = odd_full_laps_completed

        # return value: direction
        if not direction_change:
            return_value_direction = self.initialdirection
        else:
            if self.initialdirection == "up":
                return_value_direction = "down"
            else:
                return_value_direction = "up"

        # return value: position
        if return_value_direction == "up":
            return_value_position = partial_additional * self.poolsize
        else:
            return_value_position = (1-partial_additional) * self.poolsize

        return (return_value_position, return_value_direction)

def position_difference(PD1, PD2):
    p1 = PD1[0]
    p2 = PD2[0]
    diff = p1 - p2
    diff = abs(diff)
    if (diff < .000000000001):
        diff = 0
    return diff

for yusuf_laps in yusuf_laps_range:

    pool_length = XAVIER_LAPS + yusuf_laps
    solution_n = yusuf_laps
    xavier_pool_lengths_per_minute = (XAVIER_LAPS * 2.0) / pool_length
    xavier_minutes_per_pool_length = 1 / xavier_pool_lengths_per_minute
    solution_m = XAVIER_LAPS * xavier_minutes_per_pool_length

    Xavier = Swimmer(0, XAVIER_LAPS, "up", pool_length)
    Yusuf = Swimmer(pool_length, yusuf_laps, "down", pool_length)

    display_list = [solution_n, solution_m]

    # 30
    xPD = Xavier.getPositionAndDirection(30)
    yPD = Yusuf.getPositionAndDirection(30)
    display_list.append(position_difference(xPD, yPD))

    # 90
    xPD = Xavier.getPositionAndDirection(90)
    yPD = Yusuf.getPositionAndDirection(90)
    display_list.append(position_difference(xPD, yPD))
    
    # 120
    xPD = Xavier.getPositionAndDirection(120)
    yPD = Yusuf.getPositionAndDirection(120)
    position_difference_120 = position_difference(xPD, yPD)
    if (position_difference_120 == 0):
        position_difference_120 = str(position_difference_120)
        position_difference_120 = "                     " + position_difference_120
    display_list.append(position_difference_120)

    print "n = %s, m = %s, 30:%s, 90:%s, 120:%s" % tuple(display_list)

