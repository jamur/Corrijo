#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import re, csv
pat = csv.reader(open('listagem patrimonial do setor 16-06-2009teste.csv'), delimiter=';')
writer = csv.writer(open('corrijido.csv', 'wb'))
linha = pat.next()
 
while True:
  linhanova = ""
  t = linha[2]
  result = re.match( r'\d{3}\.\d{3}', t) 
  if result:
    print result.group(0)
    linhanova = linha # linhanova = linha a ser gravada no novo arquivo
  else:
    writer.writerow( linha )  # se não for número de patrimônio grava como está
    linha = pat.next()        # e volta para o while 
    continue # vai para o while
    
  # itera dentro do registro (até o próximo número de patrimônio)
  linha = pat.next()
  while True:
    t = linha[2] # lê a célula da coluna núm. de patrimônio
    result = re.match( r'\d{3}\.\d{3}', t) # verifica é do padrão núm. patrim.
    result2 = re.match( r'\w', linha[0] ) # se houver uma palavra na 1ª col. 
    if result or result2: # se na próxima for um número de patrimônio
      break               # termina esse laço (while)
    else:
      # agora verifica se tem a continuação da descrição do ítem, na segunda
      # linha (só que fica uma coluna antes)
      if re.match( r'\w', t):
        linhanova[3] += ' - ' + linha[2]
      linha = pat.next() # lê próx. linha - termina o prog se não houver (raise)

  writer.writerow(linhanova) # escreve a linha modificada no arquivo
# termina o loop quando não houver mais linhas no arquivo
