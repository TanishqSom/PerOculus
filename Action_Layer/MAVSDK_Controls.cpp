#include <iostream>
#include <mavsdk/mavsdk.h>
#include <mavsdk/plugins/action/action.h>
#include <mavsdk/plugins/mission/mission.h>
#include <thread>

using namespace mavsdk;
using namespace std;

class DroneController {
public:
    DroneController(const string& connection_url) {
        cout << "Connecting to drone..." << endl;
        mavsdk.add_any_connection(connection_url);
        system = mavsdk.systems().at(0);
        action = make_unique<Action>(system);
        mission = make_unique<Mission>(system);
        cout << "Drone Connected!" << endl;
    }

    void arm_drone() {
        cout << "Arming drone..." << endl;
        action->arm();
        cout << "Drone Armed!" << endl;
    }

    void takeoff(double altitude) {
        cout << "Taking off..." << endl;
        action->takeoff();
        this_thread::sleep_for(chrono::seconds(5));
        cout << "Drone reached altitude " << altitude << "m!" << endl;
    }

    void upload_waypoints() {
        vector<Mission::MissionItem> mission_items;
        mission_items.push_back(create_waypoint(28.7041, 77.1025, 10));
        mission_items.push_back(create_waypoint(28.7050, 77.1030, 15));

        mission->upload_mission({mission_items});
        cout << "Waypoints Uploaded!" << endl;
    }

private:
    Mavsdk mavsdk;
    shared_ptr<System> system;
    unique_ptr<Action> action;
    unique_ptr<Mission> mission;

    Mission::MissionItem create_waypoint(double lat, double lon, double alt) {
        Mission::MissionItem waypoint;
        waypoint.latitude_deg = lat;
        waypoint.longitude_deg = lon;
        waypoint.relative_altitude_m = alt;
        return waypoint;
    }
};

int main() {
    DroneController drone("udp://:14550");
    drone.arm_drone();
    drone.takeoff(10);
    drone.upload_waypoints();
    return 0;
}
