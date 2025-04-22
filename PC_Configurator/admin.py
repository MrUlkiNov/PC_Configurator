from django.contrib import admin
from .models import Processor, Motherboard, Videocard, RAM, HDD, PowerBlock, Cooler, Case
from django.utils.safestring import mark_safe


class PriceFilter(admin.SimpleListFilter):
    title = 'Фильтр по цене'
    parameter_name = 'Price'

    def lookups(self, request, model_admin):
        return [
            ('<5000', 'Бюджетные'),
            ('от 10000 до 20000', 'Средний бюджет'),
            ('>30000', 'Элитные'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<5000':
            return queryset.filter(Price__lt=5000)
        if self.value() == 'от 10000 до 20000':
            return queryset.filter(Price__gte=10000).filter(Price__lt=20000)
        if self.value() == '>30000':
            return queryset.filter(Price__gt=30000)
        return queryset


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Socket', 'Frequency', 'Cores', 'Memory_type', 'Max_RAM_frequency', 'Graphics_core',
                    'Heat_dissipation', 'image_show', 'Price']
    list_filter = [PriceFilter]
    ordering = ['Price']

    def image_show(self, obj):
        if obj.Photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.Photo.url))
        return 'None'

    image_show.__name__ = 'Картинка'


@admin.register(Motherboard)
class MotherboardAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Socket', 'Chipset', 'Memory_type', 'Max_RAM_frequency', 'PCI_slot', 'Size', 'image_show']
    ordering = ['Price']

    def image_show(self, obj):
        if obj.Photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.Photo.url))
        return 'None'

    image_show.__name__ = 'Картинка'


@admin.register(Videocard)
class VideocardAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Memory', 'Type_memory', 'Connectors', 'PCI_slot', 'Bit', 'Video_frequency', 'image_show']
    ordering = ['Price']

    def image_show(self, obj):
        if obj.Photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.Photo.url))
        return 'None'

    image_show.__name__ = 'Картинка'


@admin.register(RAM)
class RamAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Memory', 'Memory_type', 'Max_frequency', 'image_show']
    ordering = ['Price']

    def image_show(self, obj):
        if obj.Photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.Photo.url))
        return 'None'

    image_show.__name__ = 'Картинка'


@admin.register(HDD)
class HddAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Interface', 'Speed', 'Cache', 'Bandwidth', 'image_show', 'Price']
    ordering = ['Price']

    def image_show(self, obj):
        if obj.Photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.Photo.url))
        return 'None'

    image_show.__name__ = 'Картинка'


@admin.register(PowerBlock)
class PowerBlockAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Power', 'Base_connector', 'Cpu_connector', 'Sata_coonector', 'image_show']
    ordering = ['Price']

    def image_show(self, obj):
        if obj.Photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.Photo.url))
        return 'None'

    image_show.__name__ = 'Картинка'


@admin.register(Cooler)
class CoolerAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Material', 'Speed', 'Noise', 'Connector', 'Power', 'image_show']
    ordering = ['Price']

    def image_show(self, obj):
        if obj.Photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.Photo.url))
        return 'None'

    image_show.__name__ = 'Картинка'


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Form', 'USB', 'Color', 'image_show']
    ordering = ['Price']

    def image_show(self, obj):
        if obj.Photo:
            return mark_safe("<img src='{}' width='60' />".format(obj.Photo.url))
        return 'None'

    image_show.__name__ = 'Картинка'
