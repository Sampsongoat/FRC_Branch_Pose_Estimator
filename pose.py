import math

FIELD_LENGTH = 17.548 / 2 # 2025 FRC field length in meters

# ----------- Helper for printing poses -----------
def print_pose(name, x, y, rotation):
    print(f"constexpr frc::Pose2d {name} "
          f"{{{x:.3f}_m, {y:.3f}_m, frc::Rotation2d{{{rotation:.1f}_deg}}}};")


# ----------- BLUE BRANCH PARAMETERS -----------
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


# ----------- COMPUTE BLUE BRANCH POSE -----------
def compute_branch(branch_id, distance):
    x1, y1, angle, use_direct_x = BRANCHES[branch_id]
    d = distance - 0.05 if branch_id in DISTANCE_OFFSETS else distance

    if use_direct_x:
        # Branches 1 & 12 just extend directly along +X (no rotation)
        x2, y2 = x1 + d, y1
        rot_deg = angle
    else:
        # Normal trig-based branch movement
        x2 = x1 + d * math.cos(math.radians(angle))
        y2 = y1 + d * math.sin(math.radians(angle))
        rot_deg = (angle + 180) % 360

    print_pose(f"kBlueBranch{branch_id}", x2, y2, rot_deg)
    return x2, y2, rot_deg


# ----------- MAIN FUNCTION -----------
def get_branches(distance):
    blue_data = [compute_branch(i, distance) for i in range(1, 13)]

    print("\n=== RED SIDE ===")
    for i, (x, y, rot) in enumerate(blue_data, start=1):
        red_x = x + FIELD_LENGTH -.204
        red_y = y
        red_rot = rot
        print_pose(f"kRedBranch{i}", red_x, red_y, red_rot)


# ----------- RUN -----------
if __name__ == "__main__":
    distance = float(input("Enter distance from branch (in meters): "))
    print("=== BLUE SIDE ===")
    get_branches(distance)


# import math

# FIELD_LENGTH = 17.548  # 2025 FRC field length in meters

# # ----------- Helper for printing poses -----------
# def print_pose(name, x, y, rotation):
#     print(f"constexpr frc::Pose2d {name} "
#           f"{{{x:.3f}_m, {y:.3f}_m, frc::Rotation2d{{{rotation:.1f}_deg}}}};")


# # ----------- BLUE BRANCHES -----------
# def blue_branch_1(distanceFromBranch):
#     X = 5.350 + distanceFromBranch
#     Y = 4.200
#     rotation_deg = 180.0
#     print_pose("kBlueBranch1", X, Y, rotation_deg)
#     return X, Y, rotation_deg

# def blue_branch_2(distanceFromBranch):
#     x1, y1 = 5.040, 4.655
#     angle_deg = 60.0
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch2", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_3(distanceFromBranch):
#     x1, y1 = 4.802, 4.900
#     angle_deg = 60.0
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch3", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_4(distanceFromBranch):
#     x1, y1 = 4.175, 4.900
#     angle_deg = 120
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch4", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_5(distanceFromBranch):
#     x1, y1 = 3.935, 4.655
#     angle_deg = 120
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch5", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_6(distanceFromBranch):
#     x1, y1 = 3.635, 4.200
#     angle_deg = 180
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch6", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_7(distanceFromBranch):
#     x1, y1 = 3.635, 3.850
#     angle_deg = 180
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch7", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_8(distanceFromBranch):
#     x1, y1 = 3.935, 3.390
#     angle_deg = 240
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch8", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_9(distanceFromBranch):
#     x1, y1 = 4.175, 3.200
#     angle_deg = 240
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch9", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_10(distanceFromBranch):
#     x1, y1 = 4.780, 3.200
#     angle_deg = 300
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch10", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_11(distanceFromBranch):
#     x1, y1 = 5.040, 3.390
#     angle_deg = 300
#     d = distanceFromBranch
#     x2 = x1 + d * math.cos(math.radians(angle_deg))
#     y2 = y1 + d * math.sin(math.radians(angle_deg))
#     rot_deg = (angle_deg + 180.0) % 360.0
#     print_pose("kBlueBranch11", x2, y2, rot_deg)
#     return x2, y2, rot_deg

# def blue_branch_12(distanceFromBranch):
#     X = 5.350 + distanceFromBranch
#     Y = 3.850
#     rotation_deg = 180.0
#     print_pose("kBlueBranch12", X, Y, rotation_deg)
#     return X, Y, rotation_deg


# # ----------- MAIN -----------
# def get_branches(distance):
#     # Store Blue poses for Red mirroring
#     blue_data = []
#     blue_data.append(blue_branch_1(distance - 0.05))
#     blue_data.append(blue_branch_2(distance))
#     blue_data.append(blue_branch_3(distance))
#     blue_data.append(blue_branch_4(distance))
#     blue_data.append(blue_branch_5(distance))
#     blue_data.append(blue_branch_6(distance - 0.05))
#     blue_data.append(blue_branch_7(distance - 0.05))
#     blue_data.append(blue_branch_8(distance))
#     blue_data.append(blue_branch_9(distance))
#     blue_data.append(blue_branch_10(distance))
#     blue_data.append(blue_branch_11(distance))
#     blue_data.append(blue_branch_12(distance - 0.05))

#     print("\n=== RED SIDE ===")
#     for i, (x, y, rot) in enumerate(blue_data, start=1):
#         mirrored_x = FIELD_LENGTH - x
#         mirrored_rot = (360 - rot) % 360
#         print_pose(f"kRedBranch{i}", mirrored_x, y, mirrored_rot)


# # ----------- RUN -----------
# if __name__ == "__main__":
#     distance = float(input("Enter distance from branch (in meters): "))
#     print("=== BLUE SIDE ===")
#     get_branches(distance)
