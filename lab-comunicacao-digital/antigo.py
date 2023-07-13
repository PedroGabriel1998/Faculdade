import time
import serial
import asyncio
import logging
from datetime import datetime
import random
import time
import asyncio
import math 
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

comport = serial.Serial('/dev/rfcomm0', 9600)
comport2 = serial.Serial('/dev/rfcomm1', 9600)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FastAPI app")

app = FastAPI()

# Note that the verb is `websocket` here, not `get`, `post`, etc.
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Accept the connection from a client.
    await websocket.accept()

    while True:#while para manter a conexão aberta
        try:
            while True: #while para continuar recebendo as informações
                await asyncio.sleep(0.00833333333) 
                logger.info(ord(comport2.read()))
                
                await websocket.send_json(
                    {
                        "message": ord(comport.read())* (3.3/1024)*100*0.33*0.4,
                        "messageAmostragem": ord(comport2.read()),
                        #"message": ord(comport.read()),
                        #"message": random.randrange(1,10),
                        "potencia": (ord(comport.read())* (5/1024))/(math.sqrt(2)*2)*100*0.27 * 220,
                        "time": datetime.now().strftime("%H:%M:%S"),
                    }
                )
            
        except WebSocketDisconnect:
            logger.info("The connection is closed.")
            break
        
        
        