import asyncio
import sys

async def echo_server (reader, writer):
    while not reader.at_eof ():
        data = await reader.read(100)
        writer. write (data)
        await writer .drain()
        writer.close ()

async def main (host, port) :
    server = await asyncio. start_server ( echo_server, host, port )
    await server. serve_forever ( )

if __name__ == "__main__":
    host,port = sys.argv[0], sys.argv[1:]
    asyncio.run(main(host,port))