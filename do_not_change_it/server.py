import asyncio
import logging
import msgprotocol
import message_pb2 as message

logging.basicConfig(level = logging.DEBUG)

class MsgServerProtocol(msgprotocol.MsgProtocol):
    def connection_lost(self,exc):
        logging.debug("connection losted")
        msgprotocol.MsgProtocol.connection_lost(self,exc)
        if exc is not None:
        	logging.info("---exit EXCEPTION---")
        	
    # override
    def process_msg(self,msg):
        logging.debug(msg)
        
        if msg.type == message.MsgType.TLogin:
            # found the user from users db
            logging.debug("---login ok!---")
            
            msg = message.Msg()
            msg.type = message.MsgType.TLoginOk
            self.send_msg(msg)
        else:
            # no that msg!
            logging.info("not support the type msg now")

async def main():
    loop = asyncio.get_running_loop()
    
    server = await loop.create_server(
        lambda: MsgServerProtocol(), '127.0.0.1', 5678)
    
    async with server:
        await server.serve_forever()
        
if __name__ == '__main__':
	asyncio.run(main())