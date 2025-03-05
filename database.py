
# Banco de Dados Simples (database.py)

# Este arquivo gerencia os registros (simulando um banco de dados).
registros = []
contador_id = 1

def get_all_records():
    return registros

def add_record(data, doc1, doc2, descricao):
    global contador_id
    registros.append({
        'id': contador_id,
        'data': data,
        'doc1': doc1,
        'doc2': doc2,
        'descricao': descricao
    })
    contador_id += 1

def delete_record(id):
    global registros
    registros = [r for r in registros if r['id'] != id]
