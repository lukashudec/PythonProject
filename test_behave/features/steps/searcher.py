import os
import sys

from Calendar import CalendarClass
from calendar_merge import *

i=0
for x in sys.path:
    i=i+1
    print(str(i)+" "+x)