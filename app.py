from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
app._static_folder = 'static/'


@app.route("/")
def index():
    return render_template('homepage.html')


@app.route("/data-rs/<provinsi>/statistik-tenaga-medis")
def data_rs_provinsi_statisik_tenaga_medis(provinsi):
    return render_template('data-rs-provinsi.html', provinsi=provinsi)


@app.route("/data-rs/<provinsi>/tipe-perawatan")
def data_rs_provinsi_tipe_perawatan(provinsi):
    return render_template('data-rs-provinsi.html', provinsi=provinsi)


@app.route("/data-rs/<provinsi>/pengelola")
def data_rs_provinsi_pengelola(provinsi):
    return render_template('data-rs-provinsi.html', provinsi=provinsi)


@app.route("/data-rs/<provinsi>/<pengelola>")
def data_rs_pengelola(provinsi, pengelola):
    return render_template('data-rs-pengelola.html', provinsi=provinsi, pengelola=pengelola)


@app.route("/data-rs/<provinsi>")
def data_rs(provinsi):
    return render_template('data-rs.html', provinsi=provinsi)


@app.route("/data-rs/detail/<rumah_sakit>")
def detail_rs(rumah_sakit):
    return render_template('detail-rs.html', rumah_sakit=rumah_sakit)


@app.route("/data-rs/<provinsi>/tipe-rs/<tipe_rs>")
def tipe_rs(provinsi, tipe_rs):
    return render_template('tipe-rs.html', provinsi=provinsi, tipe_rs=tipe_rs)


@app.route("/data-rs/<provinsi>/kelas-rs/<kelas_rs>")
def kelas_rs(provinsi, kelas_rs):
    return render_template('kelas-rs.html', provinsi=provinsi, kelas_rs=kelas_rs)


@app.route("/data-rs/<wilayah>/jumlah-rs")
def jumlah_kamar_rs(wilayah):
    return render_template('jumlah-kamar.html', wilayah=wilayah)


@app.route("/data-puskesmas/detail/<puskesmas>")
def detail_puskesmas(puskesmas):
    return render_template('detail-puskesmas.html', puskesmas=puskesmas)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
