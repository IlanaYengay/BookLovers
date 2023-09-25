# Generated by Django 4.2.5 on 2023-09-24 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_author_birth_date'),
        ('userschats', '0003_message_book_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='book_shared',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
