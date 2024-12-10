import os
from symspellpy import SymSpell, Verbosity

def symSpellTtest(texto, lang="es"):
    if lang == "en":
        dictionary_path = os.path.join(os.getcwd(), "diccionarios", "en-80k.txt")
    else:
        dictionary_path = os.path.join(os.getcwd(), "diccionarios", "es-100l.txt")

    # Diccionarios: https://github.com/wolfgarbe/SymSpell/tree/master/SymSpell.FrequencyDictionary
    # https://symspellpy.readthedocs.io/en/latest/api/symspellpy.html#symspellpy.symspellpy.SymSpell
    spell = SymSpell(max_dictionary_edit_distance=2, # Máxima distancia de edición para hacer búsquedas
                     prefix_length=7) # Longitud de prefijos de palabras

    # Cargar el diccionar
    # https://symspellpy.readthedocs.io/en/latest/api/symspellpy.html#data-class
    load = spell.load_dictionary(dictionary_path, # ruta + nombre de archivo
                                 term_index=0, # posicion de la columna donde se encuentran las palabras
                                 count_index=1, encoding="utf-8") # posición de la columna donde se encuentran las frecuencias
    if not load:
        print("El diccionario no pudo ser cargado")
        return

    for i, token in enumerate(texto.split()):
        # Encontrar
        suggestions = spell.lookup(token, # Encontrar sugerencias para una palabra dada. https://symspellpy.readthedocs.io/en/latest/api/symspellpy.html#symspellpy.symspellpy.SymSpell
                                   Verbosity.CLOSEST, # Cantidad de sugerencias devueltas. https://symspellpy.readthedocs.io/en/latest/api/symspellpy.html#enum-class
                                   max_edit_distance=2) # distancia de edicion máxima entre la palabra y sugerencias
        for sug in suggestions: # https://symspellpy.readthedocs.io/en/latest/api/symspellpy.html#data-class
            print(sug)
        print("----------")

def symSpellCompound(texto, lang="es"):
    if lang == "en":
        dictionary_path = os.path.join(os.getcwd(), "diccionarios", "en-80k.txt")
    else:
        dictionary_path = os.path.join(os.getcwd(), "diccionarios", "es-100l.txt")

    spell = SymSpell(max_dictionary_edit_distance=2, # Máxima distancia de edición para hacer búsquedas
                     prefix_length=7) # Longitud de prefijos de palabras

    load = spell.load_dictionary(dictionary_path, term_index=0, count_index=1,encoding="utf-8") # posición de la columna donde se encuentran las frecuencias
    if not load:
        print("El diccionario no pudo ser cargado")
        return None

    # https://symspellpy.readthedocs.io/en/latest/api/symspellpy.html#symspellpy.symspellpy.SymSpell
    text= "en las nue vas elciconespresidencial del año 2024, mucha gente a opinucado bastente sobre "
    sugerencias = spell.lookup_compound(texto, max_edit_distance=2, ignore_non_words=True) # mantener los números
    # Compound hace lo siguiente: corrige cadenas compuestas (puede separar o unir términos):
    #1. Hay un espacio insertado en una palabra correcta, lo cual genera dos términos incorrectos
    #2. Se omitio un espacio entre dos palabras correctas, lo cual genera un témino incorrecto

    #for s in sugerencias:
    #    print(s)
    return sugerencias[0].term

def symSpellSegmentation(texto, lang="es"):
    if lang == "en":
        dictionary_path = os.path.join(os.getcwd(), "diccionarios", "en-80k.txt")
    else:
        dictionary_path = os.path.join(os.getcwd(), "diccionarios", "es-100l.txt")

    spell = SymSpell(max_dictionary_edit_distance=2, # Máxima distancia de edición para hacer búsquedas
                     prefix_length=7) # Longitud de prefijos de palabras

    load = spell.load_dictionary(dictionary_path, term_index=0, count_index=1,encoding="utf-8") # posición de la columna donde se encuentran las frecuencias
    if not load:
        print("El diccionario no pudo ser cargado")
        return None

    # word_segmentation separa una cadena en subpalabras y hace accinoes similares a compound
    # https://symspellpy.readthedocs.io/en/latest/api/symspellpy.html#symspellpy.symspellpy.SymSpell.word_segmentation
    sugerencia = spell.word_segmentation(texto, max_edit_distance=2, max_segmentation_word_length=None) # mantener los números
    #print("Entrada: ",sugerencia.segmented_string)
    #print("Correción: ",sugerencia.corrected_string)
    return sugerencia.corrected_string

if __name__ == '__main__':
    textEs = "información sobre las nue vas elciconespresidencials del año 2, mucha gente a opinucado bastente sobre intel igenciaartificial"
    textEn= "The president of Un ited State of Amerca is now donald trump and i have $100 dollar"
    print("Segmentation")
    print("Entrada: ",textEn)
    print("Salida:", symSpellSegmentation(textEn, "en"))
    print("Entrada: ", textEs)
    print("salida:", symSpellSegmentation(textEs, "es"))
    print("Compound")
    print("Entrada: ",textEn)
    print("Salida:", symSpellCompound(textEn, "en"))
    print("Entrada: ", textEs)
    print("salida:", symSpellCompound(textEs, "es"))
    print("Lookup")
    symSpellTtest(textEs)
