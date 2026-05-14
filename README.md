# Log Viewer Web (Python)

## Features
- File browser
- Live tail (WebSocket)
- Auto-scroll
- Search
- ANSI support (via xterm.js)

## Install

```bash
pip install -r requirements.txt
```
## Run

```bash
uvicorn app.main:app --reload --port 8001
```