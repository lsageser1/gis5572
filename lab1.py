import arcpy
import psycopg2
xys = [[5,5], [10,10], [10,5]]
array = arcpy.Array([arcpy.Point(*xy) for xy in xys])
polygon = arcpy.Polygon(array)

pt = arcpy.Point(1, 2)
pt_geometry = arcpy.PointGeometry(pt)
pt_geometry

xyz = [[1,1], [2,2], [3,3]]
LineArray = arcpy.Array([arcpy.Point(*xy) for xy in xyz])
line = arcpy.Polyline(LineArray)
line

polygon

sr = arcpy.SpatialReference(4326)
polygon.SR = sr
wkt = polygon.WKT

connection = psycopg2.connect(
    host="34.134.195.125",
    database="lab0",
    user="postgres",
    password=']X[$I*r"jR}tdEOU'
)

cursor = connection.cursor()
table_query = "CREATE TABLE IF NOT EXISTS polygon (objectid SERIAL PRIMARY KEY, geom GEOMETRY)"

cursor.execute(table_query)
connection.commit()

insert_query = f"INSERT INTO polygon (geom) VALUES (ST_GeomFromText('{wkt}', 4326))"
cursor.execute(insert_query)
connection.commit()

del connection
del cursor
