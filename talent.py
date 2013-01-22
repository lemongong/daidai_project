#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: LemonGong
#date: 2013-1-20


''' note: This is doc comment character.  The talent manager system,
use to CDUT and serch fields in DB'''

import MySQLdb as mysql

CONN = mysql.connection(host='192.168.1.101', user='root', passwd='meego', port=3306, db='test')

class Talent:
    def __init__(self):
        CONN.query('CREATE TABLE IF NOT EXISTS talent(id int(8), name varchar(20), PRIMARY KEY(id),iq int(8),power int(8),charm int(8),hobby varchar(20),note varchar(30))')
        #CONN.query('ALTER TABLE talent ADD iq int(8),ADD power int(8),ADD charm int(8),ADD hobby varchar(20),ADD note varchar(30)')
        return
    
if __name__=='__main__':
    my_talent = Talent()
