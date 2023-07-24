UnitType = input("What Unit is The Temperature in? (F/C)")
if UnitType == "C" or UnitType == "c" :
    Celsius_input = input("What Degree Celsius is the Temperature? ")
    Celsius_input = int(Celsius_input)
    print("Converting to Fahrenheit!!!")
    Celsius_conversion = ( Celsius_input * 9/5) + 32
    print(Celsius_conversion , "F" )
if UnitType == "F" or UnitType == "f" :
    Fahrenheit_input = input("What Degrees Fahrenheit is the temperature? ")
    Fahrenheit_input = int(Fahrenheit_input)
    print("Converting to Celsius!!!")
    Fahrenheit_conversion = ( Fahrenheit_input - 32 ) * (5/9)
    print(Fahrenheit_conversion , "C")