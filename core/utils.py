from itertools import permutations
from core.models import Address, Distance

def generate_address_pairs():
    addresses = list(Address.objects.all())
    for from_address, to_address in permutations(addresses, 2):
        if not Distance.objects.filter(from_address=from_address, to_address=to_address).exists():
            Distance.objects.create(from_address=from_address, to_address=to_address)
