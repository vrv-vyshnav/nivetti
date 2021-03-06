# Generated by Django 3.1 on 2020-09-16 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PASSIVE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpn', models.CharField(blank=True, max_length=150, null=True)),
                ('mfr', models.CharField(blank=True, max_length=150, null=True)),
                ('desc', models.CharField(blank=True, max_length=150, null=True)),
                ('pkg', models.CharField(blank=True, max_length=150, null=True)),
                ('ctype', models.CharField(choices=[('passive', 'passive')], max_length=150)),
                ('ptype', models.CharField(blank=True, max_length=150, null=True)),
                ('altmpn', models.CharField(blank=True, max_length=150, null=True)),
                ('altmfr', models.CharField(blank=True, max_length=150, null=True)),
                ('tol', models.CharField(blank=True, max_length=150, null=True)),
                ('rating', models.CharField(blank=True, max_length=150, null=True)),
                ('temp', models.CharField(blank=True, max_length=150, null=True)),
                ('values', models.CharField(blank=True, max_length=150, null=True)),
                ('pcb_footprint', models.CharField(blank=True, max_length=150, null=True)),
                ('symbol_id', models.CharField(blank=True, max_length=150, null=True)),
                ('detete', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ANALOG_POWER',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='CLOCK_TIMING',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='CONNECTOR',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='DISCRETE_ANALOG',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='ELECTRO_MECHANICAL',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='IC_CLASS_A',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='IC_MEMORY',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='IC_RF',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='IC_SENSOR',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='INTERFACE_LOGIC',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
        migrations.CreateModel(
            name='MECHANICAL',
            fields=[
                ('passive_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.passive')),
            ],
            bases=('library.passive',),
        ),
    ]
