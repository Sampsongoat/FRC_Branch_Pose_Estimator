import math

FIELD_LENGTH = 17.548  # 2025 FRC field length in meters

# branch_id: (x, y, angle, use_direct_x)
BRANCHES = {
    1:  (5.350, 4.200, 180, True),
    2:  (5.040, 4.655, 60,  False),
    3:  (4.745, 4.805, 60,  False),
    4:  (4.230, 4.805, 120, False),
    5:  (3.935, 4.655, 120, False),
    6:  (3.635, 4.200, 180, False),
    7:  (3.635, 3.850, 180, False),
    8:  (3.935, 3.390, 240, False),
    9:  (4.215, 3.220, 240, False),
    10: (4.745, 3.220, 300, False),
    11: (5.040, 3.390, 300, False),
    12: (5.350, 3.850, 180, True)
}
DISTANCE_OFFSETS = {1, 6, 7, 12}

def compute_branch(branch_id, distance):
    x1, y1, angle, use_direct_x = BRANCHES[branch_id]
    d = distance - 0.05 if branch_id in DISTANCE_OFFSETS else distance

    if use_direct_x:
        x2, y2 = x1 + d, y1
        rot_deg = angle
    else:
        x2 = x1 + d * math.cos(math.radians(angle))
        y2 = y1 + d * math.sin(math.radians(angle))
        rot_deg = (angle + 180) % 360

    return (round(x2, 3), round(y2, 3), round(rot_deg, 3))

def get_branches(distance):
    blue_data = [compute_branch(i, distance) for i in range(1, 13)]
    
    red_data = [
        (round(FIELD_LENGTH - x, 3), y, (360 - rot) % 360)
        for x, y, rot in blue_data
    ]
    
    return blue_data, red_data

if __name__ == "__main__":
    distance = float(input("Enter distance from branch (in meters): "))
    blue_branches, red_branches = get_branches(distance)
    
    print("Blue branches:")
    for _ in blue_branches:
        print(_)
    print("Red branches:")
    for _ in red_branches:
        print(_)
