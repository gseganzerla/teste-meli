def smaller_than(number: int, param: int):
  if number <= param:
    return number

def list_four_digits(number: int):
  x = int(f"{number}{number}{number}{number}")

  for i in range(1000, x):
    n = str(i)

    numbers = [int(n[0]), int(n[1]), int(n[2]), int(n[3])]

    filtered_number = list(filter(lambda x: smaller_than(x, number), numbers))

    listed = filtered_number

    if len(listed) == 4 and sum(listed) == 21:
      print(i)

list_four_digits(8)
