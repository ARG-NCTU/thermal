///first time
cd ~/catkin_ws/src/
git clone git@github.com:ARG-NCTU/thermal_cam.git
cd ..
catkin_make
source devel/setup.bash
\\\

<get the gray grade photo>
source catkin_ws/devel/setup.bash
roslaunch thermal_cam acquisition.launch //collect the data

#crtl C to stop 
<turn gray to RGB>
open thermaltrans.py and change the file path
