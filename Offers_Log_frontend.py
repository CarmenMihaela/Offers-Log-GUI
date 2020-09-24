from tkinter import *
from tkinter.ttk import Frame

from Offers_Log_backend import Database

database = Database("entries.db")

def show_row_entries(event): # this row will be shown in the list at cursor selection
    clear_fields_buttonpress()
    for selected_row in list1.selection():
        e1.insert(END, str(list1.item(selected_row).get('values')[1]))
        e2.insert(END, str(list1.item(selected_row).get('values')[2]))
        e3.insert(END, str(list1.item(selected_row).get('values')[3]))
        quote_status_text.set(list1.item(selected_row).get('values')[4])
        e5.insert(END, str(list1.item(selected_row).get('values')[5]))
        e6.insert(END, str(list1.item(selected_row).get('values')[6]))
        e7.insert(END, str(list1.item(selected_row).get('values')[7]))
        t1.insert(END, str(list1.item(selected_row).get('values')[8]))

def view_command(): # this is the command for view button
    list1.delete(*list1.get_children())
    for row in database.view():
        list1.insert(parent = '', index = 'end', values = row)


def search_command(): # this is the command for search button
    list1.delete(*list1.get_children())

    # single field search:
    if len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search1(no_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search11(client_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search111(item_requested_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search1111(quote_status_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search11111(offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search111111(sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search1111111(cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)

    # 2 fields search:
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search2(no_text.get(), client_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search22(no_text.get(), item_requested_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search222(no_text.get(), quote_status_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search2222(no_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search22222(no_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search222222(no_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search2222222(client_text.get(), item_requested_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search22222222(client_text.get(), quote_status_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search222222222(client_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search2222222222(client_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search22222222222(client_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search222222222222(item_requested_text.get(), quote_status_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search2222222222222(item_requested_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search22222222222222(item_requested_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search222222222222222(item_requested_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search2222222222222222(quote_status_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search22222222222222222(quote_status_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search222222222222222222(quote_status_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search2222222222222222222(offer_manager_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search22222222222222222222(offer_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) != 0:
            for row in database.search222222222222222222222(sales_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)

    # 3 fields search:
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search3(no_text.get(), client_text.get(), item_requested_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search33(no_text.get(), client_text.get(), quote_status_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search333(no_text.get(), client_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search3333(no_text.get(), client_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search33333(no_text.get(), client_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search333333(no_text.get(), item_requested_text.get(), quote_status_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search3333333(no_text.get(), item_requested_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search33333333(no_text.get(), item_requested_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search333333333(no_text.get(), item_requested_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search3333333333(no_text.get(), quote_status_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search33333333333(no_text.get(), quote_status_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search333333333333(no_text.get(), quote_status_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search3333333333333(no_text.get(), offer_manager_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search33333333333333(no_text.get(), offer_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) != 0:
            for row in database.search333333333333333(no_text.get(), sales_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search3333333333333333(client_text.get(), item_requested_text.get(), quote_status_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search33333333333333333(client_text.get(), item_requested_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search333333333333333333(client_text.get(), item_requested_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search3333333333333333333(client_text.get(), item_requested_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search33333333333333333333(client_text.get(), quote_status_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search333333333333333333333(client_text.get(), quote_status_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search3333333333333333333333(client_text.get(), quote_status_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search33333333333333333333333(client_text.get(), offer_manager_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search333333333333333333333333(client_text.get(), offer_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) != 0:
            for row in database.search3333333333333333333333333(client_text.get(), sales_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search33333333333333333333333333(item_requested_text.get(),quote_status_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search333333333333333333333333333(item_requested_text.get(),quote_status_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search3333333333333333333333333333(item_requested_text.get(),quote_status_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search33333333333333333333333333333(quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search333333333333333333333333333333(quote_status_text.get(), offer_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) != 0:
            for row in database.search3333333333333333333333333333333(offer_manager_text.get(), sales_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)

    # 4 fields search:
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search4(no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search44(no_text.get(), client_text.get(), item_requested_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search444(no_text.get(), client_text.get(), item_requested_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() == "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search4444(no_text.get(), client_text.get(), item_requested_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search44444(client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search444444(client_text.get(), item_requested_text.get(), quote_status_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search4444444(client_text.get(), item_requested_text.get(), quote_status_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search44444444(item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search444444444(item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) == 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) != 0:
            for row in database.search4444444444(quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)

    # 5 fields search:
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) == 0:
            for row in database.search5(no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search55(no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) == 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search555(no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search5555(client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search55555(client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) == 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) != 0:
            for row in database.search555555(item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)

    # 6 fields search:
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) == 0:
            for row in database.search6(no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) == 0 and len(cost_meur_text.get()) != 0:
            for row in database.search66(no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)
    elif len(no_text.get()) == 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) != 0:
            for row in database.search666(client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)

    #7 fields search:
    elif len(no_text.get()) != 0 and len(client_text.get()) != 0 and len(item_requested_text.get()) != 0 and quote_status_text.get() != "Please select" and len(offer_manager_text.get()) != 0 and len(sales_manager_text.get()) != 0 and len(cost_meur_text.get()) != 0:
            for row in database.search7(no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get(), cost_meur_text.get()):
                list1.insert(parent = '', index = 'end', values = row)

def add_command(): # this is the command for add entry button
    database.insert(no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get(), cost_meur_text.get(), comments_text())
    list1.delete(*list1.get_children())
    list1.insert(parent = '', index = 'end', values = (no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get(), cost_meur_text.get(), comments_text()))
    clear_fields_buttonpress()
    view_command()

def no_blanks(): # so that the fields cannot be left blank, except for comments
    from tkinter import messagebox
    try: # makes sure the value entered in cost field is a number and not text
        check_val = int(float(cost_meur_text.get()))
        if not 0 <= check_val <= 99999999999999:
            messagebox.showinfo("Cost field is not a number",
                            "Please use a number in Cost field to be able to add your entry to the database")
            cost_meur_text.set("")
    except ValueError:
        cost_meur_text.set("") # makes the cost field none when we enter text
        messagebox.showinfo("Cost entered is not a number",
                            "Please use a number in Cost field to be able to add your entry to the database")

    if len(no_text.get()) == 0:
        messagebox.showinfo("No field not filled in", "Please fill in No field to be able to add your entry to the database")
    elif len(client_text.get()) == 0:
        messagebox.showinfo("Client field not filled in", "Please fill in Client field to be able to add your entry to the database")
    elif len(item_requested_text.get()) == 0:
        messagebox.showinfo("Item requested field not filled in", "Please fill in Item requested field to be able to add your entry to the database")
    elif quote_status_text.get() == "Please select":
        messagebox.showinfo("Quote status not chosen", "Please choose quote status to be able to add your entry to the database")
    elif len(offer_manager_text.get()) == 0:
        messagebox.showinfo("Offer manager name not filled in",
                            "Please fill in Offer manager name to be able to add your entry to the database")
    elif len(sales_manager_text.get()) == 0:
        messagebox.showinfo("Sales manager name not filled in",
                            "Please fill in Sales manager name to be able to add your entry to the database")
    elif len(cost_meur_text.get()) == 0:
        messagebox.showinfo("Cost field not filled in",
                            "Please fill in Cost field to be able to add your entry to the database")
    else:
        add_command()


def clear_fields_buttonpress():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    quote_status_text.set('Please select')
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    t1.delete('1.0', 'end')

def delete_command(): # this is the command for delete button
    for selected_row in list1.selection():
        deleted_row = str((list1.item(selected_row).get('values')[0]))
        database.delete(deleted_row)
        clear_fields_buttonpress()
        view_command()
# to get the row selected by cursor, item gives a dictionary in which id is the first character in a tuple
# database.delete needs a string

def update_command(): # this is the command for update button
    for selected_row in list1.selection():
        database.update(str((list1.item(selected_row).get('values')[0])), no_text.get(), client_text.get(), item_requested_text.get(), quote_status_text.get(), offer_manager_text.get(), sales_manager_text.get(), cost_meur_text.get(), comments_text())
        view_command()
        clear_fields_buttonpress()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Offers Log")

notebook = ttk.Notebook(root)
window = ttk.Frame(notebook)
frame2: Frame = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
notebook.add(window, text="Tool for entries")
notebook.add(frame2, text="How to use this tool")
notebook.add(frame3, text="Statistics derived from entries")
notebook.pack()

# Import the Notebook.tab element from the default theme
noteStyler = ttk.Style()
noteStyler.element_create('Plain.Notebook.tab', "from", 'default')
# Redefine the window Tab layout to use the new element
noteStyler.layout("window",
    [('Plain.Notebook.tab', {'children':
        [('Notebook.padding', {'side': 'top', 'children':
            [('Notebook.focus', {'side': 'top', 'children':
                [('Notebook.label', {'side': 'top', 'sticky': ''})],
            'sticky': 'nswe'})],
        'sticky': 'nswe'})],
    'sticky': 'nswe'})])
noteStyler.configure("window", background='#4682B4', borderwidth=0)
noteStyler.configure("window", background="green", foreground="white",
                                      lightcolor="white", borderwidth=2)
noteStyler.configure("TFrame", background='#4682B4', foreground="white", borderwidth=0)

#create all labels and buttons in tab1:
l0 = Label(window, text="Offers Log Regenboog 2020", font = "Calibri 20", fg = "white", bg = "#4682B4", pady = 10)
l0.grid(row=0, column=4, pady = 30)

l1 = Label(window, text="No", font = "Calibri 11", fg = "white", bg = "#4682B4", pady = 10)
l1.grid(row=1, column=0)

l2 = Label(window, text="Client", font="Calibri 11", fg="white", bg="#4682B4", pady=10)
l2.grid(row=1, column=2)

l3 = Label(window, text="Item requested", font="Calibri 11", fg="white", bg="#4682B4", pady=10, padx=30)
l3.grid(row=1, column=4)

l4 = Label(window, text="Quote status", font="Calibri 11", fg="white", bg="#4682B4", pady=10)
l4.grid(row=2, column=2)

l5 = Label(window, text="Offer manager", font="Calibri 11", fg="white", bg="#4682B4", pady=10)
l5.grid(row=2, column=4)

l6 = Label(window, text="Sales manager", font="Calibri 11", fg="white", bg="#4682B4", pady=10)
l6.grid(row=3, column=2)

l7 = Label(window, text="Cost (M€)", font="Calibri 11", fg="white", bg="#4682B4", pady=10)
l7.grid(row=3, column=4)

l8 = Label(window, text="Comments", font="Calibri 11", fg="white", bg="#4682B4", pady=10)
l8.grid(row=4, column=0, padx=20)

no_text = StringVar()
e1 = Entry(window, textvariable=no_text, bg="#DCDCDC", font="Calibri 10", width=5)
e1.grid(row=1, column=1)

client_text = StringVar()
e2 = Entry(window, textvariable=client_text, bg="#DCDCDC", font="Calibri 10")
e2.grid(row=1, column=3)

item_requested_text = StringVar()
e3 = Entry(window, textvariable=item_requested_text, bg="#DCDCDC", font="Calibri 10")
e3.grid(row=1, column=5)

quote_status_text = StringVar()
choices = ["in progress","pending approval","submitted to client","won","lost", "on hold"]
quote_status_text.set('Please select') # set the default option
e4 = OptionMenu(window, quote_status_text, *choices)
e4.config(bg="#DCDCDC", font="Calibri 10", width = 15)
e4.grid(row=2, column=3)

offer_manager_text = StringVar()
e5 = Entry(window, textvariable=offer_manager_text, bg="#DCDCDC", font="Calibri 10")
e5.grid(row=2, column=5, padx=10)

sales_manager_text = StringVar()
e6 = Entry(window, textvariable=sales_manager_text, bg="#DCDCDC", font="Calibri 10")
e6.grid(row=3, column=3)

cost_meur_text = StringVar()
e7 = Entry(window, textvariable=cost_meur_text, bg="#DCDCDC", font="Calibri 10", width=5, justify=RIGHT)
e7.grid(row=3, column=5, sticky=W, padx=27)

#comments are to be written in a text widget and not in an entry widget, so that it can be multiline.
#because it is a text widget, it does not have a textvariable option

t1 = Text(window, bg = "#DCDCDC", font = "Calibri 11", height = 2, wrap = WORD, width = 50)
t1.grid(row = 4, column = 1, columnspan = 3, pady = 15)

def comments_text(): # function created to retrieve text entry
    x = t1.get('1.0', 'end')
    return x

from tkinter import ttk

#style for column headers
style = ttk.Style()
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
            ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
            ("Custom.Treeheading.text", {'sticky':'we'})
        ]})
    ]}),
])
style.configure("Custom.Treeview.Heading",
    background="grey", foreground="white", relief="flat", font=("Calibri", 11))
style.map("Custom.Treeview.Heading",
    relief=[('active','groove'),('pressed','sunken')])

list1 = ttk.Treeview(window, style="Custom.Treeview", columns = ('id', 'no', 'client', 'item_requested', 'quote_status', 'offer_manager', 'sales_manager', 'cost_meur', 'comments'))
list1.column("#0", width = 50)
list1.column("id", width = 50)
list1.column("no", width = 50)
list1.column("client", width = 130)
list1.column("item_requested", width = 150)
list1.column("quote_status", width = 130)
list1.column("offer_manager", width = 130)
list1.column("sales_manager", width = 130)
list1.column("cost_meur", width = 100)
list1.column("comments", width = 350)
list1.grid(row = 6, column = 1, pady = 15, columnspan = 9, rowspan = 8, padx = 18)
list1.heading("id", text = 'Id')
list1.heading("no", text = 'No', anchor = W)
list1.heading("client", text = "Client", anchor = W)
list1.heading("item_requested", text = "Item requested", anchor = W)
list1.heading("quote_status", text = "Quote status", anchor = W)
list1.heading("offer_manager", text = "Offer mgr", anchor = W)
list1.heading("sales_manager", text = "Sales mgr", anchor = W)
list1.heading("cost_meur", text = "Cost (M€)", anchor = W)
list1.heading("comments", text = "Comments", anchor = W)
list1['show'] = 'headings'
list1["displaycolumns"]=("no", "client", "item_requested", "quote_status", "offer_manager", "sales_manager", "cost_meur", "comments")
list1.column("cost_meur")

sb1 = Scrollbar(window)
sb1.grid(row = 8, column = 9, sticky = NS, rowspan = 3)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<TreeviewSelect>>', show_row_entries)

b1 = Button(window, text="Add entry", width=10, font="Calibri 12", bg="#FFA500", fg="white", relief=GROOVE, command = no_blanks)
b1.grid(row=4, column=4)

b2 = Button(window, text="Search entry", width=10, font="Calibri 12", bg="#FFA500", fg="white", padx=10, relief=GROOVE, command = search_command)
b2.grid(row=4, column=5, sticky = W, padx = 15)

b2 = Button(window, text="Clear all fields", width=10, font="Calibri 12", bg="#FFA500", fg="white", padx=10, relief=GROOVE, command = clear_fields_buttonpress)
b2.grid(row=4, column=6, sticky = W)

b3 = Button(window, text="View all", width=15, font="Calibri 12", bg="#FFA500", fg="white", relief=GROOVE, command = view_command)
b3.grid(row=7, column=0)

b4 = Button(window, text="Update selected", width=15, font="Calibri 12", bg="#FFA500", fg="white", relief=GROOVE, command = update_command)
b4.grid(row=8, column=0, padx=20)

b5 = Button(window, text="Delete selected", width=15, font="Calibri 12", bg="#FFA500", fg="white", relief=GROOVE, command = delete_command)
b5.grid(row=9, column=0)

b6 = Button(window, text="Close", width=15, font="Calibri 12", bg="#FFA500", fg="white", relief=GROOVE, command = window.destroy)
b6.grid(row=14, column=4, pady=20)

# code for tab 2: User manual
i0 = Label(frame2, text="User manual \n Offers Log", font = "Calibri 15", fg = "white", bg = "#4682B4")
i0.grid(row=0, column=1)
i00 = Label(frame2, text="version 0.1 \n September 2020", font = "Calibri 10", fg = "white", bg = "#4682B4")
i00.grid(row=1, column=1, pady = 10)

t0 = Text(frame2, bg = "grey", font = "Calibri 11", foreground = "white", height = 25, width = 195, cursor = "arrow")
t0.grid(row = 2, column = 1)

sb2 = Scrollbar(frame2)
sb2.grid(row = 2, column = 2, sticky = NS, rowspan = 5)
t0.configure(yscrollcommand = sb2.set)
sb2.configure(command = t0.yview)

#inserting rows in text field:
t0.insert(1.0, "\n ")
t0.insert(2.0, "1. Open the first tab of the tool (it starts at the default Tool for entries tab):")
t0.insert(3.0, "\n ")
t0.insert(4.0, "\n ")

filelocation = r"C:\Users\carme\.PyCharmCE2019.2\config\scratches\dist" #r converts normal string to raw string
photo1=PhotoImage(file= filelocation + "\overall tool tab1.png")
t0.image_create(5.0, image=photo1)

t0.insert(6.0, "\n ")
t0.insert(7.0, "\n2. For adding a new entry, fill in the fields. No is the internal number we assign to each quote made. "
                " \n In the Quote status field, please choose by using the drop down list. "
                         " \n Make sure you use only numbers in Cost field."
                        "\n All fields are mandatory to be filled in, except for the comments one.")
t0.insert(11.0, "\n ")
t0.insert(12.0, "\n3. To display all entries in the database, press View all button. "
                       "\n When selecting a row from the database, it becomes editable in each field: "
                        "\n ")
t0.insert(13.0, "\n ")

photo2=PhotoImage(file= filelocation + "/view all button.png")
t0.image_create(15.0, image=photo2)

t0.insert(16.0, "\n ")

t0.insert(17.0, "\n4. To update an entry, select it in the viewing panel, make the necessary adjustments, and then press the Update button: "
          "\n ")

t0.insert(18.0, "\n ")

photo3=PhotoImage(file= filelocation + "/update button.png")
t0.image_create(19.0, image=photo3)
t0.insert(20.0, "\n ")

t0.insert(21.0, "\n5. To delete an entry, select it in the viewing panel and press the Delete button. "
                " \n This deletes the entry from the database and it is irreversible, so please double check before pressing the button. "
          "\n ")

t0.insert(23.0, "\n6. To clear all fields for a new entry or a search, use the Clear all button. "
                "\n ")

t0.insert(24.0, "\n ")

t0.insert(25.0, "\n7. Use the Search button to find entries specific entries. One or more search fields can be used, but the text"
                "\n has to be the same as the one in the database. "
                "\n ")

t0.insert(28.0, "\n ")

photo4=PhotoImage(file= filelocation +"\search button.png")
t0.image_create(30.0, image=photo4)
t0.insert(30.0, "\n ")

t0.insert(31.0, "\n8. To see the summary of all entries in the tool, go to Statistics tab, tab no 3."
                "\n This tab automatically updates each time the tool is opened. "
                "\n ")

t0.insert(33.0, "\n9. For further assistance please refer to: xxxxxxxx."
                "\n "
                "\n Thank you for using Offers Log! "
                "\n ")

t0.configure(state='disabled')

# code for tab 3, statistics derived from entries:
def total_no_of_entries():
    list1.delete(*list1.get_children())
    for row in database.view():
        list1.insert(parent = '', index = 'end', values = row)
        a = 0
    for each in list1.get_children():
        a = a+1
    return a

def total_value():
    list1.delete(*list1.get_children())
    b = []
    for row in database.view():
        list1.insert(parent = '', index = 'end', values = row)
        b.append(row[-2])
    for i in range (0, len(b)):
        b[i] = int(b[i])
        return sum(b)

def number_of_clients():
    list1.delete(*list1.get_children())
    c = []
    for row in database.view():
        list1.insert(parent = '', index = 'end', values = row)
        c.append(row[-7])
    return len(set(c)) # set removes duplicates

def quotes_per_client():
    list1.delete(*list1.get_children())
    c = []
    for row in database.view():
        list1.insert(parent='', index='end', values=row)
        c.append(row[-7])
    from collections import Counter # dict subclass for counting hashable objects
    q = Counter(c)
    return q

def quotes_per_item():
    list1.delete(*list1.get_children())
    q = []
    for row in database.view():
        list1.insert(parent='', index='end', values=row)
        q.append(row[-6])
    from collections import Counter
    qi = Counter(q)
    return qi

def amount_per_client():
    list1.delete(*list1.get_children())
    c = []
    for row in database.view():
        list1.insert(parent='', index='end', values=row)
        c.append(row[-7])
    for i in range(0, len(set(c))):
        res_dct = {}
        for client in set(c):
            amounts = database.amount_per_client(client)
            val = sum(list(map(sum, list(amounts))))
            res_dct.update({client:val})
    return res_dct

def amount_per_item():
    list1.delete(*list1.get_children())
    c = []
    for row in database.view():
        list1.insert(parent='', index='end', values=row)
        c.append(row[-6])
    for i in range(0, len(set(c))):
        res_dct = {}
        for item in set(c):
            amounts = database.amount_per_item(item)
            val = sum(list(map(sum, list(amounts))))
            res_dct.update({item:val})
    return res_dct

#creates the title:
title1 = Label(frame3, text=" Bird's eye view of data in \n Offers Log 2020", font = "Calibri 15", fg = "white", bg = "#4682B4", height = 3)
title1.grid(row=0, column=2, columnspan = 2, pady = 20)

# initial table in tab 3
list2 = ttk.Treeview(frame3, style="Custom.Treeview", columns = ('Total number of quotes', 'Total value', 'Total number of clients'), height = 1)
list2.column("#0", width = 50)
list2.column("Total number of quotes", width = 200, anchor='center')
list2.column("Total value", width = 200, anchor='center')
list2.column("Total number of clients", width = 200, anchor='center')
list2.grid(row = 1, column = 2, columnspan = 2)
list2.heading("Total number of quotes", text = 'Total number of quotes')
list2.heading("Total value", text = 'Total value (in M eur)')
list2.heading("Total number of clients", text = "Total number of clients")
list2['show'] = 'headings'
list2["displaycolumns"]=('Total number of quotes', 'Total value', 'Total number of clients')

list2.insert(parent = '', index = 1, values = (total_no_of_entries(), total_value(), number_of_clients()))

# creating pies
import matplotlib
import matplotlib.pyplot as pyplot
import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

#create pie for number of quotes per client
def pie_quotes_per_client():
    #create fig
    fig = pyplot.figure(num = 1, figsize=(4,3), facecolor="#4682B4", dpi = 80)
    # creates the pie:
    pyplot.axis("equal")
    list1.delete(*list1.get_children())
    c = []
    for row in database.view():
        list1.insert(parent='', index='end', values=row)
        c.append(row[-7])
    from collections import Counter  # dict subclass for counting hashable objects
    q = Counter(c)
    def absolute_value(val):
        gg=numpy.array([float(v) for v in q.values()])
        number_of_quotes  = numpy.round(val/100.*gg.sum(), 0)
        return number_of_quotes
    pyplot.pie([float(v) for v in q.values()], labels=[str(k) for k in q],
               autopct=absolute_value, textprops={'color':"w"})
    pyplot.suptitle('Number of quotes per client', fontsize=12, color = "white")
    #Creating Canvas
    canv = FigureCanvasTkAgg(fig, master = frame3)
    canv.draw()
    get_widz = canv.get_tk_widget()
    get_widz.grid(row = 3, column = 1, pady = 100, sticky = W)

pie_quotes_per_client()

# create pie for number of quotes per item
def pie_quotes_per_item():
    #create fig
    fig = pyplot.figure(num = 2, figsize=(4,3), facecolor="#4682B4", dpi = 80)
    # creates the pie:
    pyplot.axis("equal")
    list1.delete(*list1.get_children())
    c = []
    for row in database.view():
        list1.insert(parent='', index='end', values=row)
        c.append(row[-6])
    from collections import Counter
    q = Counter(c)
    def absolute_value(val):
        gg=numpy.array([float(v) for v in q.values()])
        number_of_quotes  = numpy.round(val/100.*gg.sum(), 0)
        return number_of_quotes
    pyplot.pie([float(v) for v in q.values()], labels=[str(k) for k in q],
               autopct=absolute_value, textprops={'color':"w"})
    pyplot.suptitle('Number of quotes per item', fontsize=12, color = "white")
    #Creating Canvas
    canv = FigureCanvasTkAgg(fig, master = frame3)
    canv.draw()
    get_widz = canv.get_tk_widget()
    get_widz.grid(row = 3, column = 2, pady = 100, sticky = E)

pie_quotes_per_item()

# create pie for amount per client
def pie_amount_per_client():
    #create fig
    fig = pyplot.figure(num = 3, figsize=(4,3), facecolor="#4682B4", dpi = 80)
    # creates the pie:
    pyplot.axis("equal")
    def absolute_value(val):
        gg=numpy.array([float(v) for v in amount_per_client().values()])
        number_of_quotes  = numpy.round(val/100.*gg.sum(), 1)
        return number_of_quotes
    pyplot.pie([float(v) for v in amount_per_client().values()], labels=[str(k) for k in amount_per_client()],
               autopct=absolute_value, textprops={'color':"w"})
    pyplot.suptitle('Amount per client (M eur)', fontsize=12, color = "white")
    #Creating Canvas
    canv = FigureCanvasTkAgg(fig, master = frame3)
    canv.draw()
    get_widz = canv.get_tk_widget()
    get_widz.grid(row = 3, column = 3, pady = 100, sticky = W)

pie_amount_per_client()

# create pie for amount per item
def pie_amount_per_item():
    #create fig
    fig = pyplot.figure(num = 4, figsize=(4,3), facecolor="#4682B4", dpi = 80)
    # creates the pie:
    pyplot.axis("equal")
    def absolute_value(val):
        gg=numpy.array([float(v) for v in amount_per_item().values()])
        number_of_quotes  = numpy.round(val/100.*gg.sum(), 1)
        return number_of_quotes
    pyplot.pie([float(v) for v in amount_per_item().values()], labels=[str(k) for k in amount_per_item()],
               autopct=absolute_value, textprops={'color':"w"})
    pyplot.suptitle('Amount per item (M eur)', fontsize=12, color = "white")
    #Creating Canvas
    canv = FigureCanvasTkAgg(fig, master = frame3)
    canv.draw()
    get_widz = canv.get_tk_widget()
    get_widz.grid(row = 3, column = 4, pady = 100, sticky = W)

pie_amount_per_item()

root.mainloop()
