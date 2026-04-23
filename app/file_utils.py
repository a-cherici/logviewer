import os

#return the absolute path of a relative path
def safe_join(base:str, path:str)->str:
    full_path = os.path.abspath(os.path.join(base, path))
    if not full_path.startswith(base):
        raise ValueError("Invalid path")
    return full_path



def tail_lines(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    return file_content


#def tail_lines(filepath, n=100):
#    with open(filepath, "rb") as f:
#        f.seek(0, os.SEEK_END)
#        file_size = f.tell()
#
#        block_size = 1024
#        data = b""
#        lines = []
#
#        while file_size > 0 and len(lines) <= n:
#            read_size = min(block_size, file_size)
#            f.seek(file_size - read_size)
#            chunk = f.read(read_size)
#
#            data = chunk + data
#            lines = data.splitlines()
#
#            file_size -= read_size
#
#        return b"\n".join(lines[-n:]).decode(errors="ignore")

#def tail_lines(filepath, n=100):
#    with open(filepath, "rb") as f:
#        f.seek(0, os.SEEK_END)
#        buffer = bytearray()
#        pointer = f.tell()
#
#        while pointer >= 0 and len(buffer.splitlines()) <= n:
#            f.seek(pointer)
#            pointer -= 1
#            buffer.extend(f.read(1))
#
#        return b"".join(reversed(buffer)).decode(errors="ignore")