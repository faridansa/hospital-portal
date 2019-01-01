from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from backend.utils import *

app = Flask(__name__)
app._static_folder = 'static/'


@app.route("/", methods=['POST', 'GET'])
def index():
    print('INDEX')
    data_provinsi = get_seluruh_provinsi()
    if request.method == 'GET':
        return render_template('homepage.html', provinsi=data_provinsi)
    else:
        selected_provinsi = request.form.get('dropdown')
        return redirect(url_for('data_rs_provinsi', provinsi=selected_provinsi))


@app.route("/data-rs/<provinsi>/pengelola")
def data_rs_provinsi(provinsi):
    print('DATA_RS_PROV')
    tabel_pengelola = get_tabel_pengelola(provinsi)
    tabel_tipe_kelas = get_tabel_tipe_kelas(provinsi)
    return render_template('data-rs-provinsi.html', provinsi=provinsi, tabel_pengelola=tabel_pengelola, tabel_tipe_kelas=tabel_tipe_kelas)


@app.route("/data-rs/<provinsi>/<pengelola>")
def data_rs_pengelola(provinsi, pengelola):
    print('DATA_RS_PENGELOLA')
    if '_' in pengelola:
        pengelola = pengelola.replace('_', '/')
    tabel = get_rs_pengelola(pengelola, provinsi)
    # tabel = None
    return render_template('data-rs-pengelola.html', provinsi=provinsi, pengelola=pengelola, tabel_pengelola=tabel)


@app.route("/data-rs/<provinsi>")
def data_rs(provinsi):
    print('DATA_RS')
    # tabel = get_seluruh_rs(provinsi)
    tabel = None
    return render_template('data-rs.html', provinsi=provinsi, tabel_rs=tabel)


@app.route("/data-rs/detail/<rumah_sakit>")
def detail_rs(rumah_sakit):
    print('DETAIL_RS')
    data = get_detail_rs(rumah_sakit)
    # data = None
    return render_template('detail-rs.html', rumah_sakit=rumah_sakit, detail=data)


@app.route("/data-rs/<provinsi>/tipe-rs/<tipe_rs>")
def tipe_rs(provinsi, tipe_rs):
    print('TIPE_RS')
    tabel = get_tabel_tipe_rs(tipe_rs, provinsi)
    # tabel = None
    return render_template('tipe-rs.html', provinsi=provinsi, tipe_rs=tipe_rs, tabel_tipe_rs=tabel)


@app.route("/data-rs/<provinsi>/kelas-rs/<kelas_rs>")
def kelas_rs(provinsi, kelas_rs):
    print('KELAS_RS')
    tabel = get_tabel_kelas_rs(kelas_rs, provinsi)
    # tabel = None
    return render_template('kelas-rs.html', provinsi=provinsi, kelas_rs=kelas_rs, tabel_kelas_rs=tabel)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
