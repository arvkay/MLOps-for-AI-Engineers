from flask import Flask, request, jsonify
from area import area_of_farmer_field

app = Flask('__main__')

@app.route('/', methods=['GET', 'POST'])
def get_input():
    packet = request.get_json(force=True)
    length = packet['length']
    width = packet['width']
    area = area_of_farmer_field(length, width)
    return {"area":area} 

if __name__ == '__main__':
    app.run()