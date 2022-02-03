# Generated by Django 4.0.2 on 2022-02-03 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('serial_number', models.CharField(max_length=50, verbose_name='SerialNumber')),
                ('RFID_tag_id', models.CharField(max_length=50, verbose_name='RFID_tag_id')),
                ('default_locale', models.CharField(max_length=50, verbose_name='default_locale')),
                ('current_locale', models.CharField(max_length=50, verbose_name='current_locale')),
                ('status', models.BooleanField(verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='Bateria',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='Cabo',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='Extensao',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='LiveU',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='Microfone',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='Pilha',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
        migrations.CreateModel(
            name='SunGun',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.equipamento')),
            ],
            bases=('core.equipamento',),
        ),
    ]