import subprocess
import sys


width = sys.argv[1]
height = sys.argv[2]
refresh = sys.argv[3]
adapter = sys.argv[4]
def change_resolution(width, height, refresh,adapter):
    terminal_cvt = subprocess.run(['cvt', width, height, refresh], capture_output=True, text=True).stdout
    modeline = terminal_cvt[terminal_cvt.find("Modeline") + 9:]
    modeline_splited = modeline.split()
    print("Modeline:" + str(modeline))
    
    print("Generating new mode")
    xrandr_newmode = subprocess.run(['xrandr','--newmode'] + modeline_splited)
    print("Adding new mode: " + modeline_splited[0])
    xrandr_addmode = subprocess.run(['xrandr','--addmode',adapter,modeline_splited[0]],text=True)
    print("Setting the new resolution")
    xrandr_set = subprocess.run(['xrandr','--output',adapter,'--mode',modeline_splited[0]],text=True)
    print("Done")
#end function

#main
if(len(sys.argv) == 5):
    change_resolution(width, height, refresh,adapter)
else:
    print("Missing args")
    print("Usage:python3 xorg_resolution_changer.py WIDTH HEIGHT REFRESH ADAPTER")
    print("Example:" + "python3 xorg_resolution_changer.py 1280 1024 75 VGA-1")
