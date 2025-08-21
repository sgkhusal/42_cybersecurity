# Cybersecurity M02 - EX01

## Deserialization RCE (Remote Code Execution)

- Ocorre quando a aplicação desserializa dados vindos do usuário sem validação.
Exemplo: usar `pickle.loads()`, `ObjectInputStream` (Java), `Marshal.load` (Ruby)

- O formato de serialização permite executar código (por design ou por abuso de bibliotecas).
Exemplo: Pickle é extremamente inseguro: qualquer pessoa pode gerar código arbitrário sobrescrevendo o método ``__reduce__`` para executar funções arbitrárias