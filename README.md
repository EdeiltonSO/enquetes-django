# 📊 Enquetes em Django

## O que é isso?

É uma aplicação feita em Django para a criação de enquetes. Nela, o usuário pode isualizar uma lista de perguntas, acessar, votar e ver o resultado das respostas dadas.

Além disso, há um módulo para a administração do banco de dados.

## Como executar?

As instruções a seguir ainda podem estar incompletas. 

### Pra fazer só uma vez

- Instale o VirtualBox;
- Descompacte o `sd.zip` fornecido;
- Acesse a pasta descompactada;
- Atualize `ipAdrPrefix` no Vagrantfile para `192.168.56.101`;
- Se já existir uma máquina virtual sd*, execute `vagrant destroy`;
- Acesse o diretório do `Vagrantfile`;
- Execute `vagrant up`;
- Execute `vagrant ssh`;

(note que agora você tá dentro de vagrant@sd)

- Execute `cd /vagrant/web-folder/`;
- Faça o `git clone` deste repositório;
- Acesse a pasta criada com o clone;
- Execute `cp .env.example .env`;
- Preencha o `.env`;
- Execute `python manage.py runserver 0:8000`;
- Acesse `192.168.56.101:8000/enquetes`.

*confira no VirtualBox ou executando `vagrant global-status`

### Pra fazer sempre que for usar

- Acesse o diretório que contém o `Vagrantfile`;
- Execute `vagrant up`;
- Execute `vagrant ssh`;

(note que agora você tá dentro de vagrant@sd)

- Execute `cd /vagrant/web-folder/enquetes-django/`;
- Execute `python manage.py runserver 0:8000`;
- Acesse `192.168.56.101:8000/enquetes`.

## Quais rotas estão disponíveis?

A partir da URL `192.168.56.101:8000`, os seguintes caminhos podem ser acessados:

- `/admin`;
- `/enquetes`;
- `/enquetes/<question_id>`;
- `/enquetes/<question_id>/resultados`;
- `/enquetes/<question_id>/votar`.