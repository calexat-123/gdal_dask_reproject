## GDAL reprojection with Dask Arrays
#### Reprojection of maps with coordinate referrence systems (crs), using GDAL's implementation with Rasterio and supportind Dask backed arrays for parallel computing.

#### Inspired by the work of Kirill Kouzoubov in OpenDataCube and with the desire to have a standalone GDAL dask reprojection package: (Note: all errors are my own).

[Issue in rioxarray](https://github.com/corteva/rioxarray/issues/119)

[ODC code](https://github.com/opendatacube/odc-tools/blob/develop/libs/algo/odc/algo/_warp.py)
