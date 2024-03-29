
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool


class PartyMapsTestCase(ModuleTestCase):
    'Test PartyMaps module'
    module = 'party_maps'

    @with_transaction()
    def test_maps(self):
        "Test Maps"
        pool = Pool()
        Party = pool.get('party.party')
        Address = pool.get('party.address')

        party = Party()
        party.name = 'NaN-tic'
        party.save()

        address = Address()
        address.party = party
        address.street = "Carrer de les Paus"
        address.postal_code = "08202"
        address.city = "Sabadell"
        address.map_place = "Carrer de les Paus 08202 Sabadell"
        address.save()
        Address.geocode([address])
        self.assertEqual('%s' % address.latitude, '41.5508144')
        self.assertEqual('%s' % address.longitude, '2.1118345')
        self.assertEqual(
            address.on_change_with_map_url(),
            'https://www.openstreetmap.org/search?'
            'query=41.55081440%2C2.11183450')


del ModuleTestCase
