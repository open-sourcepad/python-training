meals = (1, 1.5, 2, 2.5, 3, 3.7, 4, 5, 6, 7,)
pm_meals = []

[pm_meals.append("PM {}".format(meal)) for meal in meals if meal not in [2.5, 3.7]]
