import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from papa_pg import * 

db_exec("""
            CREATE TABLE IF NOT EXISTS terminals (
            department TEXT DEFAULT '',
            termial TEXT PRIMARY KEY DEFAULT '',
            model TEXT DEFAULT '',
            serial_number TEXT DEFAULT '',
            date_manufacture TEXT DEFAULT '',
            soft TEXT DEFAULT '',
            producer TEXT DEFAULT '',
            rne_rro TEXT DEFAULT '',
            sealing TEXT DEFAULT '',
            fiscal_number TEXT DEFAULT '',
            oro_serial TEXT DEFAULT '',
            oro_number TEXT DEFAULT '',
            ticket_serial TEXT DEFAULT '',
            ticket_1sheet TEXT DEFAULT '',
            ticket_number TEXT DEFAULT '',
            sending TEXT DEFAULT '',
            books_arhiv TEXT DEFAULT '',
            tickets_arhiv TEXT DEFAULT '',
            to_rro TEXT DEFAULT '',
            owner_rro TEXT DEFAULT '',
            register TEXT DEFAULT '',
            finish TEXT DEFAULT ''
            )""")

print('terminals ok')

#________________________________

db_exec("""
            CREATE TABLE IF NOT EXISTS departments (
            department TEXT PRIMARY KEY DEFAULT '',
            region TEXT DEFAULT '',
            district_region TEXT DEFAULT '',
            district_city TEXT DEFAULT '',
            city_type TEXT DEFAULT '',
            city TEXT DEFAULT '',
            street TEXT DEFAULT '',
            street_type TEXT DEFAULT '',
            hous TEXT DEFAULT '',
            post_index TEXT DEFAULT '',
            partner TEXT DEFAULT '',
            status TEXT DEFAULT '',
            register TEXT DEFAULT '',
            edrpou TEXT DEFAULT '',
            address TEXT DEFAULT '',
            partner_name TEXT DEFAULT '',
            id_terminal TEXT DEFAULT '',
            koatu TEXT DEFAULT '',
            tax_id TEXT DEFAULT '',
            koatu2 TEXT DEFAULT ''
            )""")
    
print('departments ok')

#_____________________________________

db_exec("""
            CREATE TABLE IF NOT EXISTS otbor (
            term TEXT PRIMARY KEY DEFAULT '',
            dep TEXT DEFAULT ''
            )""")

print('otbor ok')

#______________________________

db_exec("""
            CREATE TABLE IF NOT EXISTS logi (
            department TEXT DEFAULT '',
            termial TEXT DEFAULT '',
            serial_number TEXT DEFAULT '',
            address TEXT DEFAULT '',
            datalog TEXT DEFAULT '',
            kind TEXT DEFAULT ''
            )""")

print('ok')



