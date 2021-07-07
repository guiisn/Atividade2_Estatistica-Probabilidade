from reportlab.pdfgen import canvas
import numpy as np
import functions

apresentation_text = 'Atividade 2'
reference_text = 'Referência: https://www.kaggle.com/nilimajauhari/glassdoor-analyze-gender-pay-gap'

# pdf = canvas.Canvas('test')
# pdf.setTitle('teste')
# pdf.drawString(150, 250, 'sagdbjadsahdjsbajhbdsadasdshab')
# pdf.save()
functions.write_apresentation(apresentation_text, reference_text)

##abrindo aqrquivo
arquivo = open('dataset.csv', 'r')

lista_nomes = []
lista_genero = []

##chamando funções p pegar apenas valores desejados (nomes e generos)
functions.get_archive_lists(arquivo, lista_nomes, lista_genero)

arquivo.close()

##amostragem
functions.amostragem_aleatoria(lista_nomes)
functions.amostragem_estratificada(lista_nomes)
functions.amostragem_sistematica(lista_nomes)

##distribuição de bernoulli
functions.distribuicao_de_bernoulli(lista_genero)

functions.calculate_probabilidade_binomial(lista_genero)