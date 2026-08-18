# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for SINGLE-FILE build of tibialauncher.exe
Build:
  pyinstaller tibialauncher_onefile.spec
Result:
  dist/tibialauncher.exe (one file)
"""
import os
from PyInstaller.utils.hooks import collect_submodules

APP_NAME = "tibialauncher"
ENTRY_SCRIPT = "pyside6_gaming_launcher.py"
ICON_PATH = "images/appicon.ico" if os.path.exists("images/appicon.ico") else None

hidden_imports = collect_submodules('PySide6')

datas = [
    ('images/*.png', 'images'),
    ('images/*.ico', 'images'),
    ('config/*', 'config'),
]

a = Analysis(
    [ENTRY_SCRIPT],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports + ['tibialauncher', 'tibialauncher.core', 'tibialauncher.core.launcher_core', 'tibialauncher.core.github_downloader', 'tibialauncher.core.file_manager'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_PATH,
    version='version_info.txt',
)
