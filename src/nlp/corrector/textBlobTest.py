from textblob import TextBlob

def corregir():
    """
    No permite unir o separar palabras
    Solo disponible para idioma ingles
    :return:
    """
    tb = TextBlob("avion")
    print(tb.correct())


