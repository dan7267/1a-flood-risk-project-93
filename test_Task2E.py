from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation


def test_plot_water_levels():
    plot_water_levels(MonitoringStation, 10, 5)