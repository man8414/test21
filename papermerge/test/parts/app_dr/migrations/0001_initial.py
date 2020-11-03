# Generated by Django 3.1 on 2020-11-03 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0029_auto_20201023_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='app_dr_node_related', related_query_name='app_dr_nodes', to='core.basetreenode')),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='states', to='app_dr.policy')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
