from backend.rdf import *

# list_provinsi = [
#     'Aceh',
#     'Sumatera Utara',
#     'Sumatera Barat',
#     'Riau',
#     'Jambi',
#     'Sumatera Selatan',
#     'Bengkulu',
#     'Lampung',
#     'Kepulauan Bangka Belitung',
#     'Kepulauan Riau',
#     'Daerah Khusus Ibukota Jakarta',
#     'Jawa Barat',
#     'Jawa Tengah',
#     'DI Yogyakarta',
#     'Jawa Timur',
#     'Banten',
#     'Bali',
#     'Nusa Tenggara Barat',
#     'Nusa Tenggara Timur',
#     'Kalimantan Barat',
#     'Kalimantan Tengah',
#     'Kalimantan Selatan',
#     'Kalimantan Timur',
#     'Kalimantan Utara',
#     'Sulawesi Utara',
#     'Sulawesi Tengah',
#     'Sulawesi Selatan',
#     'Sulawesi Tenggara',
#     'Gorontalo',
#     'Sulawesi Barat',
#     'Maluku',
#     'Maluku Utara',
#     'Papua Barat',
#     'Papua'
# ]


def build_header_tabel(*nama_kolom):
    tabel = '<table class="highlight"><thead><tr>'
    for i in range(len(nama_kolom)):
        tabel += '<th>%s</th>' % nama_kolom[i]
    tabel += '</tr></thead><tbody>'
    return tabel


def build_cell_tabel(data, flag_is_linked, uri):
    if flag_is_linked:
        if ('Swasta/Lainnya' in uri):
            uri = uri.replace('Swasta/Lainnya', 'Swasta_Lainnya')
        cell = '<td><a href="%s">%s</a></td>' % (uri, data)
    else:
        cell = '<td>%s</td>' % data
    return cell


def get_seluruh_provinsi():
    result = query_list_all_provinsi()
    sorted_result = {}
    list_provinsi = []
    for key, value in sorted(result.items(), key=lambda item: (item[1], item[0])):
        sorted_result[key] = value
        list_provinsi.append(value)
    return list_provinsi


def get_seluruh_rs(provinsi):
    list_rs = query_list_all_rs(provinsi)
    # print(list_rs)
    return list_rs


def get_tabel_pengelola(provinsi):
    result = query_pengelola(provinsi)
    list_pengelola = []
    list_jumlah = []
    list_uri = []
    for i in result:
        list_pengelola.append(i['pengelola_name'])
        list_jumlah.append(i['hospital_count'])
        list_uri.append(i['pengelola_iri'])
    # build tabel
    size = len(list_pengelola)
    tabel = build_header_tabel('Pengelola', 'Jumlah Rumah Sakit')

    for i in range(size):
        tabel += '<tr>%s' % build_cell_tabel(
            list_pengelola[i], True, list_pengelola[i])
        tabel += '%s</tr>' % build_cell_tabel(list_jumlah[i], False, None)
    tabel += '</tbody></table>'
    return tabel


def get_tabel_tipe_kelas(provinsi):
    result = query_tipe_kelas(provinsi)
    list_kelas = []
    list_jumlah = []
    list_uri = []
    for i in result:
        list_kelas.append(i['class_name'])
        list_jumlah.append(i['hospital_count'])
        list_uri.append(i['class_iri'])
    # build tabel
    size = len(list_kelas)
    tabel = build_header_tabel('Tipe Kelas', 'Jumlah Rumah Sakit')

    for i in range(size):
        url = '/data-rs/%s/kelas-rs/%s' % (provinsi, list_kelas[i])
        tabel += '<tr>%s' % build_cell_tabel(
            list_kelas[i], True, url)
        tabel += '%s</tr>' % build_cell_tabel(list_jumlah[i], False, None)
    tabel += '</tbody></table>'
    return tabel


def get_rs_pengelola(pengelola, provinsi):
    result = query_rs_pengelola(pengelola, provinsi)
    print(result)
    list_nama = []
    list_uri = []
    for i in result:
        list_nama.append(i['hospital_name'])
        list_uri.append(i['hospital_iri'])
    # build tabel
    size = len(list_nama)
    tabel = build_header_tabel('Nama Rumah Sakit')

    for i in range(size):
        url = '/data-rs/detail/%s' % list_nama[i]
        print('url %s' % url)
        tabel += '<tr>%s</tr>' % build_cell_tabel(
            list_nama[i], True, url)
    tabel += '</tbody></table>'
    return tabel


def get_tabel_rs(provinsi):
    result = query_rs(provinsi)
    list_nama = []
    list_tipe = []
    list_kelas = []
    list_pengelola = []
    list_wilayah = []
    for i in result:
        list_nama.append(i['hospital_name'])
        list_tipe.append(i['type_name'])
        list_kelas.append(i['class_name'])
        list_pengelola.append(i['pengelola_name'])
        list_wilayah.append(i['region_name'])
    # build tabel
    size = len(list_nama)
    tabel = build_header_tabel('Nama', 'Tipe', 'Kelas', 'Pengelola', 'Wilayah')

    for i in range(size):
        url_nama = '/data-rs/detail/%s' % list_nama[i]
        url_tipe = '/data-rs/%s/tipe-rs/%s' % (provinsi, list_tipe[i])
        url_kelas = '/data-rs/%s/kelas-rs/%s' % (provinsi, list_kelas[i])
        url_pengelola = '%s/%s' % (provinsi, list_pengelola[i])

        tabel += '<tr>%s' % build_cell_tabel(list_nama[i], True, url_nama)
        tabel += build_cell_tabel(list_tipe[i], True, url_tipe)
        tabel += build_cell_tabel(list_kelas[i], True, url_kelas)
        tabel += build_cell_tabel(list_pengelola[i], True, url_pengelola)
        tabel += '%s</tr>' % build_cell_tabel(list_wilayah[i], False, None)
    tabel += '</tbody></table>'
    return tabel


def get_detail_rs(rumah_sakit):
    data = query_detail_rs(rumah_sakit)
    return data


def get_tabel_tipe_rs(tipe_rs, provinsi):
    result = query_tipe_rs(tipe_rs, provinsi)
    list_nama = []
    list_uri = []
    for i in result:
        list_nama.append(i['hospital_name'])
        list_uri.append(i['hospital_iri'])
    # build tabel
    size = len(list_nama)
    tabel = build_header_tabel('Nama Rumah Sakit')

    for i in range(size):
        url = '/data-rs/detail/%s' % list_nama[i]
        print('url %s' % url)
        tabel += '<tr>%s</tr>' % build_cell_tabel(
            list_nama[i], True, url)
    tabel += '</tbody></table>'
    return tabel


def get_tabel_kelas_rs(kelas_rs, provinsi):
    result = query_kelas_rs(kelas_rs, provinsi)
    list_nama = []
    list_uri = []
    for i in result:
        list_nama.append(i['hospital_name'])
        list_uri.append(i['hospital_iri'])
    # build tabel
    size = len(list_nama)
    tabel = build_header_tabel('Nama Rumah Sakit')

    for i in range(size):
        url = '/data-rs/detail/%s' % list_nama[i]
        print('url %s' % url)
        tabel += '<tr>%s</tr>' % build_cell_tabel(
            list_nama[i], True, url)
    tabel += '</tbody></table>'
    return tabel
