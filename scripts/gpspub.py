import rclpy
import os
from rclpy.node import Node

from sensor_msgs.msg import NavSatFix
from sensor_msgs.msg import NavSatStatus
from std_msgs.msg import Header

import json

lat = [35.2960, 35.2989, 35.3029, 35.3019, 35.3059, 35.31253, 35.30926, 35.31171, 35.3171, 35.2960, 35.2989, 35.3029, 35.3019, 35.3059, 35.31253, 35.30926, 35.31171, 35.3171,35.2960, 35.2989, 35.3029, 35.3019, 35.3059, 35.31253, 35.30926, 35.31171, 35.3171, 35.2960, 35.2989, 35.3029, 35.3019, 35.3059, 35.31253, 35.30926, 35.31171, 35.3171, 35.2960, 35.2989, 35.3029, 35.3019, 35.3059, 35.31253, 35.30926, 35.31171, 35.3171, 35.2960, 35.2989, 35.3029, 35.3019, 35.3059, 35.31253, 35.30926, 35.31171, 35.3171, 35.2960, 35.2989, 35.3029, 35.3019, 35.3059, 35.31253, 35.30926, 35.31171, 35.3171, 35.2960, 35.2989, 35.3029, 35.3019, 35.3059, 35.31253, 35.30926, 35.31171, 35.3171]
lon = [-80.7430, -80.7372, -80.7381, -80.7465, -80.7496, -80.74303, -80.74115, -80.73361, -80.7267, -80.7430, -80.7372, -80.7381, -80.7465, -80.7496, -80.74303, -80.74115, -80.73361, -80.7267, -80.7430, -80.7372, -80.7381, -80.7465, -80.7496, -80.74303, -80.74115, -80.73361, -80.7267, -80.7430, -80.7372, -80.7381, -80.7465, -80.7496, -80.74303, -80.74115, -80.73361, -80.7267, -80.7430, -80.7372, -80.7381, -80.7465, -80.7496, -80.74303, -80.74115, -80.73361, -80.7267, -80.7430, -80.7372, -80.7381, -80.7465, -80.7496, -80.74303, -80.74115, -80.73361, -80.7267, -80.7430, -80.7372, -80.7381, -80.7465, -80.7496, -80.74303, -80.74115, -80.73361, -80.7267, ]
i = 0
#with open('gps.json') as json_file:
#    data = json.loads(json_file)
#    latlist = data["latitude"]
#    print(latlist)

class GpsNode(Node):

    def __init__(self):
        super().__init__('gps_node')
        self.publisher_ = self.create_publisher(NavSatFix, 'gps/fix', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)



    def timer_callback(self):
            msg = NavSatFix()
            msg.header = Header()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = "gps"

            msg.status.status = NavSatStatus.STATUS_FIX
            msg.status.service = NavSatStatus.SERVICE_GPS

            # Position in degrees.
            #with open('gps.txt') as json_file:
                #data = json.load(json_file)
                #print(data(0))
                #for p in data['latitude']:
                    #msg.latitude = p['latitude']
                    #msg.longitude = p['longitude']

            global i
            msg.latitude = lat[i]
            msg.longitude = lon[i]
            i = i+1
            #msg.latitude = 57.047218
            #msg.longitude = 9.920100

            # Altitude in metres.
            msg.altitude = 1.15

            msg.position_covariance[0] = 0
            msg.position_covariance[4] = 0
            msg.position_covariance[8] = 0
            msg.position_covariance_type = NavSatFix.COVARIANCE_TYPE_DIAGONAL_KNOWN

            self.publisher_.publish(msg)
            self.best_pos_a = None



def main(args=None):
    i = 0
    rclpy.init(args=args)

    gps_node = GpsNode()

    rclpy.spin(gps_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gps_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
