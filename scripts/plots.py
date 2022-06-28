import json
from pathlib import Path

import geopandas
import laspy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pdal
import rasterio
from rasterio.plot import show, show_hist
from shapely.geometry import Point, Polygon

from logger import Logger

    
    def plot_dem_contours(self) -> None:
        """
        Plots DEM with its contours
        """

        src = rasterio.open(str(self.data_dir / f"{self.region}.tif"))

        fig, ax = plt.subplots(1, figsize=(20, 10))
        show((src), cmap="Greys_r", ax=ax)
        show((src), contour=True, linewidths=0.7, ax=ax)

        plt.show()

    def plot_2D(self) -> None:
        """
        Plots side by side of DEM and histogram.
        """

        src = rasterio.open(str(self.data_dir / f"{self.region}.tif"))

        fig, (ax_rgb, ax_hist) = plt.subplots(1, 2, figsize=(20, 10))
        show((src), cmap="Greys_r", contour=True, ax=ax_rgb)
        show_hist(
            src,
            bins=50,
            histtype="stepfilled",
            lw=0.0,
            stacked=False,
            alpha=0.3,
            ax=ax_hist,
        )

        plt.show()

    def plot_heatmap(self, year: str, data_dict: dict) -> None:
        """
        Plots a heatmap view of a terrain
        Parameters
        ---
            year: str
                the year of the desired geopandas data
            data_dict: dict
                the dictionary mapping of the year to its geopandas data
        """

        fig, ax = plt.subplots(1, 1, figsize=(20, 10))
        fig.patch.set_alpha(0)
        plt.grid("on", zorder=0)
        data_dict[year].plot(
            column="elevation_m", ax=ax, legend=True, cmap="terrain"
        )
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.show()

    def plot_3D(self, year: str, data_dict: dict) -> None:
        """
        Plots a 3D view of a terrain
        Parameters
        ---
            year: str
                the year of the desired geopandas data
            data_dict: dict
                the dictionary mapping of the year to its geopandas data
        """

        fig, ax = plt.subplots(1, 1, figsize=(20, 10))
        fig.set_size_inches(18.5, 10.5, forward=True)
        ax = plt.axes(projection="3d")
        x = data_dict[year].geometry.x
        y = data_dict[year].geometry.y
        z = data_dict[year].elevation_m
        points = np.vstack((x, y, z)).transpose()
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=0.01)
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        plt.show()