from flask import Flask, flash, redirect, render_template, request, session, abort
from backend.utils import *

app = Flask(__name__)
app._static_folder = 'static/'


@app.route("/", methods=['POST', 'GET'])
def index():
    data_provinsi = get_seluruh_provinsi()
    if request.method == 'GET':
        return render_template('homepage.html', provinsi=data_provinsi)
    else:
        selected_provinsi = request.form.get('dropdown')
        return data_rs_provinsi_pengelola(selected_provinsi)

#
# @app.route("/data-rs/<provinsi>/statistik-tenaga-medis")
# def data_rs_provinsi_statisik_tenaga_medis(provinsi):
#     tabel = get_tabel_statistik_tenaga_medis(provinsi)
#     return render_template('data-rs-provinsi.html', provinsi=provinsi, tabel_stm=tabel)
#
#
# @app.route("/data-rs/<provinsi>/tipe-perawatan")
# def data_rs_provinsi_tipe_perawatan(provinsi):
#     tabel = get_tipe_perawatan(provinsi)
#     return render_template('data-rs-provinsi.html', provinsi=provinsi, tabel_tipe_perawatan=tabel)


# tabel_tipe_kelas belum ada masuk ke parameter
# namun sepertinya ku butuh untuk tampilin di 
# data-rs-provinsi.html tab 'tipe kelas'
@app.route("/data-rs/<provinsi>/pengelola")
def data_rs_provinsi_pengelola(provinsi):
    # tabel = get_tabel_pengelola(provinsi)
    tabel = None
    return render_template('data-rs-provinsi.html', provinsi=provinsi, tabel_pengelola=tabel)


@app.route("/data-rs/<provinsi>/<pengelola>")
def data_rs_pengelola(provinsi, pengelola):
    # tabel = get_rs_pengelola(pengelola, provinsi)
    tabel = None
    return render_template('data-rs-pengelola.html', provinsi=provinsi, pengelola=pengelola, tabel_pengelola=tabel)


@app.route("/data-rs/<provinsi>")
def data_rs(provinsi):
    # tabel = get_seluruh_rs(provinsi)
    tabel = None
    return render_template('data-rs.html', provinsi=provinsi, tabel_rs=tabel)


@app.route("/data-rs/detail/<rumah_sakit>")
def detail_rs(rumah_sakit):
    # data = get_detail_rs(rumah_sakit)
    data = None
    return render_template('detail-rs.html', rumah_sakit=rumah_sakit, detail=data)


@app.route("/data-rs/<provinsi>/tipe-rs/<tipe_rs>")
def tipe_rs(provinsi, tipe_rs):
    # tabel = get_tabel_tipe_rs(tipe_rs, provinsi)
    tabel = None
    return render_template('tipe-rs.html', provinsi=provinsi, tipe_rs=tipe_rs, tabel_tipe_rs=tabel)


@app.route("/data-rs/<provinsi>/kelas-rs/<kelas_rs>")
def kelas_rs(provinsi, kelas_rs):
    # tabel = get_tabel_kelas_rs(kelas_rs, provinsi)
    tabel = None
    return render_template('kelas-rs.html', provinsi=provinsi, kelas_rs=kelas_rs, tabel_kelas_rs=tabel)

#
# @app.route("/data-rs/<wilayah>/jumlah-rs")
# def jumlah_kamar_rs(wilayah):
#     jumlah_kamar, tabel = get_tabel_rs_jumlah_kamar(wilayah)
#     return render_template('jumlah-kamar.html', wilayah=wilayah, jumlah_kamar=jumlah_kamar, tabel_rs=tabel)
#
#
# @app.route("/data-puskesmas/detail/<puskesmas>")
# def detail_puskesmas(puskesmas):
#     data = get_detail_puskesmas(puskesmas)
#     return render_template('detail-puskesmas.html', puskesmas=puskesmas, detail=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
