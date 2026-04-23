const term = new Terminal({
  convertEol: true,
  scrollback: 5000
});

const fitAddon = new FitAddon.FitAddon();
term.loadAddon(fitAddon);

term.open(document.getElementById('terminal'));
fitAddon.fit();

window.addEventListener('resize', () => {
  fitAddon.fit();
});

let socket;
let buffer = [];

async function loadFiles() {
  const res = await fetch('/files');
  const files = await res.json();
  const select = document.getElementById('files');

  files.forEach(f => {
    const opt = document.createElement('option');
    opt.value = f;
    opt.innerText = f;
    select.appendChild(opt);
  });
}

async function openFile() {
  const file = document.getElementById('files').value;

  term.clear();
  fitAddon.fit();

  // preview iniziale
  const res = await fetch(`/preview?name=${file}`);
  const text = await res.text();
  term.write(text);

  // websocket
  if (socket) socket.close();

  socket = new WebSocket(`ws://${location.host}/ws`);

  socket.onopen = () => {
    socket.send(file);
  };

  socket.onmessage = (event) => {
    buffer.push(event.data);
    term.write(event.data);
  };
}

function searchText() {
  const query = document.getElementById('search').value.toLowerCase();

  term.clear();
  fitAddon.fit();

  buffer.forEach(line => {
    if (line.toLowerCase().includes(query)) {
      term.write(line);
    }
  });
}

loadFiles();