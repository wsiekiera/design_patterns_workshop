class Customer:
    def __init__(self):
        self.products = []
    # def __init__(self, name, surname, email, phone_number, street, house_number, zip_code, city):
    #     self.name = name
    #     self.surname = surname
    #     self.email = email
    #     self.phone_number = phone_number
    #     self.street = street
    #     self.house_number = house_number
    #     self.zip_code = zip_code
    #     self.city = city


class Product:
    pass


class ProductBuilder:
    def __init__(self):
        self.product = Product()

    def with_type(self, product_type):
        self.product.product_type = product_type
        return self

    def with_number(self, number):
        self.product.number = number
        return self

    def build(self):
        return self.product


class CustomerBuilder:
    def __init__(self):
        self.customer = Customer()

    def reset(self):
        self.customer = Customer()

    def with_name(self, name):
        self.customer.name = name
        return self

    def with_surname(self, surname):
        self.customer.surname = surname
        return self

    def with_email(self, email):
        self.customer.email = email
        return self

    def with_phone_number(self, phone_number):
        self.customer.phone_number = phone_number
        return self

    def with_product(self, product):
        self.customer.products.append(product)
        return self

    def build(self):
        return self.customer


if __name__ == '__main__':
    builder = CustomerBuilder() \
        .with_name('Jan') \
        .with_surname('Kowalski') \
        .with_email('somemail@gmail.com') \
        .with_phone_number('777888999') \
        .with_product(ProductBuilder().with_type('ACCOUNT').with_number('1234567').build()) \
        .with_product(ProductBuilder().with_type('CREDIT').with_number('98765').build())
    customer1 = builder.build()
    builder.reset()
    builder.with_name('Ewa').with_surname('Nowak').with_email('aaa@wp.pl').with_phone_number('445566667')
    customer2 = builder.build()

    print('a')
    # client1 = Customer("Jan", "Kowalski", 'jankowalski@gmail.com', '1234', 'Sokolska', '34', '40-111', 'Katowice')
