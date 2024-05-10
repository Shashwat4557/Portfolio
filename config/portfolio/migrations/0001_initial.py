from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engname', models.CharField(max_length=25)),
                ('rusname', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('icon', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'Types of service',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('level', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='clients')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Service')),
            ],
            options={
                'verbose_name': 'A tool',
                'verbose_name_plural': 'Tools',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='author')),
                ('skills', models.ManyToManyField(related_name='author', to='portfolio.Skill')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'The author',
                'ordering': ['-id'],
            },
        ),
    ]
