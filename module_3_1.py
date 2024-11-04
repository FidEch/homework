calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info():
    string = input(" Enter string_1: ")
    print(len(string), string.lower(), string.upper())
    count_calls()
def is_contains():
    string = ["one", "two", "three"]
    n = input(" Enter one or two or three: ")
    for n in string:
        if n == "one" or "two" or "three":
            list_to_search = True
        else:
            list_to_search = False
    print(list_to_search)
    count_calls()
string_info()
is_contains()
print(calls)
