import os
from cmath import log

from flask import (Flask, flash, jsonify, redirect, request, send_file,
                   send_from_directory, session, url_for)
from flask_cors import CORS
from flask_restx import Api, fields
from werkzeug.utils import secure_filename

from backend.models import UsernotesModel
from config import DevelopmentConfig
from db import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)


CORS(app)


@app.route('/')
def new():
    return {"message":"Server running successfully"}, 200

# post notes  
@app.route('/post/notes', methods=['GET', 'POST'])
def post_notes():
    if request.method == 'POST':
        notes = request.json['notes']

        
        record = UsernotesModel(notes=notes)
        
        db.session.add(record) 
        db.session.commit() 
        
        return {"message":"Notes added successfully"}, 200
    
#get specific notes by id
@app.route('/get/note', methods=['GET', 'POST'])
def post_notes():
    if request.method == 'GET':
        notes_id = request.args.get('id')
        note = UsernotesModel.query.filter_by(id=notes_id).first()
        if note is None:
            return {"message":"That note does not exist"}, 400
        else:
            
            cols = ['id', 'notes']
        
            result = [{col: getattr(d, col) for col in cols} for d in note]
        
            return jsonify(data=result)

#get all notes        
@app.route('/get/all/notes', methods=['GET', 'POST'])
def post_notes():
    if request.method == 'GET':
        notes = db.session.query(UsernotesModel).all()

        if notes is None:
            return {"message":"no notes"}, 200
        else:
            cols = ['id', 'notes']
        
            result = [{col: getattr(d, col) for col in cols} for d in notes]
        
            return jsonify(data=result)

        
#delete specific notes by id
@app.route('/delete/notes', methods=['GET', 'POST'])
def post_notes():
    if request.method == 'GET':
        notes_id = request.args.get('id')
        note = UsernotesModel.query.filter_by(id=notes_id).first()
        if note is None:
            return {"message":"That note does not exist"}, 400
        else:
            
            db.session.delete(note)
            db.session.commit()

            return {"message":"Successfully deleted note"}, 200
  
if __name__ == '__main__':    
    app.run()
