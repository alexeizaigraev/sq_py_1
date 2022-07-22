import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 
from papa_pg import *

class DepFromFile():

    def main_dep_from_file(self):
        self.info = refresh_deps_from_indata_lite()


#u = DepFromFile()
#print(u.main_dep_from_file())