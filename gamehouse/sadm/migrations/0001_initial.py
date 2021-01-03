# Generated by Django 3.1.4 on 2020-12-31 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sjug', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('usuario', models.OneToOneField(db_column='id_administrador', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sjug.usuario', verbose_name='Identificador del administrador')),
                ('nombre', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MatrizJuegos',
            fields=[
                ('juego', models.OneToOneField(db_column='id_juego', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sjug.juego', verbose_name='Identificador del juego')),
                ('vector_genero', models.CharField(max_length=256)),
                ('vector_plataforma', models.CharField(max_length=256)),
                ('vector_cpu', models.CharField(max_length=256)),
                ('vector_cde', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tf_Idf',
            fields=[
                ('juego', models.OneToOneField(db_column='juego', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sjug.juego', verbose_name='Juego del vector tf-idf')),
                ('vector', models.FilePathField(path='/home/mimr/azulR/var/analitycs/')),
            ],
        ),
    ]