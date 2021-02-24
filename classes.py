class MangInasal:
    def __init__(self, **kwargs):
      self.kwargs = kwargs

    def rice_statement(self):
      print(f"Rice count: {self.kwargs['rice_count']}")

    def menu(self):
      fav_list = ['PM1', 'PM1.5', 'PM2', 'PM3', 'PM4', 'PM5', 'PM6', 'PM7']

      return fav_list

    def is_available(self):
      fav = self.kwargs['favorite']

      if fav in self.menu():
        print(f"{fav} is available!")
      else:
        print(f"{fav} not available")