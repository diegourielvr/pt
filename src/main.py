import os.path
import pandas as pd

from gensim.models import Word2Vec

from src.nlp.nltk_funciones import nltk_stemming
from src.nlp.spacy_funciones import (sc_tokenizar,
                                     sc_eliminar_stopwords,
                                     sc_lematizar,
                                     sc_token_stop_punct_lemma,
                                     sc_eliminar_signos_puntuacion)
#from src.nlp.corrector.transformersTest import texto_corregido
from src.nlp.symspell_funciones import sp_corregir_ortografia

def filtrar_y_corregir(ruta_transcripciones, ruta_texto_corregido):
    # Cargar los datos con pandas
    columnas = ['lang', 'text']
    print("Cargando los datos...")
    df = pd.read_csv(ruta_transcripciones, usecols=columnas)

    # filtrar solo textos en ingles y español
    df = df[((df['lang'] == 'es') | (df['lang'] == 'en'))]

    # todo: ¿Convertir a minusculas?

    # Aplicar corrección ortográfica con symspellpy
    print("Corrigiendo información...")
    # axis=1 aplicar a cada fila, axis=0 aplicar a cada columnas
    df['text'] = df.apply(
        lambda  x: sp_corregir_ortografia(x['text'], x['lang']), axis=1)

    # Guardar texto corregido
    print("Guardando resultados...")
    df.to_csv(ruta_texto_corregido, index=False, encoding="utf-8")
    print(f"Resultado guardado en {ruta_texto_corregido}")
    return True

def preprocesamiento_partes(ruta):
    columnas = ['lang', 'text']
    print("Cargando los datos...")
    df = pd.read_csv(ruta, usecols=columnas)

    # dividir por idioma
    df_es = df[df['lang'] == 'es']
    df_en = df[df['lang'] == 'en']
    # texto = df_es['text'][0]
    texto = df_es['text']
    tokens = sc_tokenizar(texto, 'es')
    # todo: MWT

    print("Eliminando StopWords...")
    tokens = sc_eliminar_stopwords(tokens, 'es')

    print("Eliminando signos de puntuacion...")
    tokens = sc_eliminar_signos_puntuacion(tokens, 'es')

    print("Aplicando lematización")
    tokens = sc_lematizar(tokens, 'es')

    # Stemming
    print("Aplicando stemming")
    tokens = nltk_stemming(tokens, 'spanish')

    modelo = Word2Vec(
        sentences=tokens, # lista de tokens
        vector_size=100, # dimensión de los vectores de palabras
        window=2, # contexto (palabras a la izq y der)
        min_count=1, # ignorar palabras con frecuencia menor a min-count
        workers=4, # Número de hilos
        epochs=50,
        sg=1, # skipgram (a partir de una palabra central predecir las palabras de contexto)
        hs=1 # hierarchical softmax
    )

    w = "mexican" # stem
    if w in modelo.wv:
        # vector = modelo.wv[w]
        # print(f"Vector de ({w}): {vector}")
        sims = modelo.wv.most_similar(w, topn=10) # Obtener palabras similares
        print(sims)
    else: print(f"La palabra {w} no está en el corpus")

    # Obtener el vocabulario del modelo
    # vocabulario = list(modelo.wv.key_to_index.keys())
    # print(vocabulario)


def preprocesamiento_spacy(ruta):
    columnas = ['lang', 'text']
    print("Cargando los datos...")
    df = pd.read_csv(ruta, usecols=columnas)

    # dividir por idioma
    df_es = df[df['lang'] == 'es']
    df_en = df[df['lang'] == 'en']
    texto = df_es['text']

    # todo: MWT
    print("Aplicando SWT, StopWords, signos de puntuación, Lemmatization...")
    tokens = sc_token_stop_punct_lemma(texto, 'es')

    # Stemming
    print("Aplicando stemming")
    tokens = nltk_stemming(tokens, 'spanish')

    modelo = Word2Vec(
        sentences=tokens, # lista de tokens
        vector_size=100, # dimensión de los vectores de palabras
        window=2, # contexto (palabras a la izq y der)
        min_count=1, # ignorar palabras con frecuencia menor a min-count
        workers=4, #Número de hilos
        epochs=50,
        sg=1, # skipgram (a partir de una palabra central predecpir las palabras de contexto)
        hs=1 # hierarchical softmax
    )

    w = "mexican" # stem
    if w in modelo.wv:
        vector = modelo.wv[w]
        # print(f"Vector de ({w}): {vector}")
        sims = modelo.wv.most_similar(w, topn=10) # Obtener n palabras similares
        print(sims)
    else: print(f"La palabra {w} no está en el corpus")

    # Obtener el vocabulario del modelo
    # vocabulario = list(modelo.wv.key_to_index.keys())
    # print(vocabulario)

if __name__ == '__main__':
    ruta_datos_prefijo = os.path.join(os.getcwd(), "recoleccion", "datos")
    ruta_transcripciones = os.path.join(ruta_datos_prefijo, "transcripciones.csv")
    ruta_texto_corregido = os.path.join(ruta_datos_prefijo, "datos_corregidos.csv")

    # filtrar_y_corregir(ruta_transcripciones, ruta_texto_corregido)

    # Generar embeddings
    preprocesamiento_partes(ruta_texto_corregido)
    # preprocesamiento_spacy(ruta_texto_corregido)
