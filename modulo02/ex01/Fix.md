1. Nunca desserializar dados não confiáveis, com mecanismos que permitam execução de código, como é o caso do `pickle`

2. Usar formatos seguros: 
- JSON, YAML seguro, XML seguro (com validadores)
- usar parsers restritos, que convertem apenas em tipos primitivos (dict, list, string, int) ou tipos/classes esperadas, sem objetos arbitrários

3. Assinar dados serializados para garantir que não foram adulterados (ex: `JWT` ao invés do `pickle`)

4. Usar o Princípio do Menor Privilégio
O processo do app deve ser executado com permissões mínimas

