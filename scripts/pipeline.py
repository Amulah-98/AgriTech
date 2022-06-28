 pipeline_flow = [
            {
                "type": "readers.ept",
                "filename": f"http://s3-us-west-2.amazonaws.com/usgs-lidar-public/{self.region}/ept.json",
                "resolution": 5,
                "bounds": f"({self.bounds_x}, {self.bounds_y})",
            },
            # {"type": "filters.hag_nn"},
            # {"type": "filters.ferry", "dimensions": "HeightAboveGround=Z"},
            # {
            #     "type": "filters.crop",
            #     "polygon": f"{self.polygon}",
            # },
            # {"type": "filters.locate", "dimension": "Z", "minmax": "max"},
            {
                "type": "writers.las",
                "compression": "false",
                "minor_version": "2",
                "dataformat_id": "0",
                "filename": str(self.data_dir / f"{self.region}.las"),
            },
            {
                "type": "writers.gdal",
                "gdaldriver": "GTiff",
                "output_type": "all",
                "resolution": "5.0",
                "filename": str(self.data_dir / f"{self.region}.tif"),
            },
        ]