
CREATE TABLE IF NOT EXISTS terminals
(
    department text NOT NULL,
    termial text,
    model text DEFAULT '',
    serial_number text,
    date_manufacture text DEFAULT '',
    soft text DEFAULT '',
    producer text DEFAULT 'ДАТЕКС ООД',
    rne_rro text DEFAULT '',
    sealing text DEFAULT '',
    fiscal_number text DEFAULT '',
    oro_serial text DEFAULT '',
    oro_number text DEFAULT '1',
    ticket_serial text DEFAULT '',
    ticket_1sheet text DEFAULT '',
    ticket_number text DEFAULT '1',
    sending text DEFAULT '',
    books_arhiv text DEFAULT '',
    tickets_arhiv text DEFAULT '',
    to_rro text DEFAULT 'ТОВ ПОС',
    owner_rro text DEFAULT '',
    register text DEFAULT '',
    finish text DEFAULT '',
    PRIMARY KEY (termial, serial_number)
);

CREATE TABL IF NOT EXISTS departments
(
    department text NOT NULL DEFAULT '',
    region text DEFAULT '',
    district_region text DEFAULT '',
    district_city text DEFAULT '',
    city_type text DEFAULT '',
    city text DEFAULT '',
    street text DEFAULT '',
    street_type text DEFAULT '',
    hous text DEFAULT '',
    post_index text DEFAULT '',
    partner text DEFAULT '',
    status text DEFAULT '',
    register text DEFAULT '',
    edrpou text DEFAULT '',
    address text DEFAULT '',
    partner_name text DEFAULT '',
    id_terminal text DEFAULT '',
    koatu text DEFAULT '',
    tax_id text DEFAULT '',
    koatu2 text DEFAULT '',
    PRIMARY KEY (department)
);

CREATE TABL IF NOT EXISTS departments
(
    term TEXT DEFAULT '',
    dep TEXT DEFAULT ''
    PRIMARY KEY (department)
);





DROP TABLE IF EXISTS departments;
CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department TEXT DEFAULT '',
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
);

DROP TABLE IF EXISTS terminals;
CREATE TABLE terminals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department TEXT DEFAULT '',
    termial TEXT DEFAULT '',
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
);

DROP TABLE IF EXISTS otbor;
CREATE TABLE otbor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    term TEXT DEFAULT '',
    dep TEXT DEFAULT ''
);

DROP TABLE IF EXISTS logi;
CREATE TABLE logi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department TEXT DEFAULT '',
    termial TEXT DEFAULT '',
    serial_number TEXT DEFAULT '',
    address TEXT DEFAULT '',
    datalog TEXT DEFAULT '',
    kind TEXT DEFAULT ''
);


            