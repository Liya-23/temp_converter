#ask the user what temperature they want to convert
UnitType = input("What Unit is The Temperature in? (F/C)")

#if it happens to be in Celcius it must be converted to Fahrenheit
if UnitType.upper() == "C":
    Celsius_input = input("What Degree Celsius is the Temperature? ")
    Celsius_input = int(Celsius_input)
    #display which type of temperature we are converting to
    print("Converting to Fahrenheit!!!")
    #conversion formula
    Celsius_conversion = ( Celsius_input * 9/5) + 32
    print(Celsius_conversion , "F" )

#if it happens to be in Fahreinheit it must be converted to Celcious
if UnitType.upper() == "F":
    Fahrenheit_input = input("What Degrees Fahrenheit is the temperature? ")
    Fahrenheit_input = int(Fahrenheit_input)
    #display which type of temperature we are converting to
    print("Converting to Celsius!!!")
    #conversion formula
    Fahrenheit_conversion = ( Fahrenheit_input - 32 ) * (5/9)
    print(Fahrenheit_conversion , "C")
