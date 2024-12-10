import spacy

def sc_tokenizar(lista_textos: list[list[str]], lang='es'):
    """
    '¿Cuál es tu nombre?' -> ['¿', 'Cuál', 'es', 'tu', 'nombre', '?']
    'What's your name?' -> ['What', "'s", 'your', 'name', '?']
    """

    if lang == "en": nlp = spacy.load("en_core_web_sm") # cargar modelo en español
    elif lang == "es": nlp = spacy.load("es_core_news_sm") # cargar modelo en inglés

    return list(map(
        lambda texto: [token.text for token in nlp(texto)],
        lista_textos
    ))

def sc_tokenizar_expresiones_multipalabra(lista_textos: list[list[str]],
                                          lang='es'):
    """
    ["¿La Inteligencia Artificial es interesante? si o no, jeje.",
    "¿Sabes cómo se llama el presidente de Estados Unidos de America?"] ->
    [['¿', 'La', 'Inteligencia Artificial', 'es', 'interesante', '?',
    'si', 'o', 'no', ',', 'jeje', '.'],
    ['¿Sabes', 'cómo', 'se', 'llama', 'el', 'presidente', 'de',
    'Estados Unidos de America', '?']]
    """

    if lang == "en": nlp = spacy.load("en_core_web_sm") # cargar modelo en español
    elif lang == "es": nlp = spacy.load("es_core_news_sm") # cargar modelo en inglés

    lista_tokens = []
    for texto in lista_textos:
        doc = nlp(texto)
        with doc.retokenize() as retokenizer: # Unir tokens
            # Unir entidades reconocidas en un solo token
            for ent in doc.ents:
                retokenizer.merge(ent)
        lista_tokens.append([token.text for token in doc])
    return lista_tokens

def sc_eliminar_signos_puntuacion(lista_tokens: list[list[str]], lang='es'):
    """[["árbol", ".", "¿", "?", "¡", "!", ","]] -> [['árbol']]"""

    if lang == "en": nlp = spacy.load("en_core_web_sm") # cargar modelo en español
    elif lang == "es": nlp = spacy.load("es_core_news_sm") # cargar modelo en inglés

    return list(map(
        lambda tokens: [token
                        for token in tokens if not nlp.vocab[token].is_punct],
        lista_tokens
    ))

def sc_eliminar_stopwords(lista_tokens: list[list[str]], lang='es'):
    if lang == "en": nlp = spacy.load("en_core_web_sm") # cargar modelo en español
    elif lang == "es": nlp = spacy.load("es_core_news_sm") # cargar modelo en inglés

    return list(map(
        lambda tokens: [token
                        for token in tokens if not nlp.vocab[token].is_stop],
        lista_tokens
    ))

def sc_lematizar(lista_tokens: list[list[str]], lang='es'):
    """
    ['Desayunamos', 'juntos', 'trabajabamos'] ->
    ['desayunar', 'junto', 'trabajabar']
    """

    if lang == "en": nlp = spacy.load("en_core_web_sm") # cargar modelo en español
    elif lang == "es": nlp = spacy.load("es_core_news_sm") # cargar modelo en inglés

    return list(map(
        lambda tokens: [nlp(token)[0].lemma_ for token in tokens],
        lista_tokens
    ))

def sc_token_stop_punct_lemma(lista_textos, lang='es'):
    """Aplicar varias tecnicas de NLP solo con Spacy
    """

    if lang == "en": nlp = spacy.load("en_core_web_sm") # cargar modelo en español
    elif lang == "es": nlp = spacy.load("es_core_news_sm") # cargar modelo en inglés

    return [[token.lemma_
             for token in doc if not token.is_stop and not token.is_punct]
            for doc in nlp.pipe(lista_textos)]

def sc_mwt_stop_punct_lemma(lista_textos, lang='es'):
    if lang == "en": nlp = spacy.load("en_core_web_sm") # cargar modelo en español
    elif lang == "es": nlp = spacy.load("es_core_news_sm") # cargar modelo en inglés

    lista_tokens = []
    for doc in nlp.pipe(lista_textos):
        with doc.retokenize() as retokenizer:  # Unir tokens
            # Unir entidades reconocidas en un solo token
            for ent in doc.ents:
                retokenizer.merge(ent)

        lista_tokens.append([token.lemma_
                             for token in doc
                             if not token.is_stop and not token.is_punct])
