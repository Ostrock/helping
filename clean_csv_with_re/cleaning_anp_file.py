import re
import pandas as pd 
from requests import get

path = 'Documentos/code/estudos/helping/'
cleaned_file = '2019-producaomar-clean.csv'
url = 'http://www.anp.gov.br/arquivos/acesso-informacao/dp/2019-producaomar.csv'
working_file = url.split('/')[-1]
downloaded_file = get(url)
with open(path + working_file, 'wb') as wf:
    wf.write(downloaded_file.content)

with open(path + working_file, 'r', encoding = 'latin-1') as f:
    dot_sep = re.sub(r'""([+-]?[0-9]+),([0-9]+)""', r'\1.\2', f.read())
    strip_quote = re.sub(r'""', r'', dot_sep)
    del dot_sep
    end_line_quote = re.sub(r'(\n)"', r'\1', strip_quote)
    del strip_quote
    begin_line_quote = re.sub(r'"(\n)', r'\1', end_line_quote)
    del end_line_quote
    clean_string = re.sub(r'\n,+', r'', begin_line_quote)
    del begin_line_quote
    with open(path + 'clean-' + working_file, 'w') as nf:
        nf.write(clean_string)    