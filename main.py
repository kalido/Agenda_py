# -*- coding: utf-8 -*-
import csv

class Dude:

    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

class Agenda:
    
    def __init__(self):
        self._dudes = []

    def add_new(self, name, phone,email):
        dude = Dude(name, phone, email)
        self._dudes.append(dude)
        self._save()
     
    def show_all(self):
        for dude in self._dudes:
            self._print_dude(dude)

    def delete(self, name):
        for idx, dude in enumerate(self._dudes):
            if dude.name.lower() == name.lower():
                del self._dudes[idx]
                self._save()
                break

    def update(self, name):
        for i, dude in enumerate(self._dudes):
            if dude.name.lower() == name.lower():
                dude.name = str(input('Type a new name: '))
                dude.phone = str(input('Type a new phone number: '))
                dude.email = str(input('Type a new email: '))
                self._dudes[i] = dude
                break
        else:
            self._not_found()

    def search (self, name):
        for dude in self._dudes:
            if dude.name.lower() == name.lower():
                self._print_dude(dude)
                break
        else:
            self._not_found()

    def _save(self):
        with open('dudes.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            for dude in self._dudes:
                writer.writerow((dude.name, dude.phone, dude.email))

                
    def _not_found(self):
        print('**********************************')
        print('User not found, try again please.!')
        print('**********************************')

    def _print_dude(self, dude):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Name: {}'.format(dude.name))
        print('Phone: {}'.format(dude.phone))
        print('Email: {}'.format(dude.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')


def run():
    agenda = Agenda()
    
    with open('dudes.csv', "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                if row == []:
                    continue

                agenda.add_new(row[0], row[1], row[2])

    while True:
        command = str(input('''
            Select an option:

            [a]dd dude
            [u]pdate dude
            [s]earch dude
            [d]elete dude
            [l]ist dudes
            [e]xit
        '''))

        command = command.lower()

        if command == 'a':
            name = str(input('Type a user name: '))
            phone = str(input('Type a dude phone number: '))
            email = str(input('Type your email address: '))
            agenda.add_new(name,phone,email)

        elif command == 'u':
            name = str(input('What name would you like update? type it.'))
            agenda.update(name)

        elif command == 's':
            name = str(input('Write a user name: '))
            agenda.search(name)

        elif command == 'd':
            name = str(input('Write a user name: '))
            agenda.delete(name)

        elif command == 'l':
            agenda.show_all()

        elif command == 'e':
            break
        else:
            print('Command not valid.')


if __name__ == '__main__':
    run()