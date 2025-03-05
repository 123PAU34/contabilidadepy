#Este c�digo cria um servidor Flask que gerencia os registros cont�beis.
from flask import Flask, render_template,
 request, redirect, jsonify
 from database import get_all_records,
 add_record, delete_record

 app = Flask(_name_) 

@app.route('/') 
def index(): 
  registros = get_all_records() 
  return render_template('index.html',
 registros=registros) 

@app.route('/add', methods=['POST']) 
def add(): 
  data = request.form['date'] 
  doc1 = request.form['doc1'] 
  doc2 = request.form['doc2'] 
  descricao = request.form['descricao'] 

add_record(data, doc1, doc2, descricao) 
return redirect('/') 

@app.route('/delete/<int:id>', methods=
['POST']) 
def delete(id): 
delete_record(id) 
return jsonify({'message': 'Registro 
exclu�do!'})
if _name_ == '_main_':
    app.run(debug=True)