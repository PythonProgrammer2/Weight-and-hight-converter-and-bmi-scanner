try:
  def weight():
    weight = int(input('What is your weight? '))
    measurement = input('lb or kg: ').lower()
    if measurement == 'kg':
      result = weight*2.20462
      print(f'You are {result}lb')
    elif measurement == 'lb':
      result1 = weight//0.453592
      print(f'You are {result1}kg')
    else:
      print('I dont understand that')


  weight()
except ValueError:
  print('Invalid')


try:
  def height():
    height = float(input('What is your height? '))
    operation = input('cm or feet? ').lower()
    if operation == 'cm':
      current = height//0.0328084
      print(f'You are {current}feet')
    elif operation == 'feet':
      current1 = height*30.48
      print(f'You are {current1}cm')
    else:
      print('I dont understand that')


  height()
except ValueError:
  print('Invalid')
