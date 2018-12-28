from backend.rdf import *

list_provinsi = [
    'Aceh',
    'Sumatera Utara',
    'Sumatera Barat',
    'Riau',
    'Jambi',
    'Sumatera Selatan',
    'Bengkulu',
    'Lampung',
    'Kepulauan Bangka Belitung',
    'Kepulauan Riau',
    'DKI Jakarta',
    'Jawa Barat',
    'Jawa Tengah',
    'DI Yogyakarta',
    'Jawa Timur',
    'Banten',
    'Bali',
    'Nusa Tenggara Barat',
    'Nusa Tenggara Timur',
    'Kalimantan Barat',
    'Kalimantan Tengah',
    'Kalimantan Selatan',
    'Kalimantan Timur',
    'Kalimantan Utara',
    'Sulawesi Utara',
    'Sulawesi Tengah',
    'Sulawesi Selatan',
    'Sulawesi Tenggara',
    'Gorontalo',
    'Sulawesi Barat',
    'Maluku',
    'Maluku Utara',
    'Papua Barat',
    'Papua'
]


def build_tabel(*kolom):
    data = kolom[-1]
    tabel = '<table><tr>'
    for i in kolom:
        if i != data:
            tabel += '<th>%s</th>' % i
    tabel += '</tr>'
    for row in data:
        # print(row)
        tabel += '<tr>'
        for i in row:
            # print(i + '\n')
            tabel += '<th>%s</th>' % i
        tabel += '</tr>'
    tabel += '</tabel>'
    print(tabel)


def get_seluruh_provinsi():
    return list_provinsi


def get_seluruh_rs(provinsi):
    list_rs = query_list_all_rs(provinsi)
    return list_rs


def get_tabel_statistik_tenaga_medis(provinsi):
    data = query_statistik_tenaga_medis(provinsi)
    tabel = build_tabel('Jumlah Rumah Sakit', 'Jumlah Dokter Spesialis',
                        'Jumlah Dokter Gigi', 'Jumlah Dokter Umum', 'Jumlah Perawat', 'Jumlah Bidan', data)
    return tabel


def get_tabel_tipe_perawatan(provinsi):
    data = query_tipe_perawatan(provinsi)
    tabel = build_tabel('Tipe Perawatan', 'Jumlah Kamar', data)
    return tabel


def get_tabel_pengelola(provinsi):
    data = query_pengelola(provinsi)
    tabel = build_tabel('Pengelola', 'Jumlah RS', 'Jumlah Tempat Tidur', data)
    return tabel


def get_tabel_tipe_kelas(provinsi):
    data = query_tipe_kelas(provinsi)
    tabel = build_tabel('Tipe Kelas', 'Jumlah RS', 'Jumlah Tempat Tidur', data)
    return tabel


def get_rs_pengelola(pengelola, provinsi):
    data = query_rs_pengelola(pengelola, provinsi)
    tabel = build_tabel('Nama RS', data)
    return tabel


def get_tabel_rs(provinsi):
    data = query_rs(provinsi)
    tabel = build_tabel('Nama', 'Tipe', 'Kelas', 'Pengelola', 'Wilayah', data)
    return tabel


def get_detail_rs(rumah_sakit):
    data = query_detail_rs(rumah_sakit)
    return data


def get_tabel_tipe_rs(tipe_rs, provinsi):
    data = query_tipe_rs(tipe_rs, provinsi)
    tabel = build_tabel('Nama RS', data)
    return tabel


def get_tabel_kelas_rs(kelas_rs, provinsi):
    data = query_kelas_rs(kelas_rs, provinsi)
    tabel = build_tabel('Nama RS',
                        data)
    return tabel


def get_tabel_rs_jumlah_kamar(wilayah):
    data = query_rs_wilayah(wilayah)
    tabel = build_tabel('Nama RS', data)
    jumlah_kamar = len(data)
    return (jumlah_kamar, tabel)


def get_detail_puskesmas(puskesmas):
    data = query_detail_puskesmas(puskesmas)
    return data


# build_tabel('Nama', 'Tipe', 'Kelas', 'Pengelola', 'Wilayah', (
#             ['A', 'RSJ', 'A', 'Swasta', 'Wilayah'], ['B', 'RSJ', 'A', 'Swasta', 'Wilayah']))


# def get_stm_jumlah_dokter_spesialis(provinsi):
#     return None
#
#
# def get_stm_jumlah_dokter_gigi(provinsi):
#     return None
#
#
# def get_stm_jumlah_perawat(provinsi):
#     return None
#
#
# def get_stm_jumlah_bidan(provinsi):
#     return None
#
#
# def get_tipe_perawatan(provinsi):
#     return None
#
#
# def get_tipe_perawatan_jumlah_kamar(provinsi):
#     return None
#
#
# def get_pengelola(provinsi):
#     return None
#
#
# def get_pengelola_jumlah_tempat_tidur(provinsi):
#     return None
#
#
# def get_pengelola_jumlah_rs(provinsi):
#     return None
#
#
# def get_tipe_kelas(provinsi):
#     return None
#
#
# def get_tipe_kelas_jumlah_tempat_tidur(provinsi):
#     return None
#
#
# def get_tipe_kelas_jumlah_tempat_rs(provinsi):
#     return None
#
# def get_rs(pengelola, provinsi):
#     return None
