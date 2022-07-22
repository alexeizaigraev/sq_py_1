import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
import os


class Postall():
    
    def dir_out_post(self):
        return file_to_arr_nosharp(CONFIG_PATH + 'ConfigPostPath.txt')[0]

    def post_all(self, ag, fout):
        out_text = "login;status;fio;terminal;agent\n"
        a = [f'{line[0]};{line[1]};{line[2]};{line[-2]};{line[-1].strip()}' 
            for line in self.all_kass
            if (len(line) > 3 \
                and ag in line[-1] \
                and ('true' in line[1]))]
        out_text += '\n'.join(a).rstrip()
        text_to_file(out_text, fout)
        #ssay(fout)



    def mk_fierd(self):
        all_otpuska = file_to_arr_nosharp(IN_DATA_PATH + 'all_otpuska.csv')
        a = [line[0] for line in all_otpuska
            if line and 'nul' not in line[3]]
        return a

    def mk_all_kass(self):
        all = [line.split(';') for line in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8") 
            if len(line.split(';')) > 4 
            and 'true' in line.split(';')[1]
            and line.split(';')[0] not in self.fierd]
        return all

    def mk_all_otpuska(self):
        otpuska = [line for line in open(IN_DATA_PATH + 'all_otpuska.csv', 'r', encoding="UTF-8") 
        if line.split(';')[0] not in self.fierd]
        return otpuska

    def kass(self, ag):
        rez = [line[0] for line in self.all_kass
            if len(line) > 3 \
                and ag in line[-1] \
                and 'true' in line[1]]
        return rez

    def post_otpuska(self, ag, fout):
        logins = self.kass(ag)
        out_text = "login;otpusk_start;otpusk_finish;data_uvolneniya\n"
        
        #a = file_to_arr(IN_DATA_PATH + 'all_otpuska.csv')
        rez = [';'.join(line[:4]).replace('null', '')
            for line in self.otp_arr
            if line[0] in logins]
        out_text += '\n'.join(rez)
        text_to_file(out_text, fout)
        #say(fout)


    




    def postall_main(self):
        info = ''
        post_path = GDRIVE_PATH
        self.fierd = self.mk_fierd()
        self.all_kass = self.mk_all_kass()

        self.all_otpuska = self.mk_all_otpuska()
        self.otp_arr = file_to_arr_nosharp(IN_DATA_PATH + 'all_otpuska.csv')
        info += IN_DATA_PATH + 'all_otpuska.csv\n'

        self.post_all('justin', post_path + 'justin/OutPostAll.csv')
        info += post_path + 'justin/OutPostAll.csv\n'
        self.post_otpuska('justin', post_path + 'justin/OutPostOtpuskaJust.csv')
        info += post_path + 'justin/OutPostOtpuskaJust.csv\n'

        self.post_all('allo', post_path + 'allo/OutPostAllAllo.csv')
        info += post_path + 'allo/OutPostAllAllo.csv\n'

        self.post_all('satua', post_path + 'sat/OutPostAllSat.csv')
        info += post_path + 'sat/OutPostAllSat.csv\n'
        self.post_otpuska('satua', post_path + 'sat/OutPostOtpuskaSat.csv')
        info += post_path + 'sat/OutPostOtpuskaSat.csv\n\n'

        post_path = OUT_DATA_PATH + 'DOC/'
        self.post_all('justin', post_path + 'justin/OutPostAll.csv')
        info += post_path + 'justin/OutPostAll.csv\n'
        self.post_otpuska('justin', post_path + 'justin/OutPostOtpuskaJust.csv')
        info += post_path + 'justin/OutPostOtpuskaJust.csv'
        self.info = info



#u = Postall()
#u.postall_main()