# Generated by Django 2.2.9 on 2020-09-26 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('id_turma', models.AutoField(primary_key=True, serialize=False)),
                ('letra_turma', models.CharField(max_length=45)),
                ('Professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professores.Professor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
