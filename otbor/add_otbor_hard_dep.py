import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, insert_all_otbor


class OtborHardDep():
    def __init__(self, deps_choise):
        if ' ' in deps_choise:
            self.deps = deps_choise.split(' ')
        else:
            self.deps = [deps_choise,]
        
    def main(choise):
        if ' ' in choise:
            choise = choise.split(' ')
        elif '\n' in choise:
            choise = choise.split('\n')
        else:
            choise = [choise,] 
        info = ''
        arr = []
        for term, dep dep in self.deps:
            if len(dep) < len(self.deps[0]):
                dep = self.deps[0][:4] + dep
            term = dep + '1'
            info += f'{term} {dep}\n'
            arr.append([term, dep])
        insert_all_otbor(arr)
        self.info = info

