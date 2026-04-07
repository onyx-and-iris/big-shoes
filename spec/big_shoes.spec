# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
        ('../src/bundle/encdata.csv', 'bundle'), 
        ('../src/bundle/formation_dump', 'bundle'), 
        ('../src/bundle/initial_setup_data_dump', 'bundle'), 
        ('../src/bundle/preemptive.txt', 'bundle'),
        ('../src/img/icon.ico', 'img')
        ]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='big_shoes',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['../src/img/icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='big_shoes',
)
