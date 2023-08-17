# Generated by Django 4.2.3 on 2023-08-17 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="dept",
            fields=[
                ("DEPTNO", models.IntegerField(primary_key=True, serialize=False)),
                ("DNAME", models.CharField(max_length=100)),
                ("LOC", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="emp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("EMPNO", models.IntegerField()),
                ("ENAME", models.CharField(max_length=100)),
                ("JOB", models.CharField(max_length=100)),
                ("HIREDATE", models.DateField()),
                ("SAL", models.IntegerField()),
                ("COMM", models.IntegerField(default=None, null=2)),
                (
                    "DEPTNO",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.dept"
                    ),
                ),
            ],
        ),
    ]
