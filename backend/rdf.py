import rdflib
import requests

url = 'https://query.wikidata.org/sparql'


def get_query(file_name, query):
    g = rdflib.Graph()
    g.parse(file_name, format="nt")
    query_result = g.query(query)
    return query_result


def test(result):
    for row in result:
        print(result[row])


def query_list_all_rs(provinsi):
    provinsi_link = []
    query = """
SELECT ?province WHERE {
?province <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q5098> .
?province <http://www.w3.org/2000/01/rdf-schema#label> \"""" + provinsi + """\"@id.}
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        provinsi_link.append(item['province']['value'])

    file_name = 'static/data/data-rs-all.nt'
    query = """
    SELECT ?hospital_label ?hospital WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?row <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_label.
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """>.
    }"""
    result = get_query(file_name, query)
    list_of_dict = []
    for row in result:
        d = {}
        d['iri'] = str(row.asdict()['hospital'].toPython())
        d['hospital_name'] = str(row.asdict()['hospital_label'].toPython())
        list_of_dict.append(d)

    query = """
SELECT DISTINCT ?hospital_label ?rs WHERE {
?rs <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q16917> .
?rs <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_label .
?rs <http://www.wikidata.org/prop/direct/P131> ?region.
?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """> . }
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        d = {}
        d['iri'] = item['rs']['value']
        d['hospital_name'] = item['hospital_label']['value']
        list_of_dict.append(d)
    return list_of_dict


def query_list_all_provinsi():
    result = {}
    query = """
SELECT ?province_name ?province WHERE {
?province <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q5098> .
?province <http://www.w3.org/2000/01/rdf-schema#label> ?province_name.
filter(lang(?province_name) = 'id')}
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        result[item['province']['value']] = item['province_name']['value']
    return result


def query_pengelola(provinsi):
    provinsi_link = []
    query = """
SELECT ?province WHERE {
?province <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q5098> .
?province <http://www.w3.org/2000/01/rdf-schema#label> \"""" + provinsi + """\"@id.}
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        provinsi_link.append(item['province']['value'])

    file_name = 'static/data/data-rs-all.nt'
    query = """
    SELECT ?pengelola ?pengelola_label (count(?hospital) as ?count) WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?hospital <http://0.0.0.0:8080/dataRS#PENYELENGGARA> ?pengelola.
    ?pengelola <http://www.w3.org/2000/01/rdf-schema#label> ?pengelola_label.
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """>.
    } GROUP BY ?pengelola"""

    result = get_query(file_name, query)
    list_of_dict = []
    for row in result:
        d = {}
        d['pengelola_iri'] = str(row.asdict()['pengelola'].toPython())
        d['pengelola_name'] = str(row.asdict()['pengelola_label'].toPython())
        d['hospital_count'] = str(row.asdict()['count'].toPython())
        list_of_dict.append(d)
    return list_of_dict


def query_tipe_kelas(provinsi):
    provinsi_link = []
    query = """
SELECT ?province WHERE {
?province <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q5098> .
?province <http://www.w3.org/2000/01/rdf-schema#label> \"""" + provinsi + """\"@id.}
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        provinsi_link.append(item['province']['value'])

    file_name = 'static/data/data-rs-all.nt'
    query = """
    SELECT ?class ?class_label (count(?hospital) as ?count) WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?hospital <http://0.0.0.0:8080/dataRS#KLS_RS> ?class.
    ?class <http://www.w3.org/2000/01/rdf-schema#label> ?class_label.
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """>.
    } GROUP BY ?class"""

    result = get_query(file_name, query)
    list_of_dict = []
    for row in result:
        d = {}
        d['class_iri'] = str(row.asdict()['class'].toPython())
        d['class_name'] = str(row.asdict()['class_label'].toPython())
        d['hospital_count'] = str(row.asdict()['count'].toPython())
        list_of_dict.append(d)
    return list_of_dict


def query_rs_pengelola(pengelola, provinsi):
    provinsi_link = []
    query = """
SELECT ?province WHERE {
?province <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q5098> .
?province <http://www.w3.org/2000/01/rdf-schema#label> \"""" + provinsi + """\"@id.}
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        provinsi_link.append(item['province']['value'])

    file_name = '../static/data/data-rs-all.nt'
    query = """
    SELECT ?hospital ?hospital_label WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?row <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_label .
    ?hospital <http://0.0.0.0:8080/dataRS#PENYELENGGARA> ?pengelola.
    ?pengelola <http://www.w3.org/2000/01/rdf-schema#label> \"""" + pengelola + """\"@id-id .
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """>.
    }"""

    result = get_query(file_name, query)
    list_of_dict = []
    for row in result:
        d = {}
        d['hospital_iri'] = str(row.asdict()['hospital'].toPython())
        d['hospital_name'] = str(row.asdict()['hospital_label'].toPython())
        list_of_dict.append(d)
    return list_of_dict


def query_rs(provinsi):
    provinsi_link = []
    query = """
SELECT ?province WHERE {
?province <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q5098> .
?province <http://www.w3.org/2000/01/rdf-schema#label> \"""" + provinsi + """\"@id.}
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        provinsi_link.append(item['province']['value'])

    file_name = '../static/data/data-rs-all.nt'
    query = """
    SELECT ?hospital ?hospital_label ?type ?class ?class_label ?pengelola ?pengelola_label ?region ?region_label WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?row <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_label.
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.w3.org/2000/01/rdf-schema#label> ?region_label .
    ?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """>.
    ?hospital <http://0.0.0.0:8080/dataRS#JENIS_RS> ?type .
    ?hospital <http://0.0.0.0:8080/dataRS#KLS_RS> ?class .
    ?class <http://www.w3.org/2000/01/rdf-schema#label> ?class_label .
    ?hospital <http://0.0.0.0:8080/dataRS#PENYELENGGARA> ?pengelola .
    ?pengelola <http://www.w3.org/2000/01/rdf-schema#label> ?pengelola_label .
    }"""
    result = get_query(file_name, query)
    list_of_dict = []
    for row in result:
        d = {}
        d['hospital_iri'] = str(row.asdict()['hospital'].toPython())
        d['hospital_name'] = str(row.asdict()['hospital_label'].toPython())
        d['type_name'] = str(row.asdict()['type'].toPython())
        d['class_iri'] = str(row.asdict()['class'].toPython())
        d['class_name'] = str(row.asdict()['class_label'].toPython())
        d['pengelola_iri'] = str(row.asdict()['pengelola'].toPython())
        d['pengelola_name'] = str(row.asdict()['pengelola_label'].toPython())
        d['region_iri'] = str(row.asdict()['region'].toPython())
        d['region_name'] = str(row.asdict()['region_label'].toPython())
        list_of_dict.append(d)

    query = """
SELECT DISTINCT ?hospital_label ?rs WHERE {
?rs <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q16917> .
?rs <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_label .
?rs <http://www.wikidata.org/prop/direct/P131> ?region.
?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """> . }
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        d = {}
        d['hospital_iri'] = item['rs']['value']
        d['hospital_name'] = item['hospital_label']['value']
        d['type_name'] = ""
        d['class_iri'] = ""
        d['class_name'] = ""
        d['pengelola_iri'] = ""
        d['pengelola_name'] = ""
        d['region_iri'] = ""
        d['region_name'] = ""

    return list_of_dict


def query_detail_rs(rumah_sakit):
    file_name = '../static/data/data-rs-all.nt'
    query = """
    SELECT ?type_label ?address_label ?region ?region_label ?post_label ?phone_label ?fax_label
    ?direktur_label ?class ?class_label ?pengelola ?pengelola_label WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?row <http://www.w3.org/2000/01/rdf-schema#label> \"""" + rumah_sakit + """\"@id-id .
    ?hospital <http://0.0.0.0:8080/dataRS#ALAMAT> ?address_label .
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.w3.org/2000/01/rdf-schema#label> ?region_label.
    ?hospital <http://0.0.0.0:8080/dataRS#DIREKTUR> ?direktur_label .
    ?hospital <http://0.0.0.0:8080/dataRS#JENIS_RS> ?type_label .
    ?hospital <http://0.0.0.0:8080/dataRS#KLS_RS> ?class .
    ?class <http://www.w3.org/2000/01/rdf-schema#label> ?class_label .
    ?hospital <http://0.0.0.0:8080/dataRS#PENYELENGGARA> ?pengelola .
    ?pengelola <http://www.w3.org/2000/01/rdf-schema#label> ?pengelola_label .
    OPTIONAL { ?hospital <http://0.0.0.0:8080/dataRS#KODE_POS> ?post_label }
    OPTIONAL {?hospital <http://0.0.0.0:8080/dataRS#TELEPON> ?phone_label }
    OPTIONAL {?hospital <http://0.0.0.0:8080/dataRS#FAX> ?fax_label } }"""
    result = get_query(file_name, query)
    list_of_dict = []
    for row in result:
        d = {}
        d['type_name'] = str(row.asdict()['type_label'].toPython())
        d['address_name'] = str(row.asdict()['address_label'].toPython())
        d['region_iri'] = str(row.asdict()['region'].toPython())
        d['region_name'] = str(row.asdict()['region_label'].toPython())
        d['direktur_name'] = str(row.asdict()['direktur_label'].toPython())
        d['class_iri'] = str(row.asdict()['class'].toPython())
        d['class_name'] = str(row.asdict()['class_label'].toPython())
        d['pengelola_iri'] = str(row.asdict()['pengelola'].toPython())
        d['pengelola_name'] = str(row.asdict()['pengelola_label'].toPython())
        if 'post_label' in row.asdict():
            d['kode_pos'] = str(row.asdict()['post_label'].toPython())
        else:
            d['kode_pos'] = ""
        if 'phone_label' in row.asdict():
            d['no_telp'] = str(row.asdict()['phone_label'].toPython())
        else:
            d['no_telp'] = ""
        if 'fax_label' in row.asdict():
            d['no_fax'] = str(row.asdict()['fax_label'].toPython())
        else:
            d['no_fax'] = ""
        list_of_dict.append(d)

    return list_of_dict


def query_tipe_rs(tipe_rs, provinsi):
    provinsi_link = []
    query = """
SELECT ?province WHERE {
?province <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q5098> .
?province <http://www.w3.org/2000/01/rdf-schema#label> \"""" + provinsi + """\"@id.}
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        provinsi_link.append(item['province']['value'])

    file_name = '../static/data/data-rs-all.nt'
    query = """
    SELECT ?hospital ?hospital_label WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?row <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_label .
    ?hospital <http://0.0.0.0:8080/dataRS#JENIS_RS> \"""" + tipe_rs + """\"@id-id .
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """>.
    }"""

    result = get_query(file_name, query)
    list_of_dict = []
    for row in result:
        d = {}
        d['hospital_iri'] = str(row.asdict()['hospital'].toPython())
        d['hospital_name'] = str(row.asdict()['hospital_label'].toPython())
        list_of_dict.append(d)
    return list_of_dict


def query_kelas_rs(kelas_rs, provinsi):
    provinsi_link = []
    query = """
SELECT ?province WHERE {
?province <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q5098> .
?province <http://www.w3.org/2000/01/rdf-schema#label> \"""" + provinsi + """\"@id.}
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        provinsi_link.append(item['province']['value'])

    file_name = '../static/data/data-rs-all.nt'
    query = """
    SELECT ?hospital ?hospital_label WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?row <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_label .
    ?hospital <http://0.0.0.0:8080/dataRS#KLS_RS> ?class.
    ?class <http://www.w3.org/2000/01/rdf-schema#label> \"""" + kelas_rs + """\"@id-id .
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """>.
    }"""

    result = get_query(file_name, query)
    list_of_dict = []
    for row in result:
        d = {}
        d['hospital_iri'] = str(row.asdict()['hospital'].toPython())
        d['hospital_name'] = str(row.asdict()['hospital_label'].toPython())
        list_of_dict.append(d)
    return list_of_dict


if __name__ == '__main__':
    res = query_kelas_rs("A", "Daerah Khusus Ibukota Jakarta")
    # if you want to see the result
    test(res)
