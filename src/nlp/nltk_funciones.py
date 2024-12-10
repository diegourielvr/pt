from nltk.corpus import stopwords
from nltk.downloader import download
from nltk.tokenize import NLTKWordTokenizer
from nltk.stem import (WordNetLemmatizer,
                       SnowballStemmer)

# Lematizador: NLTK solo ofrece lematización para el idioma inglés

def descargar_paquetes():
    download('stopwords') # descargar corpus de stopwords

def nltk_tokenizar(lista_textos: list[list[str]]):
    """
    Algunos símbolos como '¿' o '¡' no los separa correctamente
    """

    tokenizador = NLTKWordTokenizer()
    return tokenizador.tokenize_sents(lista_textos)

def nltk_eliminar_stopwords(lista_tokens: list[list[str]], lang='spanish'):
    """
    ['Estaba', 'corriendo', 'por', 'la', 'mañana', 'acompañado', 'de', 'mis',
    'amigos'] -> ['Estaba', 'corriendo', 'mañana', 'acompañado', 'amigos']
    """

    sw = stopwords.words(lang) # 'spanish' | 'english'
    # print(stopwords.words(sw)) # Mostrar lista de stopwords
    return [[token
             for token in tokens if not token in sw]
            for tokens in lista_tokens]

# Snowball es un lenguaje de programación desarollado por Martin Porterr
# para crear algoritmos de stemming
def nltk_stemming(lista_textos: list[list[str]], lang='spanish'):
    """
    ['Estaba', 'corriendo', 'mañana', 'acompañado', 'amigos'] ->
    ['estab', 'corr', 'mañan', 'acompañ', 'amig']
    """

    #print(SnowballStemmer.languages) # Mostrar lenguajes soportados
    stemmer = SnowballStemmer(lang) # 'spanish' | 'english'
    return list(map(
        lambda tokens: [stemmer.stem(token) for token in tokens],
        lista_textos))