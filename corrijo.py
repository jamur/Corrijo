#!/usr/bin/env python
import re, csv
pat = csv.reader(open('listagem patrimonial do setor 16-06-2009teste.csv'), delimiter=';')
writer = csv.writer(open('corrijido.csv', 'wb'))
linha = pat.next()
 
while True:
  linha = pat.next()
  t = linha[2]
  result = re.match( r'\d{3}\.\d{3}', t)
  if result:
    print result.group(0)
    writer.writerow(linha)
