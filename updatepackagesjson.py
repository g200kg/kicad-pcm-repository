import os
import zipfile
import subprocess
import requests

print("Zip page Permalink : ")
url = input()

url2 = url.replace(
    'github.com/g200kg/','raw.githubusercontent.com/g200kg/')
url2 = url2.replace('blob/','')
print('')

print('{')
print('    "version": "2.x.x",')
print('    "kicad_version": "9.0",')
print('    "runtime": "ipc",')
print('    "platforms": [')
print('        "linux",')
print('        "macos",')
print('        "windows"')
print('    ],')
print('    "status": "stable",')

print(f'    "download_url":"{url2}",')
response = requests.get(url2)
response.raise_for_status()

with open("package.zip", "wb") as file:
    file.write(response.content)
print(f'    "download_size":{len(response.content)},')

fname = './package.zip'
res = subprocess.run(['sha256sum', fname], stdout=subprocess.PIPE, text=True)
sha256 = res.stdout.split(' ')[0]
print(f'    "download_sha256":"{sha256}",')

distpath = './work/'
ins_size = 0
with zipfile.ZipFile('package.zip', 'r') as zip_ref:
    for fnam in zip_ref.namelist():
        zip_ref.extract(fnam, './work/')
        ins_size += os.path.getsize(f'./work/{fnam}')
print(f'    "install_size":{ins_size}')
print('}')