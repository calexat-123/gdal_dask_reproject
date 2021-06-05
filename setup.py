import sys
from setuptools import setup
import param
import re


version = param.version.get_setup_version(__file__, 'gdal_dask_reproject', archive_commit="$Format:%h$")


if 'sdist' in sys.argv and 'bdist_wheel' in sys.argv:
    version = re.split('((\d+\.)+\d)', version)[1]


install_requires = [
    'dask[complete]',
    'pyproj',
    'rasterio',
    'rioxarray',
    'xarray-spatial',
    'param',
]

setup_args = dict(
    name='gdal_dask_reproject',
    version=version,
    install_requires=install_requires,
    zip_safe=False,
    packages=['cc_reproject',],
    include_package_data=True,
)


if __name__ == '__main__':
    setup(**setup_args)
