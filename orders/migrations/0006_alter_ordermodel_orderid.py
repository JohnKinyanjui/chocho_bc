# Generated by Django 3.2.4 on 2021-07-02 02:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_ordermodel_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='orderId',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('b3fedc52-6d90-4ffa-aa33-1e0aacdb2150'), unique=True),
        ),
    ]
