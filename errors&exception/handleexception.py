while True:
    try:
        x = int(input("Please enter a numeric password...."))
        break
        # handle one exception
    except ValueError:
        print("Opps , that was not valid password. Try again!")
        # handling multiple exception
    except (ValueError, RuntimeError, TypeError, NameError):
        pass



