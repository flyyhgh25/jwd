import pymysql
import config
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import  InputRequired,Length
from flask_wtf.file import FileField,FileAllowed
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

class Pelatihan:
    def __init__(self,judul=None,gambar_pelatihan=None,nama_pelatihan=None,deskripsi=None):
        self.judul = judul
        self.gambar_pelatihan = gambar_pelatihan
        self.nama_pelatihan = nama_pelatihan
        self.deskripsi = deskripsi
    def index(self):
        openDB()
        cursor.execute("SELECT * FROM pelatihans")
        data = cursor.fetchall()
        return data  
    def create(self,data):
        openDB()
        cursor.execute("INSERT INTO pelatihans(judul,gambar_pelatihan,nama_pelatihan,deskripsi) VALUES('%s','%s','%s','%s')"%data)
        db.commit()
        closeDB()
    def edit(self, id):
        openDB()
        cursor.execute("SELECT * FROM pelatihans WHERE id='%s'"%id)
        data=cursor.fetchall()
        closeDB()
        return data  
    def update(self,data):
        openDB()
        cursor.execute("UPDATE pelatihans SET judul='%s',gambar_pelatihan='%s',nama_pelatihan='%s',deskripsi='%s' WHERE id=%s"%data)
        db.commit()
        closeDB()
    def delete(self,id):
        openDB()
        cursor.execute("DELETE FROM pelatihans WHERE id='%s'"%id)
        db.commit()
        closeDB()
class ValidasiPelatihan(FlaskForm):
        judul = StringField('Judul',validators =[InputRequired('Judul harus diisi!'), Length(min=1,max=25)])
        gambar_pelatihan = FileField('Gambar Pelatihan',validators =[InputRequired('Gambar pelatihan harus diisi!'),FileAllowed(['jpg', 'png','webp','jpeg'], 'Images only!')])
        nama_pelatihan = StringField('Nama Pelatihan',validators =[InputRequired('Nama pelatihan harus diisi!'), Length(min=5,max=25)])
        deskripsi = TextAreaField('Deskripsi Pelatihan',validators =[InputRequired('Deskripsi pelatihan harus diisi!')])
    
    
