
import json


class Phonebook:
    def __init__(self, filename:str):
        self.filename = filename
        self.contacts = []
        self.load_phonebook()

    def load_phonebook(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass
        # Загружаем файл json
    def save_phonebook(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.contacts, file, indent=4,ensure_ascii=False)
        # Сохраняем файл так, чтобы не поменять кодировку
    def display_page(self, page_number:int):
        records_per_page = 5
        # Выводим по 5 записей на страницу
        start = (page_number - 1) * records_per_page
    # Определяем начальную запись, на нужной странице
        end = start + records_per_page
        # конечная запись на странице
        for contact in self.contacts[start:end]:
            print(f"Фамилия: {contact['last_name']}")
            print(f"Имя: {contact['first_name']}")
            print(f"Отчество: {contact['middle_name']}")
            print(f"Компания: {contact['company']}")
            print(f"Рабочий номер: {contact['work_number']}")
            print(f"Мобильный номер: {contact['mobile_number']}")
            print()
        # Красиво выводим контакты, получая зхначения из json файла
        # перебирая каждый элемент начиная от start до end
    def add_record(self):
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        company = input("Введите компанию: ")
        work_number = input("Введите рабочий номер телефона: ")
        mobile_number = input("Введите мобильный номер: ")
        # Получаем значения
        new_record = {
            "last_name": last_name,
            "first_name": first_name,
            "middle_name": middle_name,
            "company": company,
            "work_number": work_number,
            "mobile_number": mobile_number
        }
        # Записываем полученные значения в json формате
        self.contacts.append(new_record)
        # Добавляем в наш список
        self.save_phonebook()
        # и сохраняем обновление

    def edit_record(self, index:int):
        if 0 <= index < len(self.contacts):
            # Проверяем, чтобы вводимое значение было корректным
            contact = self.contacts[index]
            # Достаем нужную нам запись
            contact["last_name"] = input("Введите фамилию: ")
            contact["first_name"] = input("Введите имя: ")
            contact["middle_name"] = input("Введите отчество: ")
            contact["company"] = input("Введите компанию: ")
            contact["work_number"] = input("Введите рабочий номер телефона: ")
            contact["mobile_number"] = input("Введите мобильный номер: ")
            # Вводим новые значения под каждый ключ
            self.save_phonebook()
            # Сохраняем
            print("Запись успешно отредактирована.")
        else:
            print("Некорректный индекс записи.")

    def search_records(self, search:str):
        results = []
        for contact in self.contacts:
            if any(search.lower() in value.lower() for value in contact.values()):
                results.append(contact)
        return results


def main():
    phonebook = Phonebook('phonebook.json')
    # Указываем необходимый файл json формата для работы в классе Phonebook
    while True:
        print("Выберите опцию:")
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")
        # Список опций
        choice = input()

        if choice == "1":
            page_number = int(input("Введите номер страницы: "))
            phonebook.display_page(page_number)
        elif choice == "2":
            phonebook.add_record()
        elif choice == "3":
            index = int(input("Введите индекс записи для редактирования: "))
            phonebook.edit_record(index)
        elif choice == "4":
            search = input("Введите критерии поиска: ")
            results = phonebook.search_records(search)
            for contact in results:
                print(f"Фамилия: {contact['last_name']}")
                print(f"Имя: {contact['first_name']}")
                print(f"Отчество: {contact['middle_name']}")
                print(f"Компания: {contact['company']}")
                print(f"Рабочий номер: {contact['work_number']}")
                print(f"Мобильный номер: {contact['mobile_number']}")
                print()
        elif choice == "5":
            print("Спасибо за использование! До свидания!")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите опцию от 1 до 5.")

if __name__ == "__main__":
    main()