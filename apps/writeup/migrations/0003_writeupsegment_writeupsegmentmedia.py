# Generated by Django 2.2.5 on 2022-04-10 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_auto_20220408_2305'),
        ('writeup', '0002_writeupmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteupSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.DecimalField(decimal_places=2, max_digits=3)),
                ('text', models.TextField(blank=True, null=True)),
                ('is_media', models.BooleanField(default=False)),
                ('writeup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writeup_segments', to='writeup.Writeup')),
            ],
        ),
        migrations.CreateModel(
            name='WriteupSegmentMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.DecimalField(decimal_places=2, max_digits=3)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writeup_segment_medias', to='media.Media')),
                ('writeup_segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writeup_segment_medias', to='writeup.WriteupSegment')),
            ],
        ),
    ]