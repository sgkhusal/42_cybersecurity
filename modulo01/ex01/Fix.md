1. Desabilitar entidades externas e DTDs no parser e não processar DTDs e nem acessar a rede

```py
parser = etree.XMLParser(no_network=False, resolve_entities=True)
...
```

vira:
```py
parser = etree.XMLParser(no_network=True, resolve_entities=False, load_dtd=False)
...
```

Isso bloqueia os ataques de leitura de arquivos e SSRF via XXE

2. Ou usar bibliotecas seguras para a linguagem usada, que têm proteções embutidas
No caso do python, seria a `defusedxml`:

```py
xml = request.form['xml']
parser = etree.XMLParser(no_network=FalseU, resolve_entities=True) 
try:
    doc = etree.fromstring(str(xml), parser)
    parsed_xml = etree.tostring(doc)
...
```

vira:

```py
from defusedxml.lxml import fromstring

...
xml = request.form['xml']
try:
    doc = fromstring(xml)
    parsed_xml = etree.tostring(doc)
...
```


3. Como sempre, sanitizar qualquer dado vindo do usuário, nunca usá-lo diretamente
- Validar contra esquemas XSD quando aplicável.

4. Limitar tamanho máximo do XML recebido e tempo de parsing (Billion Laughs attack)