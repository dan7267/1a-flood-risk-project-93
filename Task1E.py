from floodsystem.stationdata import MonitoringStation
from floodsystem.geo import rivers_by_station_number

def run():
    rivers_station_number = rivers_by_station_number(MonitoringStation, 9)
    print(rivers_station_number)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()