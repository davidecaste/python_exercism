"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        ls = current_cart.setdefault(item, 0)
        current_cart[item] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    dic = {}
    for item in notes:
        x = dic.setdefault(item, 0)
        dic[item] += 1
    return dic 


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for item in recipe_updates:
        ideas[item[0]] = item[1]
    return ideas
 

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    nkeys = list(cart.keys())
    nkeys.sort()
    return {x: cart[x] for x in nkeys} 

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    ncart = {}
    for key in aisle_mapping.keys():
        if key in cart.keys():
            aisle_mapping[key].insert(0, cart[key])
            ncart[key] = aisle_mapping[key]
        else:
            continue
    
    nkeys = list(ncart.keys())
    nkeys.sort(reverse=True)
    return {x: ncart[x] for x in nkeys}


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for key in fulfillment_cart.keys():
        if key in store_inventory.keys():
            res = store_inventory[key][0] - fulfillment_cart[key][0]
            if res > 0:
                store_inventory[key][0] = res
            else:
                store_inventory[key][0] = 'Out of Stock'
        else:
            continue 
    return store_inventory
