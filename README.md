# 🔐 LAN CryptoChat (Terminal Edition)

Una semplice chat da terminale che permette la comunicazione tra più dispositivi connessi alla stessa rete locale (LAN), con **crittografia end-to-end** e **nessun salvataggio dei dati**. Progetto scritto in **Python**, pensato per essere educativo, utile e utilizzabile anche da telefono.

---

## 📌 Obiettivo del progetto

- Comunicare in modo sicuro su rete locale senza interfaccia grafica
- Utilizzare crittografia simmetrica (AES) per proteggere i messaggi
- Garantire la **temporaneità** della chat: niente file salvati, tutto si cancella a fine sessione
- Possibilità di connettersi anche da uno **smartphone** connesso alla stessa rete

---

## 🧱 Struttura del progetto

### 1. Comunicazione di rete
- Uso di `socket` per creare un **server TCP** e più **client**
- Connessione via **IP locale + porta**

### 2. Crittografia
- Cifratura e decifratura dei messaggi usando:
  - Algoritmo **AES**
  - Codifica base64 per messaggi trasmissibili
- Librerie: `cryptography` oppure `pycryptodome`

### 3. Multithreading o Async
- Un thread per inviare messaggi (input)
- Un thread per riceverli in tempo reale
- Libreria: `threading` o `asyncio`

### 4. Accesso da smartphone
- Il server resta in ascolto sull’**IP locale del PC**
- Dal telefono ci si connette tramite:
  - **Termux** con client Python
  - (Facoltativo) **Mini interfaccia web con Flask**

### 5. Sicurezza e temporaneità
- Nessun messaggio viene salvato
- Nessun log persistente
- Possibile autodistruzione o timeout della sessione

---

## ✅ Checklist sviluppo

### 🛠️ Preparazione ambiente
- [ ] Installare librerie: `cryptography`, `socket`, `threading`
- [ ] Verificare IP locale e connessione tra dispositivi
- [ ] Scegliere una porta (es. 5000)

### 🧱 Base server-client
- [ ] Server che accetta più client
- [ ] Client che si connette al server
- [ ] Test base di invio/ricezione

### 🔐 Aggiunta crittografia
- [ ] Generazione chiave segreta condivisa
- [ ] Cifratura AES lato invio
- [ ] Decifratura lato ricezione

### 🔄 Aggiunta multithreading
- [ ] Thread per ricezione messaggi
- [ ] Thread per input da terminale

### 📱 Supporto telefono
- [ ] Collegamento da Termux o altro PC
- [ ] Verifica ricezione/cifratura corretta
- [ ] (Opzionale) Versione Flask minimale

### 🔐 Sicurezza finale
- [ ] Nessun file di log
- [ ] Distruzione chiavi a fine sessione
- [ ] Disconnessione client alla chiusura del server

---

## 🧠 Tecnologie e librerie

| Scopo                 | Tecnologie / Librerie           |
|----------------------|----------------------------------|
| Networking           | `socket`, IP locali, porte       |
| Crittografia         | `cryptography`, `pycryptodome`   |
| Multithreading       | `threading` / `asyncio`          |
| Encoding             | `base64`, `secrets`              |
| Web support (opz.)   | `Flask`                          |
| Terminale da mobile  | `Termux` su Android              |

---

## 📁 Organizzazione file (esempio)

├── client.py 
├── server.py 
├── crypto_utils.py 
├── README.md 
└── requirements.txt

---

## 📎 Note finali

> ⚠️ Questo progetto è pensato a scopo didattico. Non è destinato a sostituire soluzioni di messaggistica sicura professionali.  
> Perfetto per imparare come funzionano **reti**, **crittografia** e **programmazione asincrona** in Python.

---

Se ti è piaciuto questo progetto, sentiti libero di fare una fork, migliorarne la sicurezza, o implementare una versione con GUI o webapp!

