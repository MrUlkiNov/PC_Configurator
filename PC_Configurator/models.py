from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.
class Processor(models.Model):
    A1 = 'AM4'
    A2 = 'AM3+'
    A3 = 'AM5'
    L1 = 'LGA 1151'
    L2 = 'LGA 1200'
    L3 = 'LGA 1700'
    L4 = 'LGA 2066'
    socket_choices = [
        (A1, 'AM4'),
        (A2, 'AM3+'),
        (A3, 'AM5'),
        (L1, 'LGA 1151'),
        (L2, 'LGA 1200'),
        (L3, 'LGA 1700'),
        (L4, 'LGA 2066')

    ]
    D3 = 'DDR3'
    D4 = 'DDR4'
    D5 = 'DDR5'
    RAM_choices = [
        (D3, 'DDR3'),
        (D4, 'DDR4'),
        (D5, 'DDR5')
    ]

    Name = models.CharField(max_length=40, verbose_name='Наименование')
    Socket = models.CharField(max_length=8, choices=socket_choices, default=L1, verbose_name='Сокет')
    Frequency = models.CharField(max_length=10, verbose_name='Частота')
    Cores = models.IntegerField(verbose_name='Ядра')
    Memory_type = models.CharField(max_length=4, choices=RAM_choices, verbose_name='Тип памяти')
    Max_RAM_frequency = models.IntegerField(verbose_name='Максимальная частота оперативки')
    Graphics_core = models.CharField(max_length=40, default="Не имеется", blank=True, verbose_name='Графическое ядро')
    Heat_dissipation = models.IntegerField(verbose_name='Теплоотдача')
    Photo = models.ImageField(upload_to='media/')
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

    def __str__(self):
        return f"[{self.Socket}, {self.Cores} x {self.Frequency} ГГц," \
               f" {self.Memory_type}-{self.Max_RAM_frequency} Мгц, {self.Graphics_core}, TDP {self.Heat_dissipation} Вт]"

    def get_url(self):
        return reverse('processor_url', args=[self.Name])


class add_processor(models.Model):
    Name = models.CharField(max_length=50)
    Socket = models.CharField(max_length=8, verbose_name='Сокет', blank=True, null=True)
    Memory_type = models.CharField(max_length=4, blank=True, null=True, verbose_name='Тип памяти')
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)


class Motherboard(models.Model):
    A1 = 'AM4'
    A2 = 'AM3+'
    A3 = 'AM5'
    L1 = 'LGA 1151'
    L2 = 'LGA 1200'
    L3 = 'LGA 1700'
    L4 = 'LGA 2066'
    socket_choices = [
        (A1, 'AM4'),
        (A2, 'AM3+'),
        (A3, 'AM5'),
        (L1, 'LGA 1151'),
        (L2, 'LGA 1200'),
        (L3, 'LGA 1700'),
        (L4, 'LGA 2066')
    ]
    D3 = 'DDR3'
    D4 = 'DDR4'
    D5 = 'DDR5'
    RAM_choices = [
        (D3, 'DDR3'),
        (D4, 'DDR4'),
        (D5, 'DDR5')
    ]

    Name = models.CharField(max_length=40, verbose_name='Наименование')
    Socket = models.CharField(max_length=8, choices=socket_choices, default=L1, verbose_name='Сокет')
    Chipset = models.CharField(max_length=20, verbose_name='Чипсет')
    Memory_type = models.CharField(max_length=4, choices=RAM_choices, verbose_name='Тип памяти')
    Max_RAM_frequency = models.IntegerField(verbose_name='Максимальная частота оперативки')
    PCI_slot = models.CharField(max_length=10, default='PCI-Ex16', verbose_name='Слоты PCI')
    Size = models.CharField(max_length=15, verbose_name='Размер')
    Photo = models.ImageField(upload_to='media/')
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Материская плата'
        verbose_name_plural = 'Материнские платы'

    def __str__(self):
        return f"[{self.Socket}, {self.Chipset}, {self.Memory_type}-{self.Max_RAM_frequency} Мгц, {self.PCI_slot}, {self.Size}]"

    def get_url(self):
        return reverse('motherboard_url', args=[self.Name])


class add_motherboard(models.Model):
    Name = models.CharField(max_length=50)
    Socket = models.CharField(max_length=8, verbose_name='Сокет', blank=True, null=True)
    Memory_type = models.CharField(max_length=4, blank=True, null=True, verbose_name='Тип памяти')
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    PCI_slot = models.CharField(max_length=10, default='PCI-Ex16', verbose_name='Слоты PCI')
    Size = models.CharField(max_length=15, verbose_name='Размер')


class Videocard(models.Model):
    Name = models.CharField(max_length=100, verbose_name='Наименование')
    Memory = models.IntegerField(verbose_name='Количество памяти')
    Type_memory = models.CharField(verbose_name='Тип памяти', max_length=10)
    Connectors = models.TextField(verbose_name='Видеоразъемы')
    PCI_slot = models.CharField(max_length=10, default='PCI-Ex16', verbose_name='Слоты PCI')
    Bit = models.IntegerField(verbose_name='Разрядность')
    Video_frequency = models.IntegerField(verbose_name='Частота работы видеочипа')
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'

    def __str__(self):
        return f"[{self.PCI_slot} {self.Memory}ГБ {self.Type_memory}, {self.Bit} бит, {self.Connectors} GPU {self.Video_frequency} МГц]"

    def get_url(self):
        return reverse('videocard_url', args=[self.Name])


class add_videocard(models.Model):
    Name = models.CharField(max_length=50)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    PCI_slot = models.CharField(max_length=10, default='PCI-Ex16', verbose_name='Слоты PCI')


class RAM(models.Model):
    D3 = 'DDR3'
    D4 = 'DDR4'
    D5 = 'DDR5'
    RAM_choices = [
        (D3, 'DDR3'),
        (D4, 'DDR4'),
        (D5, 'DDR5')
    ]
    Name = models.CharField(max_length=100)
    Memory_type = models.CharField(max_length=4, blank=True, null=True, verbose_name='Тип памяти', choices=RAM_choices)
    Memory = models.IntegerField(verbose_name='Количество памяти')
    Max_frequency = models.IntegerField(verbose_name='Частота')
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'

    def __str__(self):
        return f"[{self.Memory_type}, {self.Memory}ГБх1шт, {self.Max_frequency}Мгц]"

    def get_url(self):
        return reverse('ram_url', args=[self.Name])


class add_RAM(models.Model):
    Memory_type = models.CharField(max_length=4, blank=True, null=True, verbose_name='Тип памяти')
    Name = models.CharField(max_length=50)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)


class HDD(models.Model):
    Name = models.CharField(max_length=100)
    Interface = models.CharField(max_length=10, verbose_name='Интерфейс', default='SATA III')
    Bandwidth = models.IntegerField(verbose_name='Пропускная способность')
    Speed = models.IntegerField(verbose_name='Скорость оборотов')
    Cache = models.IntegerField(verbose_name='Кэш память')
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Жесткий диск'
        verbose_name_plural = 'Жесткие диски'

    def __str__(self):
        return f"[{self.Interface}, {self.Bandwidth}ГБит/с, {self.Speed} об/мин, кэш память {self.Cache} МБ]"

    def get_url(self):
        return reverse('hdd_url', args=[self.Name])


class add_HDD(models.Model):
    Name = models.CharField(max_length=50)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)


class PowerBlock(models.Model):
    Name = models.CharField(max_length=100)
    Power = models.IntegerField(verbose_name='Мощность')
    Base_connector = models.CharField(max_length=15, verbose_name='Основной разъем питания', default='20 + 4 pin')
    Cpu_connector = models.IntegerField(verbose_name='Разъемы для питания процессора', default=4)
    Sata_coonector = models.IntegerField(verbose_name='Количество SATA разъемов', default=2)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'

    def __str__(self):
        return f"[{self.Power} Вт, {self.Base_connector}, {self.Cpu_connector} pin CPU, {self.Sata_coonector} SATA ]"

    def get_url(self):
        return reverse('powerblock_url', args=[self.Name])


class add_PowerBlock(models.Model):
    Name = models.CharField(max_length=50)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)


class Cooler(models.Model):
    Name = models.CharField(max_length=100)
    Material = models.CharField(max_length=50, verbose_name='Материал')
    Speed = models.IntegerField(verbose_name='Кол-во оборотов')
    Power = models.IntegerField(verbose_name='Мощность')
    Connector = models.IntegerField(verbose_name='Разъем подключения')
    Noise = models.IntegerField(verbose_name='Уровень шума')
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Кулер'
        verbose_name_plural = 'Кулеры'

    def __str__(self):
        return f"[Основание - {self.Material}, {self.Speed} об/мин, {self.Noise} дБ, {self.Connector} pin, {self.Power} Вт]"

    def get_url(self):
        return reverse('cooler_url', args=[self.Name])


class add_Cooler(models.Model):
    Name = models.CharField(max_length=50)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)


class Case(models.Model):
    Name = models.CharField(max_length=100)
    Form = models.CharField(max_length=20, default='Micro-ATX', verbose_name='Максимальный форм фактор')
    USB = models.CharField(max_length=50, default='USB 2.0 Type-A', verbose_name='Юсб')
    Color = models.CharField(max_length=20, verbose_name='Цвет', default='Черный')
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ('Name',)
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'

    def __str__(self):
        return f"[{self.Form}, цвет {self.Color}, {self.USB}]"

    def get_url(self):
        return reverse('case_url', args=[self.Name])


class add_Case(models.Model):
    Name = models.CharField(max_length=50)
    Form = models.CharField(max_length=20, default='Micro-ATX', verbose_name='Максимальный форм фактор')
    Photo = models.ImageField(upload_to='media/', blank=True, null=True)
    Price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=10, blank=True, null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    components = models.TextField()
    total_price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class UserConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    processors = models.ManyToManyField('Processor')
    motherboards = models.ManyToManyField('Motherboard')
    hdds = models.ManyToManyField('HDD')
    coolers = models.ManyToManyField('Cooler')
    poweblocks = models.ManyToManyField('PowerBlock')
    rams = models.ManyToManyField('RAM')
    videocards = models.ManyToManyField('Videocard')
    cases = models.ManyToManyField('Case')

    # Добавьте остальные компоненты по аналогии

    def clear_config(self):
        self.processors.clear()
        self.motherboards.clear()
        self.hdds.clear()
        # Очистка всех компонентов
