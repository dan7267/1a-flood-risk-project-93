from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation

def run():
    """Requirements for Task1C"""
    Nearby_stations_info = stations_within_radius(MonitoringStation, (52.2053, 0.1218), 10)
    print(sorted(Nearby_stations_info))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()