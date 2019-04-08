from flask import Flask, render_template, request, jsonify, make_response
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_cors import CORS
from models import db, Users, Members, Concerts, Tickets, Schedules, get_model_dict
from dateutil.relativedelta import relativedelta
import json
import hashlib

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
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_EXPIRATION_DELTA'] =  relativedelta(months=3)
db.init_app(app)
db.app = app

def authenticate(username, password):
    user = Users.query.filter_by(username=username).first()
    password = hashlib.sha512(password.encode('utf-8')).hexdigest()
    if user and safe_str_cmp(user.password.encode('utf-8'), password):
        return user

def identity(payload):
    user_id = payload['identity']
    return Users.query.filter_by(id=user_id).first()

jwt = JWT(app, authenticate, identity)

@app.route('/api/regist_user', methods=["POST"])
def regist_user():
    data = request.data.decode('utf-8')
    user = json.loads(data)
    user['password'] = user['password'].encode('utf-8')
    user['password'] = hashlib.sha512(user['password']).hexdigest()
    user = Users(user['username'], user['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(get_model_dict(user))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/api/members')
@jwt_required()
def members():
    user = current_identity
    members = Members.query.filter_by(user_id=user.id).all()
    members = [get_model_dict(member) for member in members]
    return jsonify(members)

@app.route('/api/member/<id>')
@jwt_required()
def member(id):
    user = current_identity
    member = Members.query.filter_by(id=id, user_id=user.id).first()
    return jsonify(get_model_dict(member))

@app.route('/api/regist_member', methods=["POST"])
@jwt_required()
def regist_member():
    user = current_identity
    print(user)
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    member = json.loads(data)['member']
    if 'id' in member.keys():
        print('update')
        obj = Members.query.get(member['id'])
        obj.name = member['name']
        print(get_model_dict(obj))
        member = jsonify(get_model_dict(obj))
    else:
        print('create')
        member = Members(member['name'], user.id)
        db.session.add(member)
        member = jsonify(get_model_dict(member))
    db.session.commit()
    return member

@app.route('/api/concerts')
@jwt_required()
def concerts():
    user = current_identity
    concerts = Concerts.query.filter_by(user_id=user.id).all()
    concerts = [get_model_dict(concert) for concert in concerts]
    return jsonify(concerts)

@app.route('/api/concert/<id>')
@jwt_required()
def concert(id):
    user = current_identity
    concert = Concerts.query.filter_by(id=id, user_id=user.id).first()
    return jsonify(get_model_dict(concert))

@app.route('/api/regist_concert', methods=["POST"])
@jwt_required()
def regist_concert():
    user = current_identity
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    concert = json.loads(data)['concert']
    if 'id' in concert.keys():
        print('update')
        obj = Concerts.query.get(concert['id'])
        obj.name = concert['name']
        print(get_model_dict(obj))
        concert = jsonify(get_model_dict(obj))
    else:
        print('create')
        concert = Concerts(concert['name'], user.id)
        db.session.add(concert)
        concert = jsonify(get_model_dict(concert))
    db.session.commit()
    return concert

@app.route('/api/schedules')
@jwt_required()
def schedules():
    schedules = Schedules.query.all()
    schedules = [get_model_dict(schedule) for schedule in schedules]
    return jsonify(schedules)

@app.route('/api/dict_schedules/<member_id>')
@jwt_required()
def dict_schedules(member_id):
    schedules = Schedules.query.all()
    schedules = [get_model_dict(schedule) for schedule in schedules]
    ret = {}
    for schedule in schedules:
        concert_id = schedule['concert_id']
        ticket = Tickets.query.filter_by(member_id=member_id, schedule_id=schedule['id']).first()
        obj = {}
        obj['schedule_id'] = schedule['id']
        obj['date'] = '%s %s'%(schedule['date'], schedule['time'])
        obj['place'] = schedule['place']
        if ticket is None: continue
        obj['ticket_id'] = ticket.id
        obj['status'] = ticket.status
        obj['num'] = ticket.number
        if concert_id in ret.keys():
            ret[concert_id].append(obj) 
        else:
            ret[concert_id] = [obj]
    print(ret)
    return jsonify(ret)

@app.route('/api/regist_schedule', methods=["POST"])
@jwt_required()
def regist_scheule():
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    sch = json.loads(data)['schedule']
    if 'id' in sch.keys():
        print('update')
        obj = Schedules.query.get(sch['id'])
        obj.date = sch['date']
        obj.time = sch['time']
        obj.place = sch['place']
        print(get_model_dict(obj))
        schedule = jsonify(get_model_dict(obj))
    else:
        print('create')
        schedule = Schedules(sch['concert']['id'], sch['date'], sch['time'], sch['place'])
        db.session.add(schedule)
        schedule = jsonify(get_model_dict(schedule))
    db.session.commit()
    return schedule

@app.route('/api/save_schedule', methods=["POST"])
@jwt_required()
def save_scheule():
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    sch = json.loads(data)['schedule']
    print('update')
    obj = Schedules.query.get(sch['id'])
    obj.date = sch['date']
    obj.time = sch['time']
    obj.place = sch['place']
    print(get_model_dict(obj))
    schedule = jsonify(get_model_dict(obj))
    db.session.commit()
    return schedule

@app.route('/api/ticket', methods=['POST'])
@jwt_required()
def ticket():
    data = request.data.decode('utf-8')
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
@jwt_required()
def regist_ticket():
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')

    ticket = json.loads(data)['ticket']
    if 'id' in ticket.keys():
        print('update')
        obj = Tickets.query.get(ticket['id'])
        obj.number = ticket['num']
        obj.status = ticket['status']
        print(get_model_dict(obj))
        ticket = jsonify(get_model_dict(obj))
    else:
        print('create')
        ticket = Tickets(ticket['member']['id'], ticket['schedule']['id'], ticket['status'], ticket['number'])
        db.session.add(ticket)
        ticket = jsonify(get_model_dict(ticket))

    db.session.commit()
    return ticket

@app.route('/api/save_ticket', methods=["POST"])
@jwt_required()
def save_ticket():
    print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    ticket = json.loads(data)['ticket']
    print('update')
    obj = Tickets.query.get(ticket['id'])
    obj.number = ticket['num']
    obj.status = ticket['status']
    print(get_model_dict(obj))
    ticket = jsonify(get_model_dict(obj))
    db.session.commit()
    return ticket


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    print(" * Flask starting server...")
    app.run(host='0.0.0.0',port=5000)