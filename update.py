import os
import pathlib
import datetime
import time
import platform
import subprocess

print('{')
print('    "$schema": "https://gitlab.com/kicad/code/kicad/-/raw/master/kicad/pcm/schemas/pcm.v1.schema.json#/definitions/Repository",')
print('    "maintainer": {')
print('        "name": "g200kg",')
print('        "contact": {')
print('            "email": "gaito@g200kg.com",')
print('            "web": "https://www.g200kg.com",')
print('            "twitter": "@g200kg"')
print('        }')
print('    },')
print('    "name": "g200kg KiCad PCM repository",')

fname = './packages.json'
pstat = os.stat(fname)

res = subprocess.run(['sha256sum', fname], stdout=subprocess.PIPE, text=True)
sha256 = res.stdout.split(' ')[0]

tsf = pstat.st_mtime
ts = int(tsf)
dt = datetime.datetime.fromtimestamp(ts)

print('    "packages": {')
print('        "sha256": "%s",' % sha256)
print('        "update_time_utc": "%s",' % dt)
print('        "update_timestamp": %s,' % ts)
print('        "url": "https://raw.githubusercontent.com/g200kg/kicad-pcm-repository/main/packages.json"')
print('    },')

fname = './resources.zip'
pstat = os.stat(fname)

res = subprocess.run(['sha256sum', fname], stdout=subprocess.PIPE, text=True)
sha256 = res.stdout.split(' ')[0]

tsf = pstat.st_mtime
ts = int(tsf)
dt = datetime.datetime.fromtimestamp(ts)

print('    "resources": {')
print('        "sha256": "%s",' % sha256)
print('        "update_time_utc": "%s",' % dt)
print('        "update_timestamp": %s,' % ts)
print('        "url": "https://github.com/g200kg/kicad-pcm-repository/raw/main/resources.zip"')
print('    }')
print('}')
