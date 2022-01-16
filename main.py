import random


def create_database():
    all_names = [name.rstrip() for name in open('names.txt', encoding='utf-8').readlines()]
    female_names = [name for name in all_names if name.endswith('a')]

    all_surnames = [name.rstrip() for name in open('surnames.txt', encoding='utf-8').readlines()]

    female_surnames = [surname for surname in all_surnames if not surname.endswith('ski')
                       and not surname.endswith('cki') and not surname.endswith('sny')
                       and not surname.endswith('zki')]

    male_surnames = [surname for surname in all_surnames if not surname.endswith('ska')
                     and not surname.endswith('cka') and not surname.endswith('zka')
                     and not surname.endswith('sna')]

    cities = [city.rstrip() for city in open('cities.txt', encoding='utf-8').readlines()]

    def record():
        """The function creates the number of records based on user input."""
        while True:
            try:
                num_records = int(input("Enter the number of records: "))
                break
            except ValueError:
                print('Invalid value! Try again...')

        database = []
        for i in range(1, num_records + 1):
            name_choice = random.choice(all_names)
            if name_choice in female_names:
                surname_choice = random.choice(female_surnames)
            else:
                surname_choice = random.choice(male_surnames)
            city_choice = random.choice(cities)
            database.append([name_choice, surname_choice, city_choice])

        def save_data():
            name_file = input('Enter the name of the text file [name.txt]: ')
            data = open(name_file, 'w', encoding='utf=8')
            for entry in database:
                record_string = str(entry[0]) + "," + str(entry[1]) + "," + str(entry[2]) + '\n'
                data.write(record_string)
            data.close()
            print(f'Records were created in the file: {name_file}.')

        save_data()

    record()


def main():
    print('Program will create a simple database.')
    print()
    create_database()

if __name__ == '__main__':
    main()
