# Cybersecurity M01 - EX02

## SSRF + LFI

### SSRF (Server-Side Request Forgery):
- o ataque faz o servidor fazer requisições HTTP/HTTPS para destinos arbitrários
- ocorre quando a aplicação permite que um usuário forneça uma url (por exemplo, para carregar uma imagem ou buscar dados de uma API externa). Se o input não for validado, o hacker pode modificar esse valor
- pode conseguir acessar serviços internos que não deveriam estar expostos ao hacker (Ex: `http://localhost:8080/admin`)
- pode conseguir acessar metadados de servidores de nuvem
- pode conseguir acessar serviços de backend

Riscos:
- vazamento de informações internas (endpoints, serviços, arquivos)
- acesso de rede privadas (internal port scanning)
- escalada de privilégios (servidores de nuvem)
- pode levar a RCE (Remote Code Execution)

### LFI (Local File Inclusion)
Quando o atacante consegue fazer a aplicação acessar e carregar arquivos do servidor

### O problema
O código aceita qualquer caminho, incluindo caminhos para arquivos do servidor. Também aceita qualquer tipo de arquivo.