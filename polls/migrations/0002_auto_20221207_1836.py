# Generated by Django 3.2 on 2022-12-08 00:36

from django.db import migrations, models
import django.db.models.deletion


def add_initial_tags(apps, schema_editor):
    ChoiceTag = apps.get_model('polls', 'ChoiceTag')
    ChoiceTag.objects.create(tag="Tag 1")
    ChoiceTag.objects.create(tag="Tag 2")
    ChoiceTag.objects.create(tag="Tag 3")
    ChoiceTag.objects.create(tag="Tag 4")
    ChoiceTag.objects.create(tag="Tag 5")


class Migration(migrations.Migration):
    """ Clase generada con 'django makemigrations' -> migrate"""
    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=60, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Opción', 'verbose_name_plural': 'Opciones'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Pregunta', 'verbose_name_plural': 'Preguntas'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='texto'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='votos'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='titulo'),
        ),
        migrations.AddField(
            model_name='choice',
            name='tag',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.choicetag'),
        ),
        migrations.RunPython(add_initial_tags)
    ]
