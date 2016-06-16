import processing
import os
import math

layer = qgis.utils.iface.activeLayer() 

pocet = 0

for feature in layer.selectedFeatures():
    geom = feature.geometry()
    attr = feature.attributes()
    pocet += 1
  
print processing.runalg('qgis:multiparttosingleparts', layer, "vysledek.shp")  
    
print pocet

