calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()
def is_contains(string, list_to_search):
    count_calls()
    list_to_search = ' '.join(list_to_search)
    if string.lower() not in list_to_search.lower():
        return False
    else:
        return True
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['Recycling', 'cyclic']))
print(calls)
