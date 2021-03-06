# Generated by Django 3.0.8 on 2020-07-02 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('papel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data_compra', models.DateField()),
                ('preco_unitario', models.FloatField()),
                ('taxas', models.FloatField()),
                ('preco_total', models.FloatField()),
                ('codigo_acao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papel.Papel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
