import json
from game.utils.constants import SCORE_FILE_PATH
import os

def read_data():
    """Lee los datos de un archivo JSON.

    Args:
        Sin agumentos. La ruta ya está guardada en constants.py

    Returns:
        dict: Los datos del archivo JSON.
    """
    try: 
        with open(SCORE_FILE_PATH) as contain :
            scores = json.load(contain)
    except FileNotFoundError:
        scores = {"score": 0}
    return scores    

def save_data(datos):
    """escribe los datos de un archivo JSON.

    Args:
        datos (str): dict 

    Returns:
        Null
    """
    if os.path.exists(SCORE_FILE_PATH):
        with open(SCORE_FILE_PATH, "w") as archivo_json:
            json.dump(datos, archivo_json) # indent=2 para una salida con formato legible
       