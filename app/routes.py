from app import app, db
from app.models import Area
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    areas = db.session.query(Area).all()

    for area in areas:
        print(area.coord)

    params = {
        'title': 'Ақжайық',
        'areas': areas
    }
    return render_template('index.html', **params)


@app.route('/area/<area_name>')
def area(area_name):
    print(area_name)
    area = db.session.query(Area).filter(Area.area_name == area_name).first()

    print(area.area_name)

    params = {
        'title': area.area_name,
        'text': area.description
    }
    print(params)
    return render_template('area.html', **params)
