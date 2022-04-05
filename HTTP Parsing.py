import asyncio 
import sys

class HTTPParser:
    def __init__(self):
        self. part = "REQUEST"
        self. headers = []
        self. body_length = 0
         
    def feed_line (self , line: bytes):
        if self. part == "REQUEST":
            self. method, self.path, self.version = line.split (b" ",2)
            self. part = "HEADER"
        elif self. part == "HEADER" and line.strip() == b"":
            self. part = "BODY"
        elif self. Part == "HEADERS":
            name, value = line.split ( b":", 1)
            self. header.append ((name.strip(), value.strip()))
            if name.lower () == b"content-length":
                self.body_length = int (value)
async def http_parser_server (reader, writer):
    parser = HTTPParser()
    body = bytearray
    while not reader.at_eof():
        if parser.part != "BODY":
            parser.feed_line(await reader.readline())
        else:
            if len(body) >= parser.body_length:
                break
            body.extend(await reader.read(100))
    writer.write(b"HTTP/1.1 200\r\nContent-Length: 0\r\n\r\n")
    await writer.drain()
    writer.close()

async def main (host, port):
    server = await asyncio.start_server(http_parser_server, host, port)
    await server.serve_forever()

if __name__ == "__main__":
    host, port = sys.argv[0], sys.argv[1:]
    asyncio.run(main(host, port))