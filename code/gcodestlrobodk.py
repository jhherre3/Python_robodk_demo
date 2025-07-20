from robodk import robolink, robomath
import re

# === Setup RoboDK ===
RDK = robolink.Robolink()
robot = RDK.Item('', robolink.ITEM_TYPE_ROBOT)
tool = RDK.Item('Tool', robolink.ITEM_TYPE_TOOL)
frame = RDK.Item('Reference Frame', robolink.ITEM_TYPE_FRAME)
target_ref = RDK.Item('Target 1', robolink.ITEM_TYPE_TARGET)

# Sanity check
if not all([robot.Valid(), tool.Valid(), frame.Valid(), target_ref.Valid()]):
    raise Exception("Missing robot/tool/frame/target in station.")

robot.setPoseTool(tool)
robot.setPoseFrame(frame)

# === Load G-code ===
gcode_path = r"C:\cubeholesix.gcode"
x = y = z = 0.0
pose_list = []

with open(gcode_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith(';') or line.startswith('M') or not line:
            continue

        if line.startswith(('G1', 'G0')):
            if 'X' in line:
                x = float(re.search(r'X([-+]?[0-9]*\.?[0-9]+)', line).group(1))
            if 'Y' in line:
                y = float(re.search(r'Y([-+]?[0-9]*\.?[0-9]+)', line).group(1))
            if 'Z' in line:
                z = float(re.search(r'Z([-+]?[0-9]*\.?[0-9]+)', line).group(1))

            # Apply Target 1's orientation, use X/Y/Z from G-code
            base_pose = target_ref.Pose()
            pose = base_pose
            pose.setPos([x, y, z + 50])  # Safety lift if Z=0
            pose_list.append(pose)


# === MOVE ROBOT LIVE ===
if pose_list:
    try:
        robot.MoveJ(pose_list[0])
        for pose in pose_list:
            robot.MoveL(pose)
        print(f"Executed {len(pose_list)} poses from G-code.")
    except Exception as e:
        print("Robot movement failed:", e)
else:
    print("No valid poses found in G-code.")
