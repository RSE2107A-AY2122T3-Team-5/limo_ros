#!/usr/bin/env python

from __future__ import print_function
from std_msgs.msg import String
from limo_status_translator.srv import GetLimoStatus
from limo_status_translator.msg import Num
import rospy

tmp = Num()

def handle_process_msg(request):
    if request.get_status == 0:
        print('Requesting status for vehicle state:\n')
        if Num.vehicle_state == 0:
            HumanString = "System Normal"
        elif Num.vehicle_state == 2:
            HumanString = "System Exception"

        return HumanString

    elif request.get_status == 1:
        print('Requesting status for control mode:\n')
        if Num.control_mode == 0:
            HumanString = "Standby"
        elif Num.control_mode == 1:
            HumanString = "Command Control"
        elif Num.control_mode == 2:
            HumanString = "App Control"
        elif Num.control_mode == 3:
            HumanString = "Remote Control"

        return HumanString

    elif request.get_status == 2:
        print('Requesting status for battery voltage:\n')
        return Num.battery_voltage


    elif request.get_status == 3:
        print('Requesting status for error code:\n')
        #TO DO PLEASE
        status_string = "ERROR_CODE = %s"% Num.error_code

    elif request.get_status == 4:
        print('Requesting status for motion mode:\n')
        if Num.motion_mode == 0:
            HumanString = "4-Wheel differential"
        elif Num.motion_mode == 1:
            HumanString = "Ackerman"
        elif Num.motion_mode == 2:
            HumanString = "Mecanum Wheel"

        return HumanString


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + '\n')
    tmp.vehicle_state = data.vehicle_state
    tmp.control_mode  = data.control_mode
    tmp.battery_voltage = data.battery_voltage
    tmp.error_code = data.error_code
    tmp.motion_mode = data.motion_mode


def limo_translator():
    rospy.init_node('limo_status_translator_node')
    rospy.Subscriber('/limo_status', Num, callback)
    s = rospy.Service('Get_Limo_Status', GetLimoStatus, handle_process_msg)
    print("Ready to translate.")
    rospy.spin()

if __name__ == "__main__":
    limo_translator()
