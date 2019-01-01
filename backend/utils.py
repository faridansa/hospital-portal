from backend.rdf import *
import json

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
        cell = '<td><a href="#%s">%s</a></td>' % (uri, data)
    else:
        cell = '<td>%s</td>' % data
    return cell

    # size = len(kolom) - 1
    # data_uri = kolom[-2]
    # bool_is_linked = kolom[-1]
    # print(bool_is_linked)
    # index_data = int(size / 2)
    # size_data = len(data_uri)
    # tabel = '<table class="highlight"><thead><tr>'
    # for i in range(index_data):
    #     tabel += '<th>%s</th>' % kolom[i]
    # tabel += '</tr></thead><tbody>'
    #
    # for i in range(size_data):
    #     flag_linked = False
    #     # if (i < index_data) and (bool_is_linked[i]) and:
    #     tabel += '<tr>'
    #     # loop per row
    #     for data in range(index_data, size - 1):
    #         element = kolom[data][i]
    #         if flag_linked:
    #             print(element)
    #             # tabel += '<td> < a href = "#' + \
    #             #     data_uri[i] + '" > %s < /a > < / td >' % element
    #
    #         tabel += '<td>%s</td>' % element
    #     tabel += '</tr>'
    # tabel += '</tbody></table>'
    # return tabel


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
    # result = [{
    #     "label": "Organisasi Sosial",
    #     "hospital_count": "2",
    #     "uri": "http://0.0.0.0:8080/dataRS#Organisasi_Sosial"
    # }, {
    #     "label": "Swasta/Lainnya",
    #     "hospital_count": "4",
    #     "uri": "http://0.0.0.0:8080/dataRS#Swasta_Lainnya"
    # },
    #     {
    #     "label": "Kemkes",
    #         "hospital_count": "1",
    #         "uri": "http://0.0.0.0:8080/dataRS#Kemkes"
    # },
    #     {
    #     "label": "POLRI",
    #         "hospital_count": "1",
    #         "uri": "http://0.0.0.0:8080/dataRS#POLRI"
    # }]
    list_pengelola = []
    list_jumlah = []
    list_uri = []
    for i in result:
        list_pengelola.append(i['label'])
        list_jumlah.append(i['hospital_count'])
        list_uri.append(i['uri'])
    # build tabel
    size = len(list_pengelola)
    tabel = build_header_tabel('Pengelola', 'Jumlah Rumah Sakit')

    for i in range(size):
        tabel += '<tr>%s' % build_cell_tabel(
            list_pengelola[i], True, list_uri[i])
        tabel += '%s</tr>' % build_cell_tabel(list_jumlah[i], False, None)
    tabel += '</tbody></table>'
    return tabel


def get_tabel_tipe_kelas(provinsi):
    result = query_tipe_kelas(provinsi)
    # result = [
    #     {
    #         "label": "B",
    #         "hospital_count": "2",
    #         "uri": "http://0.0.0.0:8080/dataRS#B"
    #     },
    #     {
    #         "label": "C",
    #         "hospital_count": "3",
    #         "uri": "http://0.0.0.0:8080/dataRS#C"
    #     },
    #     {
    #         "label": "D",
    #         "hospital_count": "1",
    #         "uri": "http://0.0.0.0:8080/dataRS#D"
    #     },
    #     {
    #         "label": "A",
    #         "hospital_count": "2",
    #         "uri": "http://0.0.0.0:8080/dataRS#A"
    #     }
    # ]
    list_tipe = []
    list_jumlah = []
    list_uri = []
    for i in result:
        list_tipe.append(i['label'])
        list_jumlah.append(i['hospital_count'])
        list_uri.append(i['uri'])
    # build tabel
    size = len(list_tipe)
    tabel = build_header_tabel('Tipe Kelas', 'Jumlah Rumah Sakit')

    for i in range(size):
        tabel += '<tr>%s' % build_cell_tabel(
            list_tipe[i], True, list_uri[i])
        tabel += '%s</tr>' % build_cell_tabel(list_jumlah[i], False, None)
    tabel += '</tbody></table>'
    return tabel


def get_rs_pengelola(pengelola, provinsi):
    data = query_rs_pengelola(pengelola, provinsi)
    tabel = build_cell_tabel('Nama Rumah Sakit', data)
    return tabel


def get_tabel_rs(provinsi):
    data = query_rs(provinsi)
    tabel = build_cell_tabel('Nama', 'Tipe', 'Kelas', 'Pengelola',
                             'Wilayah', 'Kota/Kabupaten', data)
    return tabel


def get_detail_rs(rumah_sakit):
    data = query_detail_rs(rumah_sakit)
    return data


def get_tabel_tipe_rs(tipe_rs, provinsi):
    data = query_tipe_rs(tipe_rs, provinsi)
    tabel = build_cell_tabel('Nama Rumah Sakit', data)
    return tabel


def get_tabel_kelas_rs(kelas_rs, provinsi):
    data = query_kelas_rs(kelas_rs, provinsi)
    tabel = build_cell_tabel('Nama Rumah Sakit', data)
    return tabel
