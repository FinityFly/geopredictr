import geopandas as gpd

shapefile_filepath = "assets/shapefile/lpr_000b21a_e.shp"

shapefile_data = gpd.read_file(shapefile_filepath)

print("plot:")
shapefile_data.plot()