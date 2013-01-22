#!/usr/bin/python
# encoding=utf-8
#author: Wiszhou
#date: 2013.1.20

'''
人才资源管理系统， 提供人才数据录入， 修改，删除， 查询， 排序等功能。
查询支持全字段模糊搜索。
'''

import MySQLdb as mysql

CONN = mysql.connection(host='192.168.1.101', user='root', passwd='meego', port=3306, db='test')

class Talent:
	def __init__(self):
		CONN.query('CREATE TABLE IF NOT EXISTS talent(id int(8), name varchar(20), PRIMARY KEY (id))')
		return


if __name__=='__main__':
	my_talent = Talent()
