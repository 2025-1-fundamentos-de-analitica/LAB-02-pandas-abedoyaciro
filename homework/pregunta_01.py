"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    import pandas as pd
    
    # Leer el archivo tbl0.tsv
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    
    # Retornar la cantidad de filas
    return df.shape[0]
