#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import re, csv
pat = csv.reader(open('listagem patrimonial do setor 16-06-2009teste.csv'), delimiter=';')
writer = csv.writer(open('corrijido.csv', 'wb'))
linha = pat.next()
 
while True:
  t = linha[2]
  result = re.match( r'\d{3}\.\d{3}', t)
  if result:
    print result.group(0)
    linhanova = linha
  else:
    writer.writerow( linha ) #se não for número de patrimônio grava como está
    linha = pat.next()
    continue
  linha = pat.next()
  result = re.match( r'\d{3}\.\d{3}', t)

  # itera dentro do registro (até o próximo número de patrimônio)
  sai_do_um = False # para continue do loop de fora
  linha = pat.next()
  while True:
    t = linha[2]
    result = re.match( r'\d{3}\.\d{3}', t)
    if result:
      sai_do_um = True
      break
    else:
      # agora verifica se tem uma palavra no início da 'célula'
      if re.match( r'\w', t):
        linhanova[2] += ' ' + linha[2]
      linha = pat.next()
  writer.writerow(linhanova)
  if sai_do_um:
    continue 

