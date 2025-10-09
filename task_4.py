class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment


# Сотрудник с известными часами и email
employee1 = EmployeeSalary("Иван", 40, 2, "ivan@company.com")
print(f"Зарплата {employee1.name}: {employee1.salary()}")

# Сотрудник с неизвестными часами (рассчитываются по rest_days)
employee2 = EmployeeSalary.get_hours("Мария", None, 2, "maria@company.com")
print(f"Часы работы {employee2.name}: {employee2.hours}")
print(f"Зарплата {employee2.name}: {employee2.salary()}")

# Сотрудник с неизвестным email (генерируется автоматически)
employee3 = EmployeeSalary.get_email("Петр", 35, 2, None)
print(f"Email {employee3.name}: {employee3.email}")
print(f"Зарплата {employee3.name}: {employee3.salary()}")

# Изменение почасовой оплаты
EmployeeSalary.set_hourly_payment(500)
employee4 = EmployeeSalary("Анна", 40, 2, "anna@company.com")
print(f"Новая зарплата {employee4.name} (после повышения ставки): {employee4.salary()}")
