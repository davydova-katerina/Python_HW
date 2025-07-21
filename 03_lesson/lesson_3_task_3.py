from address import Address
from mailing import Mailing

to_address = Address("111111", "Москва", "Ленина", 1, 4)
from_address = Address("222222", "Омск", "1-го Мая", 2, 5)

mailing = Mailing(to_address, from_address, 100, "168574PG")

print(mailing)
