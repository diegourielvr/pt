import os
from symspellpy import SymSpell

ruta_prefijo = os.path.join(os.getcwd(),
                            "nlp", "corrector", "diccionarios")

def sp_corregir_ortografia(texto, lang):
    if lang == "en":
        dictionary_path = os.path.join(ruta_prefijo, "en-80k.txt")
    else:
        dictionary_path = os.path.join(ruta_prefijo, "es-100l.txt")

    spell = SymSpell(max_dictionary_edit_distance=2,
                     prefix_length=7)
    load = spell.load_dictionary(dictionary_path,
                                 term_index=0,
                                 count_index=1,
                                 encoding="utf-8")

    sugerencia = spell.word_segmentation(texto, max_edit_distance=2,
                                         max_segmentation_word_length=None)  # mantener los números
    return sugerencia.corrected_string