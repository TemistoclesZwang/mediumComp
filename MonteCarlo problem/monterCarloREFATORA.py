import pandas as pd
# ;LIMPAR COMENTARIOS NA VERSÃO FINAL

array_aprox = []
capacidadeMax  = 3 #120 MC15 #.eixo Y número 1
passagensOverbooking = 2 #quantas passagens a mais quero verificar
calcRangePassagensaMais = capacidadeMax + passagensOverbooking#-1 pois o range começa em 0 no eixo Y da primeira colulna

def bernoulli_0_ou_1(qtdPassagens):
   from random import random
   # qtdPassagens = int(input())
   n = [0.0] * qtdPassagens #para gerar X números flutuantes

   for i in range(qtdPassagens):
      n[i] = random()
      if n[i] < 0.1:
         n[i] = 0
      elif n[i] > 0.1:
         n[i] = 1

   return n


def gerarSimulacoesBernoulli(df):
   for i in range(1, qtdSimulacoes+1): #SEMPRE UMA A MAIS DEVIDO A COLUNA A MENOS GERADA PELO PANDAS df
      df.insert(i, f"U_{i}", bernoulli_0_ou_1(qtdPassagens), True)


# def no_Show(totalPassagensVendidas):
#    if totalPassagensVendidas == calcRangePassagensaMais: 
#       return 0 #se ninguém faltou não tem no show
#    elif totalPassagensVendidas < calcRangePassagensaMais:
#       return (totalPassagensVendidas - capacidadeMax) #Esse 1 é do index do pandas
#    else:
      # return 0

def no_Show(totalPassagensVendidas,qtdPassagens): 
   if totalPassagensVendidas == calcRangePassagensaMais: 
      return 0 #se ninguém faltou não tem no show
   else:
      return qtdPassagens - totalPassagensVendidas

def overbooking(totalPassagensVendidas):
   if totalPassagensVendidas > capacidadeMax:
      return totalPassagensVendidas-capacidadeMax
   else:
      return 0


def vendas(totalPassagensVendidas):
   return totalPassagensVendidas * 200


def multa(totalPassagensVendidas):
   return  overbooking(totalPassagensVendidas)*(-1000)


def remarcacao(totalPassagensVendidas):
   return no_Show(totalPassagensVendidas,qtdPassagens)*20


def arrecadado(totalPassagensVendidas):
   return vendas(totalPassagensVendidas)+ multa(totalPassagensVendidas)+ remarcacao(totalPassagensVendidas)


def gerarInformacoesIndividuais(i,totalPassagensVendidas):
   
   print(f'Coluna:{i}')
   print (f"Soma: {totalPassagensVendidas}")
   print (f"No show: {no_Show(totalPassagensVendidas,qtdPassagens)}")
   print (f"Overbooking: {overbooking(totalPassagensVendidas)}")
   print (f"Multa: {multa(totalPassagensVendidas)}") 
   print (f"Vendas: {vendas(totalPassagensVendidas)}") 
   print (f"Remarcação: {remarcacao(totalPassagensVendidas)}")
   print (f"Arrecadado: {arrecadado(totalPassagensVendidas)}")
   print('\n')
   

def somarPassagens(df): #.eixo Y
   media_aproximacao = 0
   for i in range(1, qtdSimulacoes+1):
      Total = df[f"U_{i}"].sum() #total de cada coluna
      # no_Show(Total)
      # overbooking(Total)
      # multa(Total)
      # vendas(Total)
      # remarcacao(Total)
      # arrecadado(Total)

      media_aproximacao += arrecadado(Total)

   # .modo detalhado visual
      gerarInformacoesIndividuais(i,Total)
   print(20*'-')
   print(f'\n')
   print (f"### aproximacao: {media_aproximacao/(qtdSimulacoes)}")
   return media_aproximacao/(qtdSimulacoes)


for vendasaMais in range (capacidadeMax+1, calcRangePassagensaMais+1): #+1 pois quero que conte a partir da primeira passagem vendida a mais
   qtdPassagens = vendasaMais #.eixo X de passageiros
   qtdSimulacoes = 3 #.eixo Y de simulacoes (U) 
   data = {'': [' '] * qtdPassagens}
   df = pd.DataFrame(data)# converter o dicionário em dataframe
   gerarSimulacoesBernoulli(df)
   # somarPassagens(df) #,teste
   array_aprox.append(somarPassagens(df))
   print (f"### vendas a mais: {(vendasaMais - capacidadeMax)+1}")
   # print (f"### vendas a mais: {vendasaMais} \n### aproximacao: {somarPassagens(df)}")
   print(df) #,gerar tabela grafica no terminal


