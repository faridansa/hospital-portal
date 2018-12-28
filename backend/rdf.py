import rdflib


def get_query(file_name, query):
    g = rdflib.Graph()
    g.parse(file_name, format="nt")
    query_result = g.query(query)
    return query_result


def test(result):
    for row in result:
        print(row)


def query_all_rs():
    file_name = 'data-rs-all.nt'
    query = """
    SELECT ?alamat
    WHERE { ?nama_rs <http://0.0.0.0:8080/dataRS#ALAMAT> ?alamat
    }"""
    result = get_query(file_name, query)
    return result


if __name__ == '__main__':
    res = query_all_rs()
    # if you want to see the result
    test(res)
