from development import NaturalLanguageProcessing

filename = '5000saetze'
textanalysis = NaturalLanguageProcessing(filename=filename)
textanalysis.textanalizer()
textanalysis.visualization()