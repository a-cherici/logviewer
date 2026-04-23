import os
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles


from .config import BASE_DIR, MAX_LINES
from .file_utils import safe_join, tail_lines

app = FastAPI()

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return FileResponse("static/index.html")


@app.get("/files")
def list_files():
    return [
        f for f in os.listdir(BASE_DIR)
        if os.path.isfile(os.path.join(BASE_DIR, f))
    ]


@app.get("/preview", response_class=PlainTextResponse)
def preview_file(name: str):
    #print("newwwwwww")
    path = safe_join(BASE_DIR, name)
    return tail_lines(path)#, MAX_LINES)


@app.websocket("/ws")
async def websocket_tail(ws: WebSocket):
    await ws.accept()
    filename = await ws.receive_text()

    try:
        path = safe_join(BASE_DIR, filename)
    except Exception:
        await ws.close()
        return

    with open(path, "r") as f:
        f.seek(0, os.SEEK_END)

        while True:
            line = f.readline()
            if not line:
                await asyncio.sleep(0.3)
                continue
            await ws.send_text(line)