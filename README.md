# Portfólio Pessoal - Django

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2.7-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

Um site de portfólio profissional desenvolvido com Django, projetado para mostrar projetos, habilidades e experiências de forma elegante e responsiva.

## 📋 Características

- **Design Moderno e Responsivo**
  - Interface limpa e profissional
  - Totalmente responsivo para todos os dispositivos
  - Animações suaves com AOS (Animate On Scroll)
  - Design moderno com Bootstrap 5

- **Gerenciamento de Projetos**
  - Showcase de projetos com imagens
  - Descrições detalhadas com rich text
  - Categorização por tecnologias
  - Links para demonstrações

- **Seção de Habilidades**
  - Exibição visual de competências
  - Ícones personalizados
  - Níveis de proficiência
  - Descrições detalhadas

- **Sistema de Contato**
  - Formulário de contato funcional
  - Armazenamento de mensagens no admin
  - Validação de dados
  - Notificações de sucesso

## 🛠 Tecnologias Utilizadas

- **Backend**
  - Python 3.8+
  - Django 4.2.7
  - SQLite3
  - django-ckeditor

- **Frontend**
  - HTML5
  - CSS3
  - Bootstrap 5.3
  - JavaScript
  - Font Awesome
  - AOS (Animate On Scroll)

- **Ferramentas de Desenvolvimento**
  - Git
  - Visual Studio Code
  - Python Decouple
  - Pillow

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Git

### Passo a Passo

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/portfolio-project.git
cd portfolio-project
```

2. Crie um ambiente virtual
```bash
python -m venv venv_django
```

3. Ative o ambiente virtual

No Windows:
```powershell
.\venv_django\Scripts\activate
```

No Linux/Mac:
```bash
source venv_django/bin/activate
```

4. Instale as dependências
```bash
pip install -r requirements.txt
```

5. Execute as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crie um superusuário
```bash
python manage.py createsuperuser
```

7. Inicie o servidor
```bash
python manage.py runserver
```

8. Acesse o projeto
- Frontend: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 📁 Estrutura do Projeto

```
portfolio_project/
│
├── core/                   # Configurações principais do projeto
│   ├── settings.py        # Configurações do Django
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # Configuração WSGI
│
├── portfolio/             # Aplicativo principal
│   ├── models.py         # Modelos de dados
│   ├── views.py          # Views do aplicativo
│   ├── admin.py         # Configurações do admin
│   └── urls.py          # URLs do aplicativo
│
├── static/               # Arquivos estáticos
│   ├── css/             # Arquivos CSS
│   ├── js/              # Arquivos JavaScript
│   └── img/             # Imagens
│
├── templates/           # Templates HTML
│   ├── base.html       # Template base
│   └── portfolio/      # Templates do aplicativo
│
├── media/              # Arquivos enviados pelos usuários
│
├── requirements.txt    # Dependências do projeto
└── manage.py          # Script de gerenciamento Django
```

## 🎨 Personalização

1. **Cores e Estilos**
   - Edite `static/css/style.css` para personalizar cores e estilos
   - Modifique as variáveis CSS no início do arquivo

2. **Conteúdo**
   - Acesse o painel admin para adicionar/editar projetos
   - Atualize textos nos templates HTML
   - Personalize imagens na pasta static/img

3. **Templates**
   - Os templates estão em `templates/portfolio/`
   - Modifique-os para atender suas necessidades

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Seu Nome
- LinkedIn: [Seu LinkedIn](https://linkedin.com/in/seu-perfil)
- GitHub: [Seu GitHub](https://github.com/seu-usuario)

## 📫 Contato

- Email: seu.email@exemplo.com
- LinkedIn: [Seu LinkedIn](https://linkedin.com/in/seu-perfil)

## 🤝 Contribuição

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push da Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## ⭐ Agradecimentos

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [AOS](https://michalsnik.github.io/aos/)