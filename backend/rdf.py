import rdflib


def get_query(file_name, query):
    g = rdflib.Graph()
    g.parse(file_name, format="nt")
    query_result = g.query(query)
    return query_result


def test(result):
    for row in result:
        print(row)


def query_list_all_rs(provinsi):
    # contoh template
    file_name = 'data-rs-all.nt'
    query = """
    SELECT ?alamat
    WHERE { ?nama_rs <http://0.0.0.0:8080/dataRS#ALAMAT> ?alamat
    }"""
    result = get_query(file_name, query)
    return result


def query_statistik_tenaga_medis(provinsi):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_tipe_perawatan(provinsi):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_pengelola(provinsi):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_tipe_kelas(provinsi):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_rs_pengelola(pengelola, provinsi):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_rs(provinsi):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_detail_rs(rumah_sakit):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_tipe_rs(tipe_rs, provinsi):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_kelas_rs(kelas_rs, provinsi):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_rs_wilayah(wilayah):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


def query_detail_puskesmas(puskesmas):
    file_name = None
    query = """
    """
    result = get_query(file_name, query)
    return result


if __name__ == '__main__':
    res = query_list_all_rs('Aceh')
    # if you want to see the result
    test(res)
