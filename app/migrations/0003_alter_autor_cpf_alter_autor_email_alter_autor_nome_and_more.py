# Generated by Django 5.1.3 on 2024-11-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_autor_cidade_alter_cidade_uf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='cpf',
            field=models.CharField(help_text='Informe o CPF', max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.CharField(help_text='Informe o e-mail', max_length=255, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(help_text='Informe o nome', max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='telefone',
            field=models.CharField(help_text='Informe o telefone', max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(help_text='Informe o nome da cidade', max_length=255, unique=True, verbose_name='Nome da Cidade'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='cnpj',
            field=models.CharField(help_text='Informe o CNPJ', max_length=14, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='email',
            field=models.CharField(help_text='Informe o e-mail', max_length=255, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='nome',
            field=models.CharField(help_text='Informe o nome', max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='razao_social',
            field=models.CharField(help_text='Informe a razão social', max_length=255, verbose_name='Razão Social'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='telefone',
            field=models.CharField(help_text='Informe o telefone', max_length=20, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='nome',
            field=models.CharField(help_text='Informe o nome do gênero literário', max_length=255, unique=True, verbose_name='Nome do Gênero'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='nome',
            field=models.CharField(help_text='Informe o nome do livro', max_length=255, verbose_name='Nome do Livro'),
        ),
        migrations.AlterField(
            model_name='uf',
            name='sigla',
            field=models.CharField(help_text='Informe a sigla da Unidade Federativa', max_length=2, unique=True, verbose_name='Sigla'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(help_text='Informe o CPF', max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(help_text='Informe o e-mail', max_length=255, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(help_text='Informe o nome', max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(help_text='Informe o telefone', max_length=20, verbose_name='Telefone'),
        ),
    ]