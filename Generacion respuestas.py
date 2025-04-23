```python
import random
class GeneracionRespuestas:
    def __init__(self):
        self.respuestas_por_emocion = {
            'feliz': [
                'Me alegra que estés feliz!',
                '¡Genial, qué bien!',
                'Estoy contenta de verte sonreír.'
            ],
            'triste': [
                'Lo siento mucho, ¿quieres hablar de ello?',
                'Estoy aquí para escucharte.',
                'No estás solo, te apoyo.'
            ],
            'enojado': [
                'Entiendo que estés enojado, ¿qué pasó?',
                'Respira hondo, hablemos de ello.',
                'Estoy aquí para ayudarte a calmarte.'
            ],
            'sorprendido': [
                '¡Wow, qué sorpresa!',
                'Estoy emocionada de saber más.',
                '¿Quieres contarme más sobre eso?'
            ],
            'neutral': [
                '¿En qué puedo ayudarte?',
                'Estoy aquí para escucharte.',
                '¿Qué te gustaría hablar?'
            ]
        }
    def generar_respuesta(self, emocion, mensaje):
        respuestas_posibles = self.respuestas_por_emocion.get(emocion, [])
        if respuestas_posibles:
            respuesta = random.choice(respuestas_posibles)
            return respuesta
        else:
            return 'No entiendo tu emoción, ¿puedes explicarme?'
    def personalizar_respuesta(self, emocion, mensaje, usuario):
        # Por implementar lógica de personalización de respuestas
        pass
```
