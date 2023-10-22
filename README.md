# DOCUMENTAÇÃO (deixar mais bonitinha depois)

## Pra fazer só uma vez

- instale o virtualbox
- descompacte o sd.zip fornecido
- acesse a pasta descompactada
- atualize ipAdrPrefix no Vagrantfile para "192.168.56.101"
- se já existir uma VM sd, execute vagrant destroy (tem comando do vagrant pra saber se ja tem ou precisa abrir o virtualbox?)
- acesse a pasta com o Vagrantfile
- vagrant up
- vagrant ssh

(note que agora você tá dentro de vagrant@sd)

- mkdir /vagrant/web-folder/p1
- django-admin startproject projeto1 /vagrant/web-folder/p1
- cd /vagrant/web-folder/p1
- cp .env.example .env
- preencha o .env
- python manage.py runserver 0:8000
- acesse 192.168.56.101:8000

## Pra fazer sempre que for usar

- acesse a pasta com o Vagrantfile
- vagrant up
- vagrant ssh
(note que agora você tá dentro de vagrant@sd)
- cd /vagrant/web-folder/p1/
- python manage.py runserver 0:8000
- acesse 192.168.56.101:8000