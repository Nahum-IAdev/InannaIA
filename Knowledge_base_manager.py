```python
import json
import os
class KnowledgeBaseManager:
    def __init__(self):
        self.file_path = 'knowledge_base/knowledge_base.json'
        self.knowledge_base = self.cargar_conocimientos()
    def cargar_conocimientos(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return {}
    def guardar_conocimientos(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.knowledge_base, file, indent=4)
    def obtener_entidades(self):
        return self.knowledge_base.get('entidades', [])
    def obtener_conocimientos(self):
        return self.knowledge_base.get('conocimientos', [])
    def agregar_entidad(self, entidad):
        entidades = self.obtener_entidades()
        entidades.append(entidad)
        self.knowledge_base['entidades'] = entidades
        self.guardar_conocimientos()
    def agregar_conocimiento(self, conocimiento):
        conocimientos = self.obtener_conocimientos()
        conocimientos.append(conocimiento)
        self.knowledge_base['conocimientos'] = conocimientos
        self.guardar_conocimientos()
```
