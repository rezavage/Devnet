import telnetlib
import sys
import getpass

tn = telnetlib.test('192.168.1.2')
from pathlib import Path
path = Path()
for file in path.glob('*'):
    print(file)
path = Path('email')
path.mkdir()
