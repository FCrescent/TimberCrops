# Generated by Django 4.2.4 on 2023-08-21 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crops_optimizer', '0008_natstructcat_rename_resource_cat_resource_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='NatStruct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('days_to_grow', models.PositiveIntegerField()),
                ('days_between_harvest', models.PositiveIntegerField()),
                ('resource_cut_yield', models.PositiveIntegerField()),
                ('resource_harvest_yield', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nat_structs', to='crops_optimizer.natstructcat')),
                ('resource_cut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cut_nat_structs', to='crops_optimizer.resource')),
                ('resource_harvest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='harvest_nat_structs', to='crops_optimizer.resource')),
            ],
        ),
    ]
