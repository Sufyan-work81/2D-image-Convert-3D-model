# server.py (Flask minimal backend example)
from flask import Flask, request, jsonify
import os, uuid

app = Flask(__name__, static_folder='results')

@app.route('/api/convert', methods=['POST'])
def convert():
    img = request.files.get('image')
    opts = request.form.get('options')
    # save input
    id = str(uuid.uuid4())
    os.makedirs('tmp', exist_ok=True)
    in_path = f'tmp/{id}.png'
    img.save(in_path)
    # TODO: Run MiDaS + Open3D pipeline here
    model_relpath = f'/results/{id}.glb'
    return jsonify({'status':'ok','modelUrl':model_relpath})

if __name__ == '__main__':
    app.run(debug=True)
