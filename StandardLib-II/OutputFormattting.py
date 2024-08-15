import reprlib

custom_representation = reprlib.repr(set('jackofallandmasterofnone'))
print(custom_representation)                                                # customized for abbreviated displays of large or deeply nested containers


import pprint
t = t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
pprint.pprint(t, width=30)
[[[['black', 'cyan'],'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]   # more sophisticated control over printing both built-in and user defined objects


import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))                         # module formats paragraphs of text to fit a given screen width


import locale
locale.setlocale(locale.LC_ALL, 'en_IN.utf8')           # The locale module accesses a database of culture specific data formats
conv = locale.localeconv()                                         # get mapping of conventions
x = 1234567.8
temp = locale.format_string("%d", x, grouping=True)
print(temp)
var_temp = locale.format_string("%s%.*f", (conv['currency_symbol'],   conv['frac_digits'], x), grouping=True)
print(var_temp)             # output : ₹12,34,567.80 based on setlocale()