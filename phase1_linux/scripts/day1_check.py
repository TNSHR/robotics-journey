import os
import sys
import platform
from datetime import date

print("=" * 50)
print("   ROBOTICS JOURNEY — DAY 1 SYSTEM CHECK")
print("=" * 50)
print(f"  Date      : {date.today()}")
print(f"  OS        : {platform.system()} {platform.release()}")
print(f"  Python    : {sys.version.split()[0]}")
print(f"  User      : {os.environ.get('USER')}")
print(f"  Workspace : {os.path.expanduser('~/robotics_journey')}")
print("=" * 50)
print("  STATUS    : READY FOR 10-MONTH JOURNEY 🚀")
print("=" * 50)