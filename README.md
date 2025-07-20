# Python\_robodk\_demo

## Project Overview


This project demonstrates how to use Python scripting with the RoboDK API to simulate robot toolpath programming for a 6-axis industrial robot. Specifically, it shows how to move the **ABB IRB 120-3/0.6** robot to follow a square shaped path in 3D space.

The **first exercise** in the series and focuses on foundational motion generation and simulation.
![Square Motion](images/square_motion.png)

In the second exercise, we demonstrate a more advanced motion type — a screw (helical) path — showcasing a continuous spiral with 10 rotations using linear TCP control. This spiral path introduces concepts of orientation preservation, math-based motion generation, and smooth 3D trajectory control. 
![Spiral Motion](images/spiral.png)

---

## Objectives

* Connect to RoboDK using Python
* Set up robot tool and reference frames
* Use a pre-defined target as the center of the path
* Dynamically generate and follow a square toolpath
* Visualize the simulation inside RoboDK

---

## What It Does

1. **Grabs the robot model** and assigns the active tool and reference frame.
2. **Retrieves a pose** from `Target 1` inside RoboDK (created manually).
3. **Generates 5 poses** that form a square around the center point.
4. Uses `MoveL()` linear moves to connect the square corners.
5. Runs the full simulation as a RoboDK program.

---

## Tools Used

* **Python** + `robodk` module
* **RoboDK** simulation environment
* **ABB IRB 120-3/0.6** robot model
* Custom RoboDK Targets & Frames

---

## Results

* Square toolpath completed without collisions
* TCP maintained correct orientation
* Robot motion was fully simulated in RoboDK


---

## 🔗 Resources

* [RoboDK Python API Docs](https://robodk.com/doc/en/PythonAPI/index.html)

---

> *This project serves as a foundational robotics coding exercise for anyone learning offline robot programming using Python.*
