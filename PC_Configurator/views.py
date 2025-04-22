from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Processor, Motherboard, Videocard, RAM, HDD, PowerBlock, Cooler, Case, UserConfig
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import OrderForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Order, add_processor, add_motherboard, add_videocard, add_RAM, add_HDD, add_PowerBlock, add_Cooler, \
    add_Case
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    p2 = add_processor.objects.all()
    m2 = add_motherboard.objects.all()
    v2 = add_videocard.objects.all()
    r2 = add_RAM.objects.all()
    h2 = add_HDD.objects.all()
    po2 = add_PowerBlock.objects.all()
    co2 = add_Cooler.objects.all()
    ca2 = add_Case.objects.all()
    if request.method == 'POST':
        processor_id = request.POST.get('processor_id')
        add_processor.objects.filter(id=processor_id).delete()
    if request.method == 'POST':
        motherboard_id = request.POST.get('motherboard_id')
        add_motherboard.objects.filter(id=motherboard_id).delete()
    if request.method == 'POST':
        videocard_id = request.POST.get('videocard_id')
        add_videocard.objects.filter(id=videocard_id).delete()
    if request.method == 'POST':
        RAM_id = request.POST.get('RAM_id')
        add_RAM.objects.filter(id=RAM_id).delete()
    if request.method == 'POST':
        HDD_id = request.POST.get('HDD_id')
        add_HDD.objects.filter(id=HDD_id).delete()
    if request.method == 'POST':
        powerblock_id = request.POST.get('powerblock_id')
        add_PowerBlock.objects.filter(id=powerblock_id).delete()
    if request.method == 'POST':
        cooler_id = request.POST.get('cooler_id')
        add_Cooler.objects.filter(id=cooler_id).delete()
    if request.method == 'POST':
        case_id = request.POST.get('case_id')
        add_Case.objects.filter(id=case_id).delete()
    return render(request, 'PC_Configurator/Configurator.html', {
        'product1': p2,
        'product2': m2,
        'product3': v2,
        'product4': r2,
        'product5': h2,
        'product6': po2,
        'product7': co2,
        'product8': ca2
    })


def show_processors(request):
    p = Processor.objects.order_by('Price')
    if request.method == 'POST':
        processor_id = request.POST.get('processor_id')
        config = get_user_config(request.user)
        selected_processor = Processor.objects.get(id=processor_id)
        add_processor.objects.create(Name=selected_processor.Name, Socket=selected_processor.Socket,
                                     Memory_type=selected_processor.Memory_type, Photo=selected_processor.Photo,
                                     Price=selected_processor.Price)
        config.processors.clear()
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Processors.html', {
        'processors': p
    })


def show_one_processor(request, name_processor: str):
    processor = get_object_or_404(Processor, Name=name_processor)
    if request.method == 'POST':
        add_processor.objects.create(
            Name=processor.Name,
            Photo=processor.Photo,
            Price=processor.Price
        )
        return redirect(reverse('configurator'))

    return render(request, 'PC_Configurator/One_processor.html', {'processor': processor})


def show_motherboards(request):
    m = Motherboard.objects.order_by('Price')
    if request.method == 'POST':
        motherboard_id = request.POST.get('motherboard_id')
        selected_motherboard = Motherboard.objects.get(id=motherboard_id)
        add_motherboard.objects.create(Name=selected_motherboard.Name, Socket=selected_motherboard.Socket,
                                       Memory_type=selected_motherboard.Memory_type, Photo=selected_motherboard.Photo,
                                       Price=selected_motherboard.Price, Size=selected_motherboard.Size,
                                       PCI_slot=selected_motherboard.PCI_slot)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Motherboards.html', {
        'motherboards': m
    })


def show_one_motherboard(request, name_motherboard: str):
    motherboard = get_object_or_404(Motherboard, Name=name_motherboard)
    if request.method == 'POST':
        add_motherboard.objects.create(
            Name=motherboard.Name,
            Photo=motherboard.Photo,
            Price=motherboard.Price
        )
        return redirect(reverse('configurator'))
    return render(request, 'PC_Configurator/One_motherboard.html', {
        'motherboard': motherboard
    })


def show_videocards(request):
    v = Videocard.objects.order_by('Price')
    if request.method == 'POST':
        videocard_id = request.POST.get('videocard_id')
        selected_videocard = Videocard.objects.get(id=videocard_id)
        add_videocard.objects.create(Name=selected_videocard.Name, PCI_slot=selected_videocard.PCI_slot,
                                     Photo=selected_videocard.Photo,
                                     Price=selected_videocard.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Videocards.html', {
        'videocards': v
    })


def show_one_videocard(request, name_videocard: str):
    videocard = get_object_or_404(Videocard, Name=name_videocard)
    if request.method == 'POST':
        add_videocard.objects.create(
            Name=videocard.Name,
            Photo=videocard.Photo,
            Price=videocard.Price
        )
        return redirect(reverse('configurator'))

    return render(request, 'PC_Configurator/One_videocard.html', {'videocard': videocard})


def show_RAMS(request):
    r = RAM.objects.order_by('Price')
    if request.method == 'POST':
        RAM_id = request.POST.get('RAM_id')
        selected_RAM = RAM.objects.get(id=RAM_id)
        add_RAM.objects.create(Name=selected_RAM.Name, Memory_type=selected_RAM.Memory_type, Photo=selected_RAM.Photo,
                               Price=selected_RAM.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/RAMS.html', {
        'RAMS': r
    })


def show_one_RAM(request, name_ram: str):
    ram = get_object_or_404(RAM, Name=name_ram)
    if request.method == 'POST':
        add_RAM.objects.create(
            Name=ram.Name,
            Photo=ram.Photo,
            Price=ram.Price
        )
        return redirect(reverse('configurator'))

    return render(request, 'PC_Configurator/One_ram.html', {'ram': ram})


def show_HDD(request):
    h = HDD.objects.order_by('Price')
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f'/login/?next={request.path}')
        HDD_id = request.POST.get('hdd_id')
        selected_HDD = HDD.objects.get(id=HDD_id)
        add_HDD.objects.create(Name=selected_HDD.Name, Photo=selected_HDD.Photo, Price=selected_HDD.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/HDD.html', {
        'HDDS': h
    })


def show_one_HDD(request, name_hdd: str):
    hdd = get_object_or_404(HDD, Name=name_hdd)
    if request.method == 'POST':
        add_HDD.objects.create(
            Name=hdd.Name,
            Photo=hdd.Photo,
            Price=hdd.Price
        )
        return redirect(reverse('configurator'))

    return render(request, 'PC_Configurator/One_hdd.html', {'hdd': hdd})


def show_powerblocks(request):
    po = PowerBlock.objects.order_by('Price')
    if request.method == 'POST':
        powerblock_id = request.POST.get('powerblock_id')
        selected_powerblock = PowerBlock.objects.get(id=powerblock_id)
        add_PowerBlock.objects.create(Name=selected_powerblock.Name, Photo=selected_powerblock.Photo,
                                      Price=selected_powerblock.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Powerblocks.html', {
        'pows': po
    })


def show_one_powerblock(request, name_powerblock: str):
    pow = get_object_or_404(PowerBlock, Name=name_powerblock)
    if request.method == 'POST':
        add_PowerBlock.objects.create(
            Name=pow.Name,
            Photo=pow.Photo,
            Price=pow.Price
        )
        return redirect(reverse('configurator'))
    return render(request, 'PC_Configurator/One_powerblock.html', {
        'pow': pow
    })


def show_coolers(request):
    co = Cooler.objects.order_by('Price')
    if request.method == 'POST':
        cooler_id = request.POST.get('cooler_id')
        selected_cooler = Cooler.objects.get(id=cooler_id)
        add_Cooler.objects.create(Name=selected_cooler.Name, Photo=selected_cooler.Photo, Price=selected_cooler.Price)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Coolers.html', {
        'coolers': co
    })


def show_one_cooler(request, name_cooler: str):
    cooler = get_object_or_404(Cooler, Name=name_cooler)
    if request.method == 'POST':
        add_Cooler.objects.create(
            Name=cooler.Name,
            Photo=cooler.Photo,
            Price=cooler.Price
        )
        return redirect(reverse('configurator'))
    return render(request, 'PC_Configurator/One_cooler.html', {
        'cooler': cooler
    })


def show_cases(request):
    Ca = Case.objects.order_by('Price')
    if request.method == 'POST':
        case_id = request.POST.get('case_id')
        selected_case = Case.objects.get(id=case_id)
        add_Case.objects.create(Name=selected_case.Name, Photo=selected_case.Photo, Price=selected_case.Price,
                                Form=selected_case.Form)
        return HttpResponseRedirect('Configurator')
    return render(request, 'PC_Configurator/Cases.html', {
        'cases': Ca
    })


def show_one_case(request, name_case: str):
    case = get_object_or_404(Case, Name=name_case)
    if request.method == 'POST':
        add_Case.objects.create(
            Name=case.Name,
            Photo=case.Photo,
            Price=case.Price
        )
        return redirect(reverse('configurator'))
    return render(request, 'PC_Configurator/One_case.html', {
        'case': case
    })


# Регистрация
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('configurator')
    else:
        form = CustomUserCreationForm()
    return render(request, 'PC_Configurator/auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.GET.get('next', 'configurator'))
    else:
        form = CustomAuthenticationForm()
    return render(request, 'PC_Configurator/auth/login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        config = get_user_config(request.user)
        config.clear_config()
    logout(request)
    return redirect('configurator')


def get_user_config(user):
    config, created = UserConfig.objects.get_or_create(user=user)
    return config


@login_required
def order_created(request):
    components_count = (
            add_processor.objects.count() +
            add_motherboard.objects.count() +
            add_videocard.objects.count() +
            add_RAM.objects.count() +
            add_HDD.objects.count() +
            add_PowerBlock.objects.count() +
            add_Cooler.objects.count() +
            add_Case.objects.count()
    )

    if components_count < 8:
        return redirect('configurator')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            components = []
            total_price = 0
            for proc in add_processor.objects.all():
                components.append(f"Процессор: {proc.Name} - {proc.Price}₽")
                total_price += proc.Price

            for mb in add_motherboard.objects.all():
                components.append(f"Материнская плата: {mb.Name} - {mb.Price}₽")
                total_price += mb.Price

            for cl in add_Cooler.objects.all():
                components.append(f"Кулер: {cl.Name} - {cl.Price}₽")
                total_price += cl.Price

            for pb in add_PowerBlock.objects.all():
                components.append(f"Блок питания: {pb.Name} - {pb.Price}₽")
                total_price += pb.Price

            for hd in add_HDD.objects.all():
                components.append(f"Жесткий диск: {hd.Name} - {hd.Price}₽")
                total_price += hd.Price

            for rm in add_RAM.objects.all():
                components.append(f"Оперативная память: {rm.Name} - {rm.Price}₽")
                total_price += rm.Price

            for vc in add_videocard.objects.all():
                components.append(f"Видеокарта: {vc.Name} - {vc.Price}₽")
                total_price += vc.Price

            for cs in add_Case.objects.all():
                components.append(f"Корпус: {cs.Name} - {cs.Price}₽")
                total_price += cs.Price

            order = Order(
                user=request.user,
                components="\n".join(components),
                total_price=total_price,
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
            )
            order.save()
            add_processor.objects.all().delete()
            add_motherboard.objects.all().delete()
            add_Cooler.objects.all().delete()
            add_HDD.objects.all().delete()
            add_RAM.objects.all().delete()
            add_videocard.objects.all().delete()
            add_Case.objects.all().delete()
            add_PowerBlock.objects.all().delete()

            return render(request, 'PC_Configurator/order_success.html', {
                'order': order,
                'total_price': total_price
            })

    else:
        form = OrderForm()

    return render(request, 'PC_Configurator/order_create.html', {'form': form})
