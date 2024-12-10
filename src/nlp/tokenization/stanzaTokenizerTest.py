import stanza

def tokenizerStanza():
    nlp = stanza.Pipeline("es", processors='tokenize, mwt', use_gpu=False)
    #nlp = stanza.Pipeline("es")
    textoEn = "I can't believe John's café—where they sell New York-style bagels—isn't open 24/7 anymore... What're they thinking? 🤔 Anyway, I’ve gotta go pick up some groceries—milk, bread, eggs, etc.—before heading to grandma's house for her birthday party at 5:00 p.m. Oh, btw, are we still on for the AI workshop next Fri?"
    textoEs = "¡No puedo creerlo! Juan's Café—donde venden pan recién hecho, tipo francés—cerró temprano hoy... ¿Qué estarán pensando? 😕 En fin, voy a recoger unas cosas: leche, pan, huevos, etc., antes de ir a casa de mi abuela para su fiesta de cumpleaños a las 17:00. Ah, por cierto, ¿seguimos con la reunión de Inteligencia Artificial el próximo viernes?"
    doc = nlp(textoEs)
    for sentence in doc.sentences:
        for word in sentence.words:
            print(word.lemma)
    #print(doc)

if __name__ == '__main__':
    tokenizerStanza()
