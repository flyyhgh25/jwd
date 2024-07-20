import os
import datetime
from flask import Flask, render_template,session,send_file,request, Response,redirect, url_for,make_response,flash
from werkzeug.utils import secure_filename
from flask_paginate import Pagination,get_page_args
from datetime import datetime
import string
from http import HTTPStatus
from model.Pelatihan import Pelatihan, ValidasiPelatihan
from model.Pendaftaran import Pendaftaran, ValidasiPendaftaran

app= Flask(__name__)

# handle file upload
app.config['SECRET_KEY'] = '@#123456&*()'
UPLOAD_FOLDER = 'static/images/uploads/'
ALLOWED_EXTENSIONS = {'webp','jpg', 'jpeg','png','gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# handle navigation
navbar = [
        ('/','Home','home-outline'),
        ('/pendaftaran','Pendaftaran','fas fa-people-arrows'),
        ('/pendaftaran','Pendaftar','fas fa-plus'),
        ('/pelatihan','Pelatihan','fas fa-plus'),
]

navbarAdmin = [
        ('/dataPendaftaran','Data Pendaftaran','home-outline'),
        ('/DataProgram','Data Program','fas fa-people-arrows'),
]

# Inisialisasi ITems

@app.route('/', methods=['GET'])
def index():
    pelatihan = Pelatihan()
    pelatihans =pelatihan.index()
    def get_pelatihans(offset=0, per_page=5):
        return pelatihans[offset: offset + per_page]
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    total = len(pelatihans)
    pagination_pelatihan= get_pelatihans(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,record_name='Pelatihan')
    return render_template('index.html',nav=navbar, pelatihans=pagination_pelatihan,per_page=per_page,page=page,pagination=pagination)

@app.route('/pelatihan', methods=['GET'])
def pelatihan():
    pelatihan = Pelatihan()
    form = ValidasiPelatihan()
    errors = form.errors.items
    pelatihans =pelatihan.index()
    def get_pelatihans(offset=0, per_page=5):
        return pelatihans[offset: offset + per_page]
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    total = len(pelatihans)
    pagination_pelatihan= get_pelatihans(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,record_name='Pelatihan')
    return render_template('pelatihan/index.html',nav=navbar,pelatihans=pagination_pelatihan,per_page=per_page,page=page,pagination=pagination)

@app.route('/createPelatihan', methods=['GET','POST'])
def createPelatihan():
    pelatihan = Pelatihan()
    pelatihanItem = Pelatihan()
    form = ValidasiPelatihan()
    errors = form.errors.items
    if request.method == 'POST':
        pelatihans =pelatihan.index()
        if form.validate_on_submit():
            gambar_pelatihan = form.gambar_pelatihan.data
            judul = form.judul.data
            nama_pelatihan = form.nama_pelatihan.data
            deskripsi = form.deskripsi.data
            if gambar_pelatihan and allowed_file(gambar_pelatihan.filename):
                filename = secure_filename(gambar_pelatihan.filename)
                gambar_pelatihan.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                data = (judul,filename,nama_pelatihan,deskripsi)
                pelatihanItem.create(data)
                print(data)
                return redirect(url_for('pelatihan'))
            print("cek")
        return render_template('pelatihan/create.html',nav=navbar, form=form, errors=errors)
    return render_template('pelatihan/create.html',nav=navbar, form=form)

@app.route('/updatePelatihan/<id>', methods=["GET","POST"], endpoint="updatePelatihan")
def updatePelatihan(id):
    pelatihans = Pelatihan()
    form = ValidasiPelatihan()
    errors = form.errors.items
    pelatihan = pelatihans.edit(id)[0]
    if pelatihan[0]!=None:
        if request.method == 'POST':
            if form.validate_on_submit():
                gambar_pelatihan = form.gambar_pelatihan.data
                nama_pelatihan = form.nama_pelatihan.data
                judul = form.judul.data
                deskripsi = form.deskripsi.data
                if gambar_pelatihan and allowed_file(gambar_pelatihan.filename):
                    filename = secure_filename(gambar_pelatihan.filename)
                    gambar_pelatihan.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    data = (judul, gambar_pelatihan, nama_pelatihan, deskripsi,id)
                    pelatihan.update(data)
                    print(data)
                    return redirect(url_for('pelatihan'))
                return render_template('pelatihan/edit.html',nav=navbar,form=form, pelatihan=pelatihan )
            return render_template('pelatihan/edit.html',nav=navbar,form=form, pelatihan=pelatihan )
        else:
            print("Isis ", pelatihan)
            form.judul.data = pelatihan[1]
            form.gambar_pelatihan.data = pelatihan[2]
            form.nama_pelatihan.data = pelatihan[3]
            form.deskripsi.data = pelatihan[4]
            return render_template('pelatihan/edit.html',nav=navbar,form=form, pelatihan=pelatihan )
           
            
@app.route('/deletePelatihan/<id>')
def deletePelatihan(id):
    pelatihan = Pelatihan()
    pelatihan = pelatihan.delete(id)
    return redirect(url_for('pelatihan'))


# PENDAFTARAN

@app.route('/pendaftaran', methods=['GET'])
def pendaftaran():
    pendaftaran = Pendaftaran()
    form = ValidasiPendaftaran()
    errors = form.errors.items
    pendaftarans =pendaftaran.index()
    def get_pendaftarans(offset=0, per_page=5):
        return pendaftarans[offset: offset + per_page]
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    total = len(pendaftarans)
    pagination_pendaftaran= get_pendaftarans(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,record_name='Pelatihan')
    return render_template('pendaftaran/index.html',nav=navbar,pendaftarans=pagination_pendaftaran,per_page=per_page,page=page,pagination=pagination)

@app.route('/createPendaftaran', methods=['GET','POST'])
def createPendaftaran():
    pendaftaran= Pendaftaran()
    form = ValidasiPendaftaran()
    errors = form.errors.items
    if request.method == 'POST':
        if form.validate_on_submit():
            nama_lengkap = form.nama_lengkap.data
            nik = form.nik.data
            no_whatsapp = form.no_whatsapp.data
            email = form.email.data
            id_pelatihan = form.id_pelatihan.data
            data = (nama_lengkap, nik, no_whatsapp, email, id_pelatihan)
            pendaftaran.create(data)
            print(data)
            return redirect(url_for('pelatihan'))
        return render_template('pendaftaran/create.html',nav=navbar, form=form, errors=errors)
    return render_template('pendaftaran/create.html',nav=navbar, form=form)

@app.route('/updatePendaftaran/<id>', methods=["GET","POST"], endpoint="updatePendaftaran")
def updatePendaftaran(id):
    pendaftarans = Pendaftaran()
    form = ValidasiPendaftaran()
    errors = form.errors.items
    pendaftaran = pendaftarans.edit(id)[0]
    print("Cekdarar",pendaftaran)
    if pendaftaran[0]!=None:
        if request.method == 'POST':
            if form.validate_on_submit():
                nama_lengkap = form.nama_lengkap.data
                nik = form.nik.data
                no_whatsapp = form.no_whatsapp.data
                email = form.email.data
                id_pelatihan = form.id_pelatihan.data
                data = (nama_lengkap, nik, no_whatsapp, email, id_pelatihan,id)
                pendaftarans.update(data)
                print(data)
                return redirect(url_for('pendaftaran'))
            return render_template('pelatihan/edit.html',nav=navbar,form=form, pendaftaran=pendaftaran )
        else:
            form.nama_lengkap.data = pendaftaran[2]
            form.nik.data = pendaftaran[3]
            form.no_whatsapp.data = pendaftaran[4]
            form.email.data = pendaftaran[5]
            form.id_pelatihan.data = pendaftaran[2]
            return render_template('pendaftaran/edit.html',nav=navbar,form=form, pendaftaran=pendaftaran )
           
            
@app.route('/deletePendaftaran/<id>')
def deletePendaftaran(id):
    pendaftaran = Pendaftaran()
    pendaftaran = pendaftaran.delete(id)
    return redirect(url_for('pendaftaran'))
  

if __name__ == '__main__':
    app.run(debug=True)
