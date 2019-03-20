# -*- mode: python -*-
import os
import sys
import distutils.util

block_cipher = None
COM_PLATFORM = distutils.util.get_platform()

if COM_PLATFORM == 'win-amd64':
    platform = 'win'
    PATHEX = ['E:\\work\\https'] 
    ICO_NAME = 'icon/test.ico'
    STRIP = False
else:
    print('Un-support Platform:{}'.format(platform))
    sys.exit(-1)


a = Analysis(
    ['main.py'],
    pathex=PATHEX,
    binaries=[],
    datas=[
        ('icon', 'icon'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher)


pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher)


exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='test',
    debug=False,
    strip=STRIP,
    upx=True,
    icon=ICO_NAME,
    console=False
)
