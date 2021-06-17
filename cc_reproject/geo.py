import xarray
from .warp import reproject


@xarray.register_dataarray_accessor('geo')
class CCRasterArray:

    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    def reproject(self, dst_crs, **kwargs):
        return reproject(self._obj, dst_crs, **kwargs)
