import pymysql
import config
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SelectField
from wtforms.validators import  InputRequired,Length
from model.Pelatihan import Pelatihan
db = cursor = None
db,cursor
def openDB():
    global db, cursor
    db = pymysql.connect(
        host = config.host,
        user = config.user,
        password=config.pwd,
        database=config.name
	)
    cursor = db.cursor()
def closeDB():
    global db, cursor
    db.close()

class Pendaftaran:
    def __init__(self,nama_lengkap=None,nik=None,no_whatsapp=None,email=None, id_pelatihan=None):
        self.nama_lengkap = nama_lengkap
        self.nik = nik
        self.no_whatsapp = no_whatsapp
        self.email = email
        self.id_pelatihan = id_pelatihan
    def index(self):
        openDB()
        cursor.execute("SELECT * FROM pendaftarans")
        data = cursor.fetchall()
        return data  
    def create(self,data):
        openDB()
        cursor.execute("INSERT INTO pendaftarans(nama_lengkap,nik,no_whatsapp,email, id_pelatihan) VALUES('%s','%s','%s','%s','%s')"%data)
        db.commit()
        closeDB()
    def edit(self, id):
        openDB()
        cursor.execute("SELECT * FROM pendaftarans WHERE id='%s'"%id)
        data=cursor.fetchall()
        closeDB()
        return data  
    def update(self,data):
        openDB()
        cursor.execute("UPDATE pendaftarans SET nama_lengkap='%s',nik='%s',no_whatsapp='%s',email='%s', id_pelatihan='%s' WHERE id=%s"%data)
        db.commit()
        closeDB()
    def delete(self,id):
        openDB()
        cursor.execute("DELETE FROM pendaftarans WHERE id='%s'"%id)
        db.commit()
        closeDB()
class ValidasiPendaftaran(FlaskForm):
        nama_lengkap = StringField('Nama Lengkap',validators =[InputRequired('Nama lengkap harus diisi!'), Length(min=1,max=25)])
        nik =IntegerField('NIK',validators =[InputRequired('NIK harus diisi!')])
        no_whatsapp = IntegerField('No Whatsapp',validators =[InputRequired('No Whatsapp harus diisi!')])
        email = StringField('Email',validators =[InputRequired('Email harus diisi!')])
        model = Pelatihan()
        data = model.index()
        id_pelatihan = SelectField('Pelatihan',choices=[ (p[0],p[3]) for p in data])
