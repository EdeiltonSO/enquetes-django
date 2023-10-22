Essa é a versão da documentação antes do projeto estar no GitHub. A principal diferença é que aqui não é mais necessário executar o `django-admin startproject`, pois o repositório já conta com o resultado dessa execução.

## Pra fazer só uma vez

- Instale o VirtualBox
- Descompacte o `sd.zip` fornecido
- Acesse a pasta descompactada
- Atualize `ipAdrPrefix` no Vagrantfile para `192.168.56.101`
- Se já existir uma máquina virtual sd*, execute `vagrant destroy`
- Acesse o diretório do `Vagrantfile`
- Execute `vagrant up`
- Execute `vagrant ssh`

(note que agora você tá dentro de vagrant@sd)

- Execute `mkdir /vagrant/web-folder/p1`
- Execute `django-admin startproject projeto1 /vagrant/web-folder/p1`
- Execute `cd /vagrant/web-folder/p1`
- Execute `cp .env.example .env`
- Preencha o `.env`
- Execute `python manage.py runserver 0:8000`
- Acesse `192.168.56.101:8000`

*confira no VirtualBox ou executando `vagrant global-status`

## Pra fazer sempre que for usar

- Acesse o diretório do `Vagrantfile`
- Execute `vagrant up`
- Execute `vagrant ssh`

(note que agora você tá dentro de vagrant@sd)

- Execute `cd /vagrant/web-folder/p1/`
- Execute `python manage.py runserver 0:8000`
- Acesse `192.168.56.101:8000`