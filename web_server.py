from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from crypto_utils import generate_key, encrypt_message, decrypt_message
import json
import os

app = Flask(__name__, 
    static_folder='static',
    static_url_path='/static',
    template_folder='templates'
)
app.config['SECRET_KEY'] = 'lan_cryptochat_secret'
socketio = SocketIO(app)

encryption_key = generate_key()
connected_users = {}
user_rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connesso')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    
    if request.sid in user_rooms:
        old_room = user_rooms[request.sid]
        leave_room(old_room)
        emit('status', {
            'msg': f'{username} ha lasciato la chat',
            'room': old_room
        }, room=old_room)
    
    connected_users[request.sid] = username
    user_rooms[request.sid] = room
    
    join_room(room)
    
    emit('encryption_key', {'key': encryption_key.decode()})
    
    emit('status', {
        'msg': f'{username} è entrato nella chat',
        'room': room
    }, room=room)

@socketio.on('leave_room')
def handle_leave_room(data):
    room = data['room']
    username = connected_users.get(request.sid, 'Anonimo')
    leave_room(room)
    emit('status', {
        'msg': f'{username} ha lasciato la chat',
        'room': room
    }, room=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    username = connected_users.get(request.sid, 'Anonimo')
    
    emit('message', {
        'username': username,
        'message': data['message']
    }, room=room)

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in connected_users:
        username = connected_users[request.sid]
        room = user_rooms.get(request.sid)
        
        del connected_users[request.sid]
        if request.sid in user_rooms:
            del user_rooms[request.sid]
        
        if room:
            emit('status', {
                'msg': f'{username} ha lasciato la chat',
                'room': room
            }, room=room)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) 