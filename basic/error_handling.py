try:
    b='a'
    float(b)
    int(b)
    a = 10/0
except Exception as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")