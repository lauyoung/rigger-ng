#coding=utf8
import re , os , logging
import utls.dbc
import json
import interface
from utls.rg_io import rg_logger

def load_file(jsonfile,xpath= None) :
    if len(xpath) == 0 :
        xpath = "/"
    utls.dbc.must_exists(jsonfile)
    doc = open(jsonfile,"r").read()
    try :
        data = json.loads(doc)
        arr = xpath.split("/")
        for key in arr :
            if len(key) == 0 :
                continue
            data = data[key]
            utls.dbc.not_none(data, "data[%s] not exists" %key)
        return data
    except :
        raise interface.rigger_exception("bad json file %s" %jsonfile )



