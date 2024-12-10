from transformers import pipeline

# Cargar el modelo T5 preentrenado para la corrección
corrector = pipeline("text2text-generation", model="t5-small", tokenizer="t5-small")

# Texto a corregir
texto = "en las nue vas elciconespresidencial del año 2024, mucha gente a opinucado bastente sobre intel igenciaartificial"

# Pedimos al modelo que corrija el texto
resultado = corrector("corregir: " + texto)

# Imprimir el texto corregido
texto_corregido = resultado[0]['generated_text']
print("Texto corregido:", texto_corregido)
