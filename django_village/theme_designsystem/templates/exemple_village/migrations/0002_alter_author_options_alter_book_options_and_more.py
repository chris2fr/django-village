# Generated by Django 5.0.3 on 2024-04-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("example_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name": "Author"},
        ),
        migrations.AlterModelOptions(
            name="book",
            options={"verbose_name": "Book"},
        ),
        migrations.AlterModelOptions(
            name="genre",
            options={"verbose_name": "Genre"},
        ),
        migrations.AlterField(
            model_name="author",
            name="birth_date",
            field=models.DateField(blank=True, null=True, verbose_name="Birth date"),
        ),
        migrations.AlterField(
            model_name="author",
            name="first_name",
            field=models.CharField(max_length=250, verbose_name="First name"),
        ),
        migrations.AlterField(
            model_name="author",
            name="last_name",
            field=models.CharField(max_length=250, verbose_name="Last name"),
        ),
        migrations.AlterField(
            model_name="book",
            name="book_format",
            field=models.CharField(
                blank=True,
                choices=[("PAPER", "Paper"), ("NUM", "Digital")],
                default="",
                max_length=10,
                verbose_name="Format",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="number_of_pages",
            field=models.CharField(
                blank=True, default="", max_length=6, verbose_name="Number of pages"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=250, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="genre",
            name="designation",
            field=models.CharField(max_length=250, verbose_name="Designation"),
        ),
        migrations.AlterField(
            model_name="genre",
            name="help_text",
            field=models.CharField(
                blank=True, default="", max_length=250, verbose_name="Help text"
            ),
            preserve_default=False,
        ),
    ]
