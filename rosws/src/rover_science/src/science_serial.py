#!/usr/bin/env python
import serial
import struct
import rospy
import time
import std_srvs.srv
import rover_science.srv

s = serial.Serial(port="/dev/ttyACM0", baudrate=38400)
rospy.init_node("science_serial")

# CAROUSEL CONTROL
def move_to_funnel(request):
    data = struct.pack("<BB", 0x00, request.index)
    s.write(data)
    rospy.loginfo('Move %s to funnel' % request.index)
    return rover_science.srv.CarouselResponse()

def move_to_ph(request):
    data = struct.pack("<BB", 0x01, request.index)
    s.write(data)
    rospy.loginfo('Move %s to ph' % request.index)
    return rover_science.srv.CarouselResponse()

to_funnel_service = rospy.Service("/science/carousel/funnel", rover_science.srv.Carousel, move_to_funnel)
rospy.loginfo('Initialized service /science/carousel/funnel')
to_ph_service = rospy.Service("/science/carousel/ph", rover_science.srv.Carousel, move_to_ph)
rospy.loginfo('Initialized service /science/carousel/ph')

# ETHANOL TUBE CONTROL
def open_tube(request):
    data = struct.pack("<B", 0x02)
    s.write(data)
    rospy.loginfo('Open tube')
    return std_srvs.srv.EmptyResponse()

open_tube_service = rospy.Service("/science/tube/open", std_srvs.srv.Empty, open_tube)
rospy.loginfo('Initialized service /science/tube/open')

def close_tube(request):
    data = struct.pack("<B", 0x03)
    s.write(data)
    rospy.loginfo('Close tube')
    return std_srvs.srv.EmptyResponse()

close_tube_service = rospy.Service("/science/tube/close", std_srvs.srv.Empty, close_tube)
rospy.loginfo('Initialized service /science/tube/close')

while not rospy.is_shutdown():
    time.sleep(1)

