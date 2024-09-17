from myapp.forms import BookingForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


# Create your views here.


def home(request):
    return render(request, "index.html")


def drinks(request, drink_name):
    drinks = {'mocha': 'type of coffee', 'tea': 'type of beverage',
              'lemonade': 'type of refreshment'}
    choice_of_drink = drinks[drink_name]

    return HttpResponse(f"<h2> {drink_name} </h2> {choice_of_drink}")


def menu(request):
    menu_data = models.Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", main_data)


def display_menu_item(request, pk=None):
    if pk:
        menu_item = models.Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}

    # variable_name = {'key_accessed_in_form': "content"}
    return render(request, "about.html")


def book(request):

    if request.method == 'POST':
        # if the form is submitted, it creates a POST Request
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('book')

    form = BookingForm()
    context = {"form": form}
    return render(request, "book.html", context)
