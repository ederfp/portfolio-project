from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField('Título', max_length=100)
    description = RichTextField('Descrição')
    technology = models.CharField('Tecnologias Utilizadas', max_length=200)
    image = models.ImageField('Imagem', upload_to='projects')
    link = models.URLField('Link do Projeto', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    icon = models.CharField('Ícone', max_length=50, help_text='Nome do ícone do Font Awesome')
    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    subject = models.CharField('Assunto', max_length=100)
    message = models.TextField('Mensagem')
    created_at = models.DateTimeField('Enviado em', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.name} - {self.subject}'