import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from doc_papa import *


class Rasplomb():

    def main(self):

        query = """SELECT terminals.model, terminals.serial_number,
        terminals.fiscal_number,
		terminals.termial, terminals.department
        FROM terminals, otbor
        WHERE terminals.termial = otbor.term;"""

        head = "№ п/п;model;serial;fiscal;terminal;department"
        fName = "Rasplomb.csv"
        self.info = doc_papa(query, head, fName)


#u = Rasplomb()
#u.main()
#print(u.info)