# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['time_tracker_v_4.py'],
             pathex=['C:\\Users\\jinal\\Documents\\Time_Tracker\\Time_Tracker_Git_Windows\\testing_code_latesttt'],
             binaries=[],
             datas=[('C:\\Users\\jinal\\Envs\\time_tracker\\lib\\site-packages\\eel\\eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='time_tracker_v_4',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
