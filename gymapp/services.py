from .models import Perfil, Equipamiento_Del_Usuario
from .testApi import get_completion, calcular_edad # Aquí está la función que interactúa con la IA
import json
from django.core.exceptions import ObjectDoesNotExist


#En esta clase se realizo la inversion de dependencias del punto 3.
class RoutineService:
    def __init__(self, user):
        self.user = user

    def get_user_profile(self):
        # Obtener los detalles del perfil del usuario
        perfil = Perfil.objects.get(user=self.user)
        return {
            'deporte': perfil.deporte_practicado,
            'objetivo': perfil.objetivos,
            'condiciones': perfil.condiciones_medicas,
            'genero': perfil.genero,
            'edad': calcular_edad(perfil.fecha_Nacimiento)
        }

    def get_user_equipment(self, place):
        # Obtener el equipamiento del usuario
        try:
            equipa = Equipamiento_Del_Usuario.objects.get(user=self.user)
            if place == 'Gym':
                equipa = equipa.equp_gimnasio or 'No especificado'
            else:
                equipa = equipa.equp_casa or 'No especificado'
        except ObjectDoesNotExist:
            equipa = 'No especificado'
        return equipa

    def generate_routine(self, user_input, place):
        # Obtener detalles del perfil y equipo del usuario
        profile = self.get_user_profile()
        equipa = self.get_user_equipment(place)

        # Crear la solicitud con todos los parámetros relevantes
        solicitud = '''Necesito que actues como un entrenador deportivo de alta calidad, tu proposito es dar excelente rutinas de ejercicio para las personas dependiendo de las distintas caracteristicas de la persona en si. La rutina que vas a proporcionar va a ser en formato json de la manera que te voy a decir a continuación: {"Tiempo_Aproximado" : "Tu respuesta", "Tiempo_de_Descanso": "Tu respuesta", "Calentamiento" : "Tu respuesta" , "Numero_de_series_por_ejercicio" : "Tu respuesta", "Ejercicios" : {"Ejercicio_1": "Tu respuesta", "Ejercicio_2": "Tu respuesta", "Ejercicio_3": "Tu respuesta - Numero de repeticiones", "Ejercicio_4": "Tu respuesta ", "Ejercicio_5": "Tu respuesta", "Ejercicio_6": "Tu respuesta",.....,"Ejercicio_n":"Tu respuesta"}}

'''+ f'''Las caracteristicas de la persona son las siguientes: Genero: {profile['genero']}, Objetivo: {profile['objetivo']}, Edad: {profile['edad']} años, Condiciones medicas: {profile['condiciones']}, Deporte practicado: {profile['deporte']}, Equipamiento para entrenar: {equipa}, Lugar de entreno: {place}
La cantidad de ejercicios depende de tu criterio o de lo que la persona especifique, lo mismo con la el tiempo aproximado y el tiempo de descanso. Estas son las cualidades especificas que quiere la persona en su rutina: {user_input}. Dado el caso que la persona no especifique nada, o lo que te haya dicho no tenga nada de relevancia, elige por ella lo mas adecuado basado en los datos que se te han dado.

Por ultimo solamente quiero que la respuesta que me des sea el json, no quiero que me des ningun mensaje mas para que des un mejor rendimiento.'''
        
        # Llamar a la IA para obtener la respuesta
        respuesta_vanilla = get_completion(solicitud)
        respuesta_dict = self.process_response(respuesta_vanilla)

        return respuesta_vanilla, respuesta_dict

    def process_response(self, response):
        # Procesar la respuesta de la IA (convertirla a JSON)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {}