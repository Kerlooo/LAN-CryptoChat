# 🔐 LAN CryptoChat

Una chat web che permette la comunicazione tra più dispositivi connessi alla stessa rete locale (LAN), con **crittografia** e **nessun salvataggio dei dati**. Progetto scritto in **Python** con interfaccia web moderna e reattiva.

---

## 📌 Caratteristiche principali

- Interfaccia web moderna e responsive
- Supporto per stanze multiple
- Crittografia dei messaggi
- Tema scuro con colore personalizzabile
- Nessun salvataggio dei messaggi
- Accessibile da qualsiasi dispositivo con un browser

---

## 🚀 Come iniziare

### Requisiti di sistema
- Python 3.8 o superiore
- pip (gestore pacchetti Python)

### Installazione su Debian/Ubuntu

1. Installa Python e pip se non sono già installati:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

2. Clona il repository:
```bash
git clone https://github.com/Kerlooo/LAN-CryptoChat
cd LAN-CryptoChat
```

3. Crea e attiva un ambiente virtuale:
```bash
python3 -m venv myenv
source myenv/bin/activate
```

4. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

### Avvio dell'applicazione

1. Attiva l'ambiente virtuale se non è già attivo:
```bash
source myenv/bin/activate
```

2. Avvia il server:
```bash
python web_server.py
```

3. Accedi alla chat:
- Apri il browser su `http://IP_DEL_SERVER:5000`
- Inserisci il tuo username e il nome della stanza
- Inizia a chattare!

### Note importanti
- Assicurati che tutti i dispositivi siano sulla stessa rete locale
- Il firewall potrebbe bloccare le connessioni. Se necessario, apri la porta 5000:
```bash
sudo ufw allow 5000
```

---

## 🎨 Funzionalità

### 💬 Chat
- Supporto per stanze multiple
- Username personalizzati
- Messaggi di stato per entrate/uscite
- Crittografia dei messaggi

### ⚙️ Personalizzazione
- Tema scuro moderno
- Colore principale personalizzabile
- Salvataggio delle preferenze
- Interfaccia responsive per mobile

### 🔒 Sicurezza
- Crittografia dei messaggi
- Nessun salvataggio dei dati
- Connessioni solo in rete locale

---

## 📁 Struttura del progetto

```
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── chat.js
├── templates/
│   └── index.html
├── crypto_utils.py
├── web_server.py
├── README.md
└── requirements.txt
```

---

## 🧠 Tecnologie utilizzate

| Scopo                 | Tecnologie / Librerie           |
|----------------------|----------------------------------|
| Backend              | Flask, Flask-SocketIO            |
| Frontend             | HTML5, CSS3, JavaScript          |
| WebSocket            | Socket.IO                        |
| Crittografia         | cryptography                     |

---

## 📎 Note finali

> ⚠️ Questo progetto è pensato per l'uso in rete locale.  
> Perfetto per chattare in modo sicuro all'interno della propria rete.

---

Se ti è piaciuto questo progetto, sentiti libero di fare una fork e aggiungere nuove funzionalità!

