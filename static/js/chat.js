const DEFAULT_COLOR = '#00ff00';

let socket;
let encryptionKey;
let currentUsername;
let currentRoom;
let fernet;

function initChat() {
    document.getElementById('message-input').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    document.getElementById('send-button').addEventListener('click', sendMessage);

    const savedColor = localStorage.getItem('mainColor');
    if (savedColor) {
        updateMainColor(savedColor);
        document.getElementById('main-color').value = savedColor;
    }

    document.addEventListener('click', (e) => {
        const settingsMenu = document.getElementById('settings-menu');
        const settingsButton = document.getElementById('settings-button');
        if (!settingsMenu.contains(e.target) && !settingsButton.contains(e.target)) {
            settingsMenu.style.display = 'none';
            settingsButton.classList.remove('active');
        }
    });
}

function joinChat() {
    const username = document.getElementById('username').value.trim();
    const room = document.getElementById('room').value.trim();

    if (!username) {
        alert('Inserisci un username!');
        return;
    }

    currentUsername = username;
    currentRoom = room;

    document.getElementById('current-room-display').textContent = currentRoom;

    socket = io();
    
    socket.on('connect', () => {
        socket.emit('join', { username, room });
        document.getElementById('login-screen').style.display = 'none';
        document.getElementById('chat-screen').style.display = 'flex';
        
        document.getElementById('message-input').focus();
    });

    socket.on('encryption_key', (data) => {
        encryptionKey = data.key;
    });

    socket.on('message', (data) => {
        appendMessage(data.username, data.message);
    });

    socket.on('status', (data) => {
        if (data.room === currentRoom) {
            appendStatus(data.msg);
        }
    });
}

function changeRoom() {
    const newRoom = document.getElementById('new-room').value.trim();
    if (!newRoom) {
        alert('Inserisci il nome della nuova stanza!');
        return;
    }

    socket.emit('leave_room', { room: currentRoom });

    currentRoom = newRoom;
    socket.emit('join', { username: currentUsername, room: newRoom });

    document.getElementById('current-room-display').textContent = currentRoom;
    document.getElementById('new-room').value = '';

    document.getElementById('messages').innerHTML = '';
}

function resetColor() {
    updateMainColor(DEFAULT_COLOR);
    document.getElementById('main-color').value = DEFAULT_COLOR;
}

function toggleSettings() {
    const menu = document.getElementById('settings-menu');
    const button = document.getElementById('settings-button');
    const isVisible = menu.style.display === 'block';
    
    menu.style.display = isVisible ? 'none' : 'block';
    button.classList.toggle('active');
}

function updateMainColor(color) {
    document.documentElement.style.setProperty('--main-color', color);
    localStorage.setItem('mainColor', color);
}

function sendMessage() {
    const input = document.getElementById('message-input');
    const message = input.value.trim();
    
    if (message) {
        socket.emit('message', {
            message: message,
            room: currentRoom
        });
        input.value = '';
        input.focus();
    }
}

function appendMessage(username, message) {
    const messagesDiv = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.className = 'message';
    
    const usernameSpan = document.createElement('span');
    usernameSpan.className = 'username';
    usernameSpan.textContent = username + ':';
    
    const messageSpan = document.createElement('span');
    messageSpan.className = 'message-text';
    messageSpan.textContent = ' ' + message;
    
    messageElement.appendChild(usernameSpan);
    messageElement.appendChild(messageSpan);
    
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function appendStatus(message) {
    const messagesDiv = document.getElementById('messages');
    const statusElement = document.createElement('div');
    statusElement.className = 'status';
    statusElement.textContent = message;
    messagesDiv.appendChild(statusElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

document.addEventListener('DOMContentLoaded', initChat);