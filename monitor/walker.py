# -*- coding: utf-8 -*-
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os
import shutil
from papa_pg import get_data

class Walker():

    def dir_in_walk(self):
        return file_to_arr_nosharp(CONFIG_PATH + 'ConfigRaskladPath.txt')[0]

    def dir_out_walk(self):
            return 'G:/Мой диск/'
        
    def show(self):
        a = os.listdir(self.dir_in_walk())
        for aa in a:
            self.info += aa + '\n'
        if not a:
            self.info += '\nnothing show\n'


    def mk_agents(self):
        h = dict()
        for line in get_data('SELECT * FROM comon_data;'):
                h[line[1]] = line[4]
        return h

    def mover(self):
        self.info = ''
        agents = self.mk_agents()
        a = os.listdir(self.dir_in_walk())
        if len(a) < 1:
                self.info += '\n\tno files found\n'
        old_dir = self.dir_in_walk()
        out_dir = self.dir_out_walk()
        for aa in a:
            fname = os.path.abspath(aa).split(os.sep)[-1]
            old_fname = os.path.join(old_dir, fname)
            folder = fname[:7]
            key = fname[:3]
            new_root = os.path.join(out_dir, agents[key])
            new_dir = os.path.join(new_root, folder)
            new_fname = os.path.join(new_dir, fname)
            backup_fname = 'R:/DRM/ЗАИГРАЕВ ОБМЕН АРХИВ/Архив/' + fname
            arhiv_fname = 'C:/Users/Alex/Desktop/ЯРЛЫКИ/Data/arhiv_rp/' + fname
            if not os.path.exists(new_dir):
                try:
                    os.mkdir(new_dir)
                    self.info += '\tnew folder\n'
                except:
                    self.info += new_dir + '\n'
            try:
                shutil.copy(old_fname, backup_fname)
            except:
                pass

            try:
                shutil.copy(old_fname, arhiv_fname)
            except:
                pass
            
            try:
                shutil.move(old_fname, new_fname)
                self.info += new_fname + '\n'
            except Exception as ex:
                self.info += f'>> {new_fname}\n{ex}\n'
            
            
    def walker_main(self):
        self.out = ''
        
        self.info = ''        
        self.mover()

        self.info += '\n\n\nОстаток в rasklad:\n'
        self.show()
        self.info += (f'\n{self.out}\n')


#u = Walker()
#print(u.walker_main())

