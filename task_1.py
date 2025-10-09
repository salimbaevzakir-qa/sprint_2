class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")


class ExtendedCase(Case):
    def __init__(self, test_case_id, name, step_description, expected_result, precondition, environment):
        super().__init__(test_case_id, name, step_description, expected_result)
        self.precondition = precondition
        self.environment = environment

    def print_test_case_info(self):
        super().print_test_case_info()
        print(f"\nПредусловие: {self.precondition}"
              f"\nОкружение: {self.environment}")


extended_cases = [
    ExtendedCase(
        test_case_id=1,
        name="Тест входа",
        step_description="Ввести имя пользователя и пароль",
        expected_result="Пользователь вошел в систему",
        precondition="Пользователь зарегистрирован",
        environment="Веб"
    ),
    ExtendedCase(
        test_case_id=2,
        name="Тест выхода",
        step_description="Нажать кнопку выхода",
        expected_result="Пользователь вышел из системы",
        precondition="Пользователь вошел в систему",
        environment="Веб"
    ),
    ExtendedCase(
        test_case_id=3,
        name="Тест добавления в корзину",
        step_description="Добавить товар в корзину",
        expected_result="Товар добавлен в корзину",
        precondition="Пользователь вошел в систему",
        environment="Мобильное приложение"
    ),
]

# Вывод информации о каждом расширенном тест-кейсе
for case in extended_cases:
    case.print_test_case_info()
    print("\n" + "-" * 50 + "\n")
