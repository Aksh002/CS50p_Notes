#pip install pyfiglet
from pyfiglet import Figlet as fg
import sys
try:
    z=sys.argv[2]
except pyfinglet.FontNotFound(Font):
    sys.exit()
if len(sys.argv)==1:
    x=fg()
elif len(sys.argv)==3:
    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        x=fg(font=sys.argv[2])
else:
    sys.exit()
i=input("Input:")
print(x.renderText(i))