import time
import serial
import asyncio
import logging
from datetime import datetime
import random
import time
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

comport = serial.Serial('/dev/rfcomm0', 38400)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FastAPI app")

while(True):

    print(ord(comport.read()))

app = FastAPI()

# Note that the verb is `websocket` here, not `get`, `post`, etc.
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     # Accept the connection from a client.
#     await websocket.accept()
#     contador = 1
#     while True:#while para manter a conexão aberta
#         try:
#             while True: #while para continuar recebendo as informações
#                 await asyncio.sleep(0.00000000000001) 
#                 # logger.info(ord(comport.read()))
#                 print(ord(comport.read().decode('latin-1')))
#                 contador+=1
#                 print(contador)
                
#                 await websocket.send_json(
#                     {
#                         "message": ord(comport.read()),
#                         "contador": contador,
#                         # "message": random.random(),
#                         "time": datetime.now().strftime("%H:%M:%S"),
#                     }
#                 )
            
#         except WebSocketDisconnect:
#             logger.info("The connection is closed.")
#             break

# @app.websocket("/wsLento")
# async def websocket_endpoint(websocket: WebSocket):
#     # Accept the connection from a client.
#     await websocket.accept()

#     while True:#while para manter a conexão aberta
#         try:
#             while True: #while para continuar recebendo as informações
#                 # logger.info(ord(comport.read()))
#                 # print(ord(comport.read()))
                
#                 await websocket.send_json(
#                     {
#                         "message": ord(comport.read()),
#                         # "message": random.random(),
#                         "time": datetime.now().strftime("%H:%M:%S"),
#                     }
#                 )
            
#         except WebSocketDisconnect:
#             logger.info("The connection is closed.")
#             break

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     # Accept the connection from a client.
#     await websocket.accept()
#     contador = 1
#     while True:#while para manter a conexão aberta
#         await asyncio.sleep(0.00000000000001) 
#                 # logger.info(ord(comport.read()))
#         print(ord(comport.read().decode('latin-1')))
#         contador+=1
#         print(contador)
                
#         await websocket.send_json(
#                     {
#                         "message": ord(comport.read()),
#                         "contador": contador,
#                         # "message": random.random(),
#                         "time": datetime.now().strftime("%H:%M:%S"),
#                     }
#         )



        