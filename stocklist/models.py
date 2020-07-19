from django.db import models

class ListModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='商品编号')
    goods_name = models.CharField(max_length=50, verbose_name='商品描述')
    onhand_stock = models.BigIntegerField(default=0, verbose_name='现有库存')
    can_order_stock = models.BigIntegerField(default=0, verbose_name='可订货库存')
    inspect_stock = models.BigIntegerField(default=0, verbose_name='待检库存')
    cross_stock = models.BigIntegerField(default=0, verbose_name='暂存库存')
    hold_stock = models.BigIntegerField(default=0, verbose_name='不可发库存')
    damage_stock = models.BigIntegerField(default=0, verbose_name='破损库存')
    pre_delivery_stock = models.BigIntegerField(default=0, verbose_name='预计到货库存')
    pre_load_stock = models.BigIntegerField(default=0, verbose_name='待卸货库存')
    pre_sort_stock = models.BigIntegerField(default=0, verbose_name='待清点库存')
    sort_stock = models.BigIntegerField(default=0, verbose_name='待上架库存')
    pick_stock = models.BigIntegerField(default=0, verbose_name='待拣货库存')
    picked_stock = models.BigIntegerField(default=0, verbose_name='待发货库存')
    back_order_stock = models.BigIntegerField(default=0, verbose_name='欠货库存')
    appid = models.CharField(max_length=50, verbose_name='用户匹配码')
    t_code = models.CharField(max_length=50)
    is_delete = models.BigIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
