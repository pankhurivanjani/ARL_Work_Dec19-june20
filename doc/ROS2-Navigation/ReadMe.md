ROS2 Navigtion

* Creation of a geofence 

* Embeddeding virtual obstacle layer in static layer of costmap 

* Playing with parameter( launch file) to change the configuration of costmap configurations 

* Working with static layer, robot fails to recignize the boundary from static map 

* Writing new costmap plugins? Doesn't make sense especially from GPS data. For new costmap we require some logics which we don't have here.

* Probable cause of failure in this method- we  are providing different world, and different localization. Localization failure ???

* Most of the robots using ros2 navigation rely on Laser scan and SLAM

* What next???

* Let's play around with localization! 

* Turn off by default AMCL  

* Implement something simpler, maybe your own linear function converting GPS lat-lons to your own co-ordinate system OR for complexity Kalman filter based localization

* Where/how to fit/link the new localizer instead of amcl in the navigation stack 

https://github.com/ArghyaChatterjee/GPS-waypoint-based-Autonomous-Navigation-in-ROS



