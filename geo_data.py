#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
"""GeoTest

Usage:
  geotest.py <filename>
  
"""

import os
import sys
import geojson
from docopt import docopt

def print_props(feature):
    props = feature['properties']
    print("----------------------------------------")
    for k,v in props.items():
        try: 
            print('{}:\t\t{}'.format(k, v))
        except:
            print("ERROR")
    print("----------------------------------------")
    
def by_prop(feature, *args, **kwargs):
    props = feature['properties']
    for key, value in kwargs.items():
        try:
            if props[key] != value:
                return False
        except KeyError:
            return False
                
    return True

def load_geo_json(filename):
    f = open(filename, encoding="utf-8")
    net = geojson.load(f)
    f.close()
    return net

def main(args):
    filename = args['<filename>']
    vendor_data = load_geo_json(filename)
    filtered = filter(lambda x: by_prop(x, bahnart="Schmalspurbahn"), net['features'])
    for feature in filtered:
        print_props(feature)
        
    
if __name__ == '__main__':
    arguments = docopt(__doc__, version='GeoTest 1.0')
    main(arguments)