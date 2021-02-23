class MangInasal:

    def __init__(self, rice_count=None):
        self.rice_count = rice_count
        self.values = [1, 1.5, 2, 2.5, 3, 3.7, 4, 5, 6, 7]
        self.dont_display = [2.5, 3.7]

    def rice_statement(self):
        print('Rice count is {}'.format(self.rice_count))

    def menu(self):
        print(['PM{}'.format(value) for value in self.values if value not in self.dont_display])

    def is_available(self, favorite=None):
        menu = ['PM{}'.format(value) for value in self.values if value not in self.dont_display]
        if favorite in menu:
            print(True)
        else:
            print(False)

MangInasal(rice_count=5).rice_statement()
MangInasal().menu()
MangInasal().is_available('PM2')
