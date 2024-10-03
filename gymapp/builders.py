# gymapp/builders.py

class RoutineBuilder:
    def __init__(self):
        self.routine = {
            "Lunes": {},
            "Martes": {},
            "Miercoles": {},
            "Jueves": {},
            "Viernes": {},
            "Sabado": {},
            "Domingo": {}
        }

    def add_day_routine(self, day, approx_time, rest_time, warm_up, exercises):
        """
        Add routine details for a given day.
        """
        self.routine[day] = {
            "Tiempo_Aproximado": approx_time,
            "Tiempo_de_Descanso": rest_time,
            "Calentamiento": warm_up,
            "Ejercicios": exercises
        }
        return self

    def add_rest_day(self, day):
        """
        Mark a day as a rest day.
        """
        self.routine[day] = {"Descanso": "Descanso"}
        return self

    def build(self):
        """
        Return the final routine structure.
        """
        return self.routine

