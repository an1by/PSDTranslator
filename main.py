from deep_translator import GoogleTranslator
import psd_tools

inputName = input("PSD-file name (example: Model.psd): ")
outputName = input("Output PSD-file name (example: output.psd. Default - translated PSD-file name): ")
targetLanguage = input("Target Language (Default - en): ")
if targetLanguage.strip() == '':
    targetLanguage = 'en'

translator = GoogleTranslator(source='auto', target=targetLanguage)
if outputName.strip() == '':
    outputName = translator.translate(inputName)

psd = psd_tools.PSDImage.open(inputName)

def renameLayer(group: psd_tools.api.layers.Group):
    previous = group.name
    translated = translator.translate(previous)
    if translated is None:
        translated = previous
    group.name = translated
    print(f"Translated: {previous} -> {translated}")


c = 0
for layer in psd.descendants():
    c += 1
    renameLayer(layer)

psd.save(outputName)
print(f"PSD saved to \"{outputName}\". Translated layers: {c}")