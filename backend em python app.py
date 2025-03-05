
from flask import Flask, render_template, request, jsonify, redirect, url_for
import database

app = Flask(__name__)
app.secret_key = 'chave_secreta_do_app'

@app.route('/')
def index():
    registros = database.get_all_records()
    return render_template('index.html', registros=registros)

@app.route('/add', methods=['POST'])
def add():
    data = request.form.get('date')
    doc1 = request.form.get('doc1')
    doc2 = request.form.get('doc2')
    descricao = request.form.get('descricao')
    database.add_record(data, doc1, doc2, descricao)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    database.delete_record(id)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
