from robodk import robolink, robomath
import math

# Init API and get objects
RDK = robolink.Robolink()
robot = RDK.Item('', robolink.ITEM_TYPE_ROBOT)
tool = RDK.Item('Tool', robolink.ITEM_TYPE_TOOL)
ref_frame = RDK.Item('Reference Frame', robolink.ITEM_TYPE_FRAME)
target = RDK.Item('Target 1', robolink.ITEM_TYPE_TARGET)

robot.setPoseTool(tool)
robot.setPoseFrame(ref_frame)

# Get base pose from Target 1
base_pose = target.Pose()

# Helix parameters
radius = 25             # mm (OD/2)
pitch = 20              # mm per turn
turns = 10
steps_per_turn = 36
total_steps = turns * steps_per_turn

# Create program
prog = RDK.AddProgram("Motion_Screw", robot)
prog.setRunType(robolink.PROGRAM_RUN_ON_SIMULATOR)

# Start at home
prog.MoveJ(robot.JointsHome())

# Generate screw (helix) path
for i in range(total_steps + 1):
    theta = 2 * math.pi * i / steps_per_turn
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    z = pitch * i / steps_per_turn
    pose_offset = robomath.transl(x, y, z)
    pose = base_pose * pose_offset
    prog.MoveL(pose)

# Return to home
prog.MoveJ(robot.JointsHome())

RDK.ShowMessage("Helical screw motion completed.")
