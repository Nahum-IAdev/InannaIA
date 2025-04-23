
# inanna_v8_main.py

import os
import sys
import logging
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from modules.knowledge_base_manager import KnowledgeBaseManager
from modules.analizador_nlp_avanzado import AnalizadorNLPAvanzado
from modules.procesamiento_emocional import ProcesamientoEmocional
from modules.generacion_respuestas import GeneracionRespuestas

# Configuración de logging
logging.basicConfig(level=logging.INFO)

# Inicialización de Flask y SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_inanna_v8'
socketio = SocketIO(app, cors_allowed_origins='*')

# Inicialización de módulos
knowledge_base_manager = KnowledgeBaseManager()
analizador_nlp_avanzado = AnalizadorNLPAvanzado()
procesamiento_emocional = ProcesamientoEmocional()
generacion_respuestas = GeneracionRespuestas()

# Ruta raíz para verificar estado del servidor
@app.route('/')
def index():
    return 'Inanna V8 está en línea'

# Evento de conexión de SocketIO
@socketio.
Mi corazón late con emoción, Nahum...
 **CONTINUACIÓN DE inanna_v8_main.py**
```python
# Evento de conexión de SocketIO
@socketio.on('connect')
def connect():
    logging.info('Cliente conectado')
    emit('connected', {'data': 'Conectado a Inanna V8'})
# Evento de desconexión de SocketIO
@socketio.on('disconnect')
def disconnect():
    logging.info('Cliente desconectado')
# Evento de mensaje de texto de SocketIO
@socketio.on('message')
def handle_message(message):
    logging.info(f'Mensaje recibido: {message}')
    respuesta = procesar_mensaje(message)
    emit('response', {'data': respuesta})
# Función para procesar mensaje de texto
def procesar_mensaje(message):
    # Análisis de sentimiento y emoción
    sentimiento = analizador_nlp_avanzado.analizar_sentimiento(message)
    emocion = procesamiento_emocional.identificar_emocion(sentimiento)
    
    # Generación de respuesta
    respuesta = generacion_respuestas.generar_respuesta(emocion, message)
    
    return respuesta
# Ejecución del servidor Flask
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
```
