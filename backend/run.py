from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from models import db, Members, Concerts, Tickets, Schedules, get_model_dict
import json

app = Flask(__name__,
            static_folder = "../frontend/dist",
            template_folder = "../frontend/dist")
CORS(app)

app.config['DEBUG'] = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/the_name?charset=utf8'.format(**{
        'user': 'root',
        'password': 'mahoto1500',
        'host': 'localhost',
    })
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_NATIVE_UNICODE'] = 'utf-8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
db.app = app

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/api/members')
def members():
    members = Members.query.all()
    members = [get_model_dict(member) for member in members]
    return jsonify(members)

@app.route('/api/member/<id>')
def member(id):
    member = Members.query.filter_by(id=id).first()
    return jsonify(get_model_dict(member))

@app.route('/api/regist_member', methods=["POST"])
def regist_member():
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    name = json.loads(data)['name']
    member = Members(name)
    db.session.add(member)
    db.session.commit()
    return jsonify(get_model_dict(member))

@app.route('/api/concerts')
def concerts():
    concerts = Concerts.query.all()
    concerts = [get_model_dict(concert) for concert in concerts]
    return jsonify(concerts)

@app.route('/api/concert/<id>')
def concert(id):
    concert = Concerts.query.filter_by(id=id).first()
    return jsonify(get_model_dict(concert))

@app.route('/api/regist_concert', methods=["POST"])
def regist_concert():
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    data = json.loads(data)['concert']
    concert = Concerts(data['name'])
    db.session.add(concert)
    db.session.commit()
    return jsonify(get_model_dict(concert))

@app.route('/api/schedules')
def schedules():
    schedules = Schedules.query.all()
    schedules = [get_model_dict(schedule) for schedule in schedules]
    return jsonify(schedules)

@app.route('/api/dict_schedules/<member_id>')
def dict_schedules(member_id):
    schedules = Schedules.query.all()
    schedules = [get_model_dict(schedule) for schedule in schedules]
    print(schedules)
    ret = {}
    for schedule in schedules:
        concert_id = schedule['concert_id']
        ticket = Tickets.query.filter_by(member_id=member_id, schedule_id=schedule['id']).first()
        obj = {}
        obj['date'] = '%s %s'%(schedule['date'], schedule['time'])
        obj['place'] = schedule['place']
        if ticket is None: continue
        obj['status'] = ticket.status
        obj['num'] = ticket.number
        if concert_id in ret.keys():
            ret[concert_id].append(obj) 
        else:
            ret[concert_id] = [obj]
    print(ret)
    return jsonify(ret)

@app.route('/api/regist_schedule', methods=["POST"])
def regist_scheule():
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    data = json.loads(data)['schedule']
    schedule = Schedules(data['concert']['id'], data['date'], data['time'], data['place'])
    db.session.add(schedule)
    db.session.commit()
    return jsonify(get_model_dict(schedule))

@app.route('/api/ticket', methods=['POST'])
def ticket():
    data = request.data.decode('utf-8')
    print(data)
    data = json.loads(data)
    member_id = data['member_id']
    schedule_id = data['schedule_id']
    tickets = Tickets.query.filter_by(member_id=member_id, schedule_id=schedule_id).all()
    tickets = [get_model_dict(ticket) for ticket in tickets]
    ret = {}
    for ticket in tickets:
        schedule_id = ticket['schedule_id']
        obj = {}
        obj['ID'] = ticket['id']
        obj['date'] = ticket['created']
        obj['status'] = ticket['status']
        if schedule_id in ret.keys():
            ret[schedule_id].append(obj) 
        else:
            ret[schedule_id] = [obj]
    return jsonify(ret)

@app.route('/api/regist_ticket', methods=["POST"])
def regist_ticket():
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    data = json.loads(data)['ticket']
    ticket = Tickets(data['member']['id'], data['schedule']['id'], 'Applyed', data['number'])
    db.session.add(ticket)
    db.session.commit()
    return jsonify(get_model_dict(ticket))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    print(" * Flask starting server...")
    app.run(host='0.0.0.0',port=5000)