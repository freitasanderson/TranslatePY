from deep_translator import GoogleTranslator
source = str(input("Digite a lingua de origem do texto ou deixe em branco para automático: "))
target = str(input("Digite a lingua de saída do texto ou deixe em branco para 'English': "))
texto = str(input("Digite o Texto: "))

tradutor = GoogleTranslator(source=source,target=target)

textoTraduzido = tradutor.translate(texto)

print(f"Texto: {textoTraduzido}")