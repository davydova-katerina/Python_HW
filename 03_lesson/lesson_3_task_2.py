from smartphone import Smartphone

catalog = [
    Smartphone("IPhone", "15Pro", +79123456789),
    Smartphone("Samsung", "A3", +79234567891),
    Smartphone("LG", "Razer", +79345678912),
    Smartphone("Sony", "Q1", +79456789123),
    Smartphone("Honor", "XE", +79567891234)
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
