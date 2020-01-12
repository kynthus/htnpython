import sys
import cx_Freeze

cx_Freeze.setup(
    name='mytest',
    executables=[
        cx_Freeze.Executable(
            script='msi_hello.py',
            base='Win32GUI' if sys.platform == 'win32' else None,
            targetName='hello.exe',
        ),
    ],
)
