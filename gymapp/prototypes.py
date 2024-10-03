# gymapp/prototypes.py

import copy
from .models import Rutina_Semanal

class RoutinePrototype:
    def __init__(self, original_routine):
        self.original_routine = original_routine

    def clone(self, user=None, modifications=None):
        """
        Clone the routine and apply any modifications.
        """
        # Create a deep copy of the original routine
        cloned_routine = copy.deepcopy(self.original_routine)
        
        # If a new user is provided, assign the routine to this user
        if user:
            cloned_routine.user = user

        # Apply any other modifications provided
        if modifications:
            for key, value in modifications.items():
                setattr(cloned_routine, key, value)

        # Reset ID to create a new entry in the database
        cloned_routine.id = None
        cloned_routine.save()
        
        return cloned_routine
