#Django-Little-Printer-Menu

A simple Django app to create a weekly menu formatted for the BERG Cloud Little Printer.

This is a proof of concept toy for the family to prepare menus to stick on the kitchen notice board. Your mileage may vary.

![Screengrab](https://raw.github.com/davidjamesmoss/django-little-printer-menu/master/screengrab.png)
![Example Printout](https://raw.github.com/davidjamesmoss/django-little-printer-menu/master/example_printout.jpg)

##Features
- Multiple dishes per day.
- Title is configurable.


##Implementation notes
- Prepares HTML menu and POSTs it to the direct print interface.
- Images for the menu are provided in static, but are currently hard-coded to S3 so the app doesn’t have to be accessible to BERG’s servers.
- CSS for the menu is inline for the same reason.
- Printer key stored in DB, can be set from interface.
- No login or user auth - if you’re putting this on the open internet, stick it behind an HTTP basic auth at least.
- Interface is kind of responsive (uses Bootstrap 3), but not that useful on smaller screens.


##Requirements
- Django 1.5
- Requests
- Crispy Forms
- A BERG Cloud account and direct print key
- A Little Printer

##Installation
1. Install:

        pip install git+https://github.com/davidjamesmoss/django-little-printer-menu.git

2. In your settings.py (or equivalent), specify the bootstrap3 template for Crispy Forms and add to your installed apps:

        CRISPY_TEMPLATE_PACK = 'bootstrap3'

        INSTALLED_APPS = (
            ...
            'menu',
        )

3. Link into your URLs.py.

4. Run syncdb.

##First-time usage
1. Go to the URL you have set and click the cog icon. Enter your printer key (instructions for finding this are on the page).

2. Click ‘Dishes’ and add some meals.

3. Click ‘Create menu’ and select dishes or enter an alternative (eg. “Kitchen closed. Fend for yourselves.”) for each day of the week. A preview of the menu is shown at right.

4. Click ‘Print’ and within 10-20 seconds your Little Printer should spring into life.
