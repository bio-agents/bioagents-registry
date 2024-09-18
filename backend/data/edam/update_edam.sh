#!/bin/bash
filename='/iechor/application/backend/data/edam/current_version.txt'
version=$(head -n 1 $filename)
url="https://raw.githubusercontent.com/edamontology/edamontology/master/releases/EDAM_"${version}".owl"
writepath=/iechor/application/backend/data/edam/owl/EDAM_${version}.owl
curl $url > $writepath
python /iechor/application/backend/manage.py parse_edam
