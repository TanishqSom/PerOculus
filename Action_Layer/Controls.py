import pymavlink.mavutil as mavutil
import time

class DroneController:
    def __init__(self, connection_string="udp:127.0.0.1:14550"):
        """Connect to the drone via MAVLink"""
        print("Connecting to drone...")
        self.drone = mavutil.mavlink_connection(connection_string)
        self.drone.wait_heartbeat()
        print("Drone Connected!")

    def arm_drone(self):
        """Arms the drone"""
        self.drone.mav.command_long_send(
            self.drone.target_system, self.drone.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0,
            1, 0, 0, 0, 0, 0, 0
        )
        print("Drone Armed!")

    def upload_waypoints(self, waypoints):
        """Upload waypoints for autonomous flight"""
        for i, (lat, lon, alt) in enumerate(waypoints):
            self.drone.mav.mission_item_send(
                self.drone.target_system, self.drone.target_component,
                i, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 1, 0, 0, 0, 0, lat, lon, alt
            )
        print("Waypoints Uploaded!")

    def takeoff(self, altitude=10):
        """Takeoff command"""
        self.drone.mav.command_long_send(
            self.drone.target_system, self.drone.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0,
            0, 0, 0, 0, 0, 0, altitude
        )
        print(f"Drone taking off to {altitude}m altitude!")

if __name__ == "__main__":
    drone = DroneController()
    drone.arm_drone()
    drone.takeoff()
    waypoints = [(28.7041, 77.1025, 10), (28.7050, 77.1030, 15)]
    drone.upload_waypoints(waypoints)
