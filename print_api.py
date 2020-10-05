import sys
import os

platform = sys.platform

# print(platform)

if platform == "linux":
    print("On Linux")
    os.system("lpr -p MF3010 " + platform)
elif platform == "win32":
    print("On windows")


def send_to_os(filepath):
    if platform == "linux":
        print("Sending " + filepath + " to lpr...")
    elif platform == "win32":
        print("Sending " + filepath + " to Print...")


send_to_os("print.pdf")
