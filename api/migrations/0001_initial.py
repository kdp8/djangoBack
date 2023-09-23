# Generated by Django 4.2.5 on 2023-09-22 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.CharField(max_length=20)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.TextField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_year', models.TextField(blank=True, null=True)),
                ('rental_duration', models.PositiveIntegerField()),
                ('rental_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('length', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('replacement_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.CharField(blank=True, max_length=5, null=True)),
                ('special_features', models.CharField(blank=True, max_length=54, null=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'film',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmText',
            fields=[
                ('film_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'film_text',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'inventory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'language',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('payment_date', models.DateTimeField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('rental_id', models.AutoField(primary_key=True, serialize=False)),
                ('rental_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'rental',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('picture', models.TextField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.IntegerField()),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(blank=True, db_collation='utf8mb4_bin', max_length=40, null=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('actor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.actor')),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('film', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.film')),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_category',
                'managed': False,
            },
        ),
    ]
