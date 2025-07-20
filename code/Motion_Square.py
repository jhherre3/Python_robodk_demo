from robodk import robolink, robomath

RDK = robolink.Robolink()
robot = RDK.Item('', robolink.ITEM_TYPE_ROBOT)
tool = RDK.Item('Tool', robolink.ITEM_TYPE_TOOL)
ref_frame = RDK.Item('Reference Frame', robolink.ITEM_TYPE_FRAME)
robot.setPoseTool(tool)
robot.setPoseFrame(ref_frame)

target = RDK.Item('Target 1', robolink.ITEM_TYPE_TARGET)
if not target.Valid():
    raise Exception("Target 1 not found.")

pose_center = target.Pose()

side = 50
offsets = [[0, 0], [side, 0], [side, side], [0, side], [0, 0]]

poses = [pose_center * robomath.transl(dx, dy, 0) for dx, dy in offsets]

prog = RDK.AddProgram("Motion_Square", robot)
prog.setRunType(robolink.PROGRAM_RUN_ON_SIMULATOR)

prog.MoveJ(robot.JointsHome())
for pose in poses:
    prog.MoveL(pose)

RDK.ShowMessage("Square path complete.")
