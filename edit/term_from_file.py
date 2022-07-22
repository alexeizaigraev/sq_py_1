
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 
from papa_pg import *

class TermFromFile():

    def main_term_from_file(self):
        self.info = term_from_file_full()

#u = TermFromFile()
#u.main_term_from_file()
