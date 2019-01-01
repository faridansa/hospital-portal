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
        print("%s : %s" % (row, result[row]))


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
    SELECT ?hospital_name ?hospital WHERE {
    ?row <http://0.0.0.0:8080/dataRS#NAMA_RS> ?hospital.
    ?row <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_name.
    ?hospital <http://0.0.0.0:8080/dataRS#KAB_KOTA> ?region.
    ?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """>.
    }"""
    result = get_query(file_name, query)
    print(type(result))
    print(len(result))
    d = {}
    for row in result:
        # print(row)
        d[str(row.asdict()['hospital'].toPython())] = str(
            row.asdict()['hospital_name'].toPython())

    query = """
SELECT DISTINCT ?hospital_name ?rs WHERE {
?rs <http://www.wikidata.org/prop/direct/P31> <http://www.wikidata.org/entity/Q16917> .
?rs <http://www.w3.org/2000/01/rdf-schema#label> ?hospital_name .
?rs <http://www.wikidata.org/prop/direct/P131> ?region.
?region <http://www.wikidata.org/prop/direct/P131> <""" + provinsi_link[0] + """> . }
    """
    r = requests.get(url, params={'format': 'json', 'query': query})
    data = r.json()
    for item in data['results']['bindings']:
        d[item['rs']['value']] = item['hospital_name']['value']

    return d


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
    print(type(result))
    d = {}
    try:
        print('kesini')
        print(len(result))
        iri = result.vars[0]
        print(iri)
        for row in result:
            print('sini cuy')
            print(row)
            iri = str(row.asdict()['pengelola'].toPython())
            # print(iri)
            d[iri] = {}
            d[iri]['label'] = str(row.asdict()['pengelola_label'].toPython())
            d[iri]['hospital_count'] = str(row.asdict()['count'].toPython())
        # print(d)
    except Exception as e:
        print('kesana')
        print(e)
    return d


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
    d = {}
    for row in result:
        iri = str(row.asdict()['class'].toPython())
        d[iri] = {}
        d[iri]['label'] = str(row.asdict()['class_label'].toPython())
        d[iri]['hospital_count'] = str(row.asdict()['count'].toPython())
    return d


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


if __name__ == '__main__':
    res = query_tipe_kelas("Daerah Khusus Ibukota Jakarta")
    # if you want to see the result
    test(res)
