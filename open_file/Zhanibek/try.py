
# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")
# else:
#     print("Nothing went wrong")

# finally:
#     print("The 'try except' is finished")


# x = -1
#
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")



# x = "hello"
#
# if not type(x) is int:
#   raise TypeError("Only integers are allowed")


# try:
#   f = open('rawdata.txt')
# except FileNotFoundError as e:
#   print(e)
# except Exception as e:
#   print(e)
# else:
#   print(f.read())
#   f.close()
# finally:
#   print("Executing Finally...")
#


try:
    f = open("rawdata.txt")
    try:
        print(f.readline())
    except:
        print("NO")
    finally:
        print("Final")
except:
  print("Something went wrong when opening the file")

print("Olzhas done")