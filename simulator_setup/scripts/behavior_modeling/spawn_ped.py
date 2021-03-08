#!/usr/bin/env python
import rospy
import os
import rospkg
import sys
from pedsim_srvs.srv import SpawnPedsRequest, SpawnPeds
from pedsim_msgs.msg import Ped
from geometry_msgs.msg import Point

rospack = rospkg.RosPack()
spawn_ped_srv = rospy.ServiceProxy('pedsim_simulator/spawn_peds', SpawnPeds)

peds = []
ped = Ped()

ped.id = 0
ped.pos = Point(1, 1, 0)
ped.type = 0
ped.number_of_peds = 1
ped.waypoints = [Point(9, 9, 0)]
ped.yaml_file = os.path.join(rospack.get_path("simulator_setup"), "obstacles", "person_two_legged.model.yaml")

peds.append(ped)

ped2 = Ped()
ped2.id = 1
ped2.pos = Point(1, 3, 0)
ped2.type = 0
ped2.number_of_peds = 1
ped2.waypoints = [Point(3, 3, 0), Point(3, 8, 0)]
ped2.yaml_file = os.path.join(rospack.get_path("simulator_setup"), "obstacles", "person_two_legged.model.yaml")

peds.append(ped2)

response = spawn_ped_srv.call(peds)
print("success" if response.finished else "failed")
