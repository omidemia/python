from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "15")

mailing = Mailing(to_address, from_address, 1500, "TRACK123456789")

message = (f"Отправление {mailing.track} из "
           f"{mailing.from_address.index}, {mailing.from_address.city}, "
           f"{mailing.from_address.street}, {mailing.from_address.house} - "
           f"{mailing.from_address.apartment} в "
           f"{mailing.to_address.index}, {mailing.to_address.city}, "
           f"{mailing.to_address.street}, {mailing.to_address.house} - "
           f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")

print(message)
