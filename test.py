import datetime
from decimal import Decimal, getcontext
goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},],
    
    'Вода': [{'amount': Decimal('1.5'), 'expiration_date': None}],}
def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    elif expiration_date != None:
        expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
    elif expiration_date == None:
        expiration_date = None
    items[title].append({'amount': Decimal(str(amount)), 'expiration_date' : expiration_date})
    return None
def add_by_note(items, note):
    note = note.split(' ')
    if datetime.strptime(note[-1], '%Y-%m-%d') == True:
        expiration_date = datetime.datetime.strptime(note[-1], '%Y-%m-%d').date()
        amount = note[-2]
        title = ' '.join(note[:-2])
    else:
        expiration_date = None
        amount = note[-1]
        title = ' '.join(note[:-1])
    add(goods, title, amount, expiration_date)
    return None
def find(items, needle):
    ...


def amount(items, needle):
    ...


def expire(items, in_advance_days=0):
    ...