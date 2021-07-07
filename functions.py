from reportlab.pdfgen import canvas
from math import factorial
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random

from reportlab.platypus.doctemplate import FrameBreak

title = 'Atividade 2'
student = 'Marcos Guilherme (19111175)' 
pdf = canvas.Canvas(title + '- ' + student)
pdf.setTitle(title + '- ' + student)

# print("PDF gerado com sucesso!\nNome do arquivo: {}".format(title + '- ' + student))

##passando apenas os valores desejados para uma lista
def get_archive_lists (arquivo, list_names, list_genders):
    print('Gerando lista de nomes...')
    print('Gerando lista de gêneros...')

    for linha in arquivo:
        valores = linha.split(',')
        list_names.append(valores[0])
        list_genders.append(valores[1])
    return list_names, list_genders

##apresentação no pdf
def write_apresentation(text, reference) :
    pdf.drawString(50, 800, text)
    pdf.drawString(50, 780, reference)

##amostragens
def amostragem_aleatoria(lista) :
    print('Gerando amostragem aleatória...')

    tam = len(lista)
    qtd = 10

    jobs_selecionados = random.sample(lista, qtd)
    print('     ¬ Gerando amostragem aleatória (selecionando cargos)...')
    
    pdf.drawString(50, 750, "AMOSTRAGEM ALEATÓRIA")
    pdf.drawString(50, 730, 'A dataset dispõe de {} cargos. O estudo por meio desta amostragem escolheu {} desses:'.format(tam, qtd))

    eixoX = 50
    eixoy = 710
    for i in jobs_selecionados:
        pdf.drawString(eixoX, eixoy, i + ',')
        eixoy -= 20
    pdf.drawString(50, eixoy, 'Observação pós amostragem:')
    eixoy -= 20
    pdf.drawString(eixoX, eixoy, 'Todos os {} cargos possuem a mesma chance de serem selecionados.'.format(tam))

def amostragem_estratificada(lista) :
    print('Gerando amostragem estratificada...')
    eixoX = 50
    eixoY = 450

    pdf.drawString(eixoX, eixoY, "AMOSTRAGEM ESTRATIFICADA")
    
    
    #criando listas dos cargos
    tam = len(lista)
    
    lista1 = []
    lista2 = []
    lista3 = []

    print('     ¬ Gerando amostragem estratificada (salvando em listas)...')

    qtd_lista1 = tam // 3
    for i in range(qtd_lista1):
        lista1.append(lista[i])
    
    resto1 = (tam - qtd_lista1)
    qtd_lista2_and_lista3 = resto1 // 2

    for k in range(qtd_lista1, (qtd_lista1 + qtd_lista2_and_lista3)):
        lista2.append(lista[k])

    for j in range( (qtd_lista1 + qtd_lista2_and_lista3), tam ):
        lista3.append(lista[j])

    #selecionando três cargos de cada lista
    cargos_selecionados = []
    cargos_selecionados.append(random.sample(lista1, 3))
    cargos_selecionados.append(random.sample(lista2, 3))
    cargos_selecionados.append(random.sample(lista3, 3))

    print('     ¬ Gerando amostragem estratificada (selecionando cargos)...')

    eixoY -= 20
    pdf.drawString(eixoX, eixoY, 'Nessa amostragem, dividi os cargos em "subcargos". Dividi em arrays.')

    eixoY -= 20
    pdf.drawString(eixoX, eixoY, 'Ou seja, temos {} cargos, dividi em 3 arrays com {}, {} e {} cargos respectivamente.'.format(tam, len(lista1), len(lista2), len(lista3)))

    eixoY -= 20
    pdf.drawString(eixoX, eixoY, 'Dessa forma, temos representantes aleatórios de cada array ou "subcargo". São eles:')

    lista_aux = []
    for listas in cargos_selecionados:
        for j in range(len(listas)):
            lista_aux.append(listas[j])

    eixoY -= 20
    pdf.drawString(eixoX, eixoY, '"Subcargo" 1:')

    eixoY -= 20
    for i in range(3):
        pdf.drawString(eixoX, eixoY, '{}'.format(lista_aux[i]))
        eixoX += 150

    eixoX = 50
    eixoY -= 20
    pdf.drawString(eixoX, eixoY, '"Subcargo" 2:')

    eixoY -= 20
    for i in range(3, 6):
        pdf.drawString(eixoX, eixoY, '{}'.format(lista_aux[i]))
        eixoX += 150

    eixoX = 50
    eixoY -= 20
    pdf.drawString(eixoX, eixoY, '"Subcargo" 3:')

    eixoY -= 20
    for i in range(6, 9):
        pdf.drawString(eixoX, eixoY, '{}'.format(lista_aux[i]))
        eixoX += 150

def amostragem_sistematica(lista) :
    print('Gerando amostragem sistemática...')
    eixoX = 50
    eixoY = 230

    pdf.drawString(eixoX, eixoY, "AMOSTRAGEM SISTEMÁTICA")

    eixoY -= 20
    pdf.drawString(eixoX, eixoY, "Nessa amostra, foi atribuído um número a cada cargo.")

    eixoY -= 20
    pdf.drawString(eixoX, eixoY, "Depois, foi selecionado um cargo a cada 200 cargos. Foram eles: ")

    eixoY -= 20
    for i in range(1, len(lista), 200) :
        pdf.drawString(eixoX, eixoY, lista[i] + ', ')
        eixoX += 110

def distribuicao_de_bernoulli(lista) :
    print('Gerando distribuição de Bernoulli...')
    eixoX = 50
    eixoY = 150

    pdf.drawString(eixoX, eixoY, 'DISTRIBUIÇÃO DE BERNOULLI')

    masc = 0
    fem = 1

    for i in lista:
        if i == 'Male':
            masc += 1
        if i == 'Female' :
            fem += 1

    male = [0]*masc
    female = [1]*fem

    uniao = male + female
    
    media = np.mean(uniao)
    variancia = np.var(uniao)

    eixoY -= 15
    pdf.drawString(eixoX, eixoY, 'A média é: {:.2f} e a variância é: {:.2f}'.format(media, variancia))
        
    return ['{:.2f}'.format(media), '{:.2f}'.format(variancia)]
    

def probabilidadeBinomial(x,n,p,q):
    return (factorial(n)/(factorial(n-x)*factorial(x)))*(p**x)*(q**(n-x))

def calculate_probabilidade_binomial(lista) :
    print('Gerando probabilidade binomial...')

    p_and_q = distribuicao_de_bernoulli(lista)

    p = float(p_and_q[0])
    q = float(p_and_q[1])
    n = 7
    probabilidades = []

    for x in range(8):
        px = probabilidadeBinomial(x,n,p,q)
        # print('P(',x,') =',px)
        probabilidades.append(px)

    # print(np.sum(probabilidades))

    basewidth = 200
    img = Image.open('fig.png')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('fig.png') 

    imagem = 'fig.png'

    pdf.drawImage(imagem, 50, 2)
    pdf.drawString(250, 80, 'Observando o grafico, podemos notar que a maior')
    pdf.drawString(250, 50, 'probablilidade de sucesso é o 5.')


    print('Gerando PDF..')
    print("PDF GERADO COM SUCESSO!")

    pdf.save()
