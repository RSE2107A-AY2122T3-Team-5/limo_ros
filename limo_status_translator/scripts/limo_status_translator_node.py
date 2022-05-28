#!/usr/bin/env python

from __future__ import print_function
from std_msgs.msg import String
from limo_status_translator.srv import GetLimoStatus
from limo_status_translator.msg import Num
import rospy

def handle_process_msg(request):
    if request.get_status == 0:
        print('Requesting status for vehicle state:\n')
        if Num.vehicle_state == 0:
            status_string = "VEHICLE_STATE = System Normal"
        elif Num.vehicle_state == 2:
            status_string = "VEHICLE_STATE = System Exceptional"

      
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

        status_string = "CONTROL_MODE = %s"% HumanString

    elif request.get_status == 2:
        print('Requesting status for battery voltage:\n')
        status_string = "BATTERY_VOLTAGE = %s"% Num.battery_voltage

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

        status_string = "MOTION_MODE = %s"% HumanString

    return status_string

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "\n%s", data.data)

def limo_translator():
    rospy.init_node('limo_status_translator_node')
    rospy.Subscriber('/limo_status', String, callback)
    s = rospy.Service('Get_Limo_Status', GetLimoStatus, handle_process_msg)
    print("Ready to translate.")
    rospy.spin()

if __name__ == "__main__":
    limo_translator()
