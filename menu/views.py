import requests
from django.http import HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from collections import OrderedDict
from .models import Menu, Dish, Setup
from .forms import DishesForm, SetupForm
from .settings import PRINT_URL


def _build_menu(request):
    days = OrderedDict(Menu.day_choices)
    setup = Setup.values.get()

    for k, v in days.iteritems():
        days[k] = {'name': v, 'dishes': Menu.objects.filter(day=k)}

    return render_to_string(
        'menu/menu.html',
        {
            'request': request,
            'days': days,
            'menu_title': setup.menu_title,
        },
        context_instance=RequestContext(request)
    )


def create_menu(request, day):
    if not day:
        day = 'fri'
    menu = Menu.objects.filter(day=day)
    days = OrderedDict(Menu.day_choices)
    setup = Setup.values.get()
    dishes = Dish.objects.all()

    if request.method == 'POST':
        if request.POST.get('print', False):
            if setup.printer_key:
                url = '%s%s' % (PRINT_URL, setup.printer_key)
            else:
                messages.add_message(request, messages.ERROR,
                                     'You need to add your printer key first.')
                return HttpResponseRedirect(reverse('menu_setup'))

            r = requests.post(
                url,
                data={'html': _build_menu(request)}
            )
            if r.status_code == requests.codes.ok:
                messages.add_message(request, messages.SUCCESS,
                                     'Menu sent to Little Printer!')
            else:
                messages.add_message(request, messages.ERROR,
                                     'There was a problem printing the menu. \
                                      Check your printer URL.')
            return HttpResponseRedirect(reverse('menu_create',
                                                kwargs={'day': day}))

        remove = request.POST.get('remove', False)
        if remove:
            Menu.objects.filter(day=day, id=remove).delete()
            return HttpResponseRedirect(reverse('menu_create',
                                                kwargs={'day': day}))

        alternative = request.POST.get('alternative', False)
        dish = request.POST.get('dish', False)
        if dish:
            dish = Dish.objects.get(id=dish)

        m = Menu(
            day=day,
            alternative=alternative
        )

        if dish:
            m.dish = dish

        m.save()

        return HttpResponseRedirect(reverse('menu_create',
                                    kwargs={'day': day}))

    else:
        return render_to_response(
            'menu/create.html',
            {
                'request': request,
                'dishes': dishes,
                'menu': menu,
                'current_day_key': day,
                'current_day': days[day],
                'days': days,
            },
            context_instance=RequestContext(request)
        )


def setup(request):
    setup = Setup.values.get()

    if request.method == 'POST':
        form = SetupForm(request.POST, instance=setup)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Settings saved.')
            return HttpResponseRedirect(reverse('menu_setup'))
    else:
        form = SetupForm(instance=setup)

    return render_to_response(
        'menu/setup.html',
        {
            'request': request,
            'form': form,
        },
        context_instance=RequestContext(request)
    )


def dishes(request):
    dishes = Dish.objects.all()

    if request.method == 'POST':
        delete = request.POST.get('delete', False)
        if delete:
            Dish.objects.filter(id=delete).delete()
            messages.add_message(request, messages.SUCCESS, 'Dish deleted.')
            return HttpResponseRedirect(reverse('menu_dishes'))

        form = DishesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Dish added.')
            return HttpResponseRedirect(reverse('menu_dishes'))
    else:
        form = DishesForm()

    return render_to_response(
        'menu/dishes.html',
        {
            'request': request,
            'dishes': dishes,
            'form': form,
        },
        context_instance=RequestContext(request)
    )


def preview(request):
    return HttpResponse(_build_menu(request))
