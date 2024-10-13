# Generated by Django 5.1.1 on 2024-10-13 09:33

import django.db.models.deletion
import django_jalali.db.models
import mdeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('association_type', models.CharField(choices=[('p', 'پرورشی'), ('A', 'آموزشی'), ('f', 'فرهنگی')], default='پرورشی', max_length=100, verbose_name='نوع انجمن')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('goals', mdeditor.fields.MDTextField(verbose_name='اهداف')),
                ('social_media_link', models.URLField(blank=True, null=True, verbose_name='لینک شبکه اجتماعی')),
                ('site_link', models.URLField(blank=True, null=True, verbose_name='لینک وبسایت')),
                ('channel_link', models.URLField(blank=True, null=True, verbose_name='لینک کانال')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='ساخته شده در')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='ویرایش شده در')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('description', models.TextField(max_length=300, verbose_name='توضیحات کوتاه')),
                ('profile_image', models.ImageField(default='association/users/profiles/default.svg', upload_to='association/users/profiles', verbose_name='عکس پروفایل')),
                ('created_at', django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='ساخته شده در')),
                ('updated_at', django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='ویرایش شده در')),
            ],
        ),
        migrations.CreateModel(
            name='AssociationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='سمت')),
                ('association_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='association.association')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='association.user')),
            ],
            options={
                'unique_together': {('user_id', 'association_id')},
            },
        ),
        migrations.AddField(
            model_name='association',
            name='association_users',
            field=models.ManyToManyField(related_name='users', through='association.AssociationUser', to='association.user'),
        ),
    ]
