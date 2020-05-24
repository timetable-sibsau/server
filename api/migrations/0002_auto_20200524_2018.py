# Generated by Django 3.0.5 on 2020-05-24 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subgroup',
            field=models.ManyToManyField(to='api.Subgroup', verbose_name='Предметы'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time',
            field=models.CharField(max_length=11, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='department',
            field=models.TextField(blank=True, verbose_name='Кафедра'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.TextField(verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='phone',
            field=models.CharField(blank=True, max_length=12, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='groups',
            field=models.ManyToManyField(to='api.Group', verbose_name='Группы'),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='num',
            field=models.IntegerField(default=0, verbose_name='Подгруппа'),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Place', verbose_name='Аудитория'),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='professors',
            field=models.ManyToManyField(to='api.Professor', verbose_name='Преподаватели'),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Subject', verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Лекция'), (2, 'Лабораторная работа'), (3, 'Практика')], verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='timetablegroup',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='timetablegroup',
            name='even_week',
            field=models.BooleanField(verbose_name='Четная неделя'),
        ),
        migrations.AlterField(
            model_name='timetablegroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='timetablegroup',
            name='lesson',
            field=models.ManyToManyField(to='api.Lesson', verbose_name='Ленты'),
        ),
        migrations.AlterField(
            model_name='timetableplace',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='timetableplace',
            name='even_week',
            field=models.BooleanField(verbose_name='Четная неделя'),
        ),
        migrations.AlterField(
            model_name='timetableplace',
            name='lesson',
            field=models.ManyToManyField(to='api.Lesson', verbose_name='Ленты'),
        ),
        migrations.AlterField(
            model_name='timetableplace',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Place', verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='timetableprofessor',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='timetableprofessor',
            name='even_week',
            field=models.BooleanField(verbose_name='Четная неделя'),
        ),
        migrations.AlterField(
            model_name='timetableprofessor',
            name='lesson',
            field=models.ManyToManyField(to='api.Lesson', verbose_name='Ленты'),
        ),
    ]
