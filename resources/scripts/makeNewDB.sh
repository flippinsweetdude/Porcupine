#!/bin/bash
## backup the existing db 
## make a new db
## build out the tables 
## insert if needed

# Backup if existing db
backup="archive/backup-$(date +"%d-%m-%Y-%M-%s").txt" 
#echo "$backup"
[ -f current.db ] && mv current.db $backup

# Make new sqlite db
sqlite3 current.db "create table network (id integer primary key autoincrement, addresses text, description text, isdeleted integer, createddate integer);"
sqlite3 current.db "create table devicenode (id integer primary key autoincrement, ipaddress text, macaddress text, network_id integer, isdeleted integer, createddate integer);"
sqlite3 current.db "create table scanresult (id integer primary key autoincrement, devicenode_id integer, port integer, isread integer, isdeleted integer, createddate integer);"
sqlite3 current.db "create table scanlog (id integer primary key autoincrement, devicenode_id integer, result text, isdeleted integer, createddate integer);"
sqlite3 current.db "create table log (id integer primary key autoincrement, isdebug integer, message text, isdeleted integer, createddate integer);"
sqlite3 current.db "create table job (id integer primary key autoincrement, job_type integer, startdate integer, enddate integer, jobstatus integer, jobjson text, isdeleted integer, createddate integer);"
sqlite3 current.db "create table setting (id integer primary key autoincrement, setting_type integer, setting_value text, last_upate integer, isdeleted integer, createddate integer);"

