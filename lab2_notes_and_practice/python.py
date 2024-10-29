def biblio_add_record(biblio: list, record: dict):
    for key in record.keys():
        for elements in biblio:
            if key not in elements:
                biblio.append(key)
                biblio.append(record[key])
    return biblio

biblio = ['id: skiena2017data']
record = {"id": "skiena2017data", "title": "The data science design manual", "authors": '["Steven Skiena"]', 'year': '2017', "hello":"new"}
biblio_add_record(biblio, record)

        
    