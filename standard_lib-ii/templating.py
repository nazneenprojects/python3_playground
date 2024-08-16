from string import Template

t = Template('${village} folk send $$10 to $cause.')             # The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users.
result = t.substitute(village='Nottingham', cause='the ditch fund')

print(result)


t = Template('Return the $item to $owner.')                         # It will leave placeholders unchanged if data is missings
d = dict(item='unladen swallow')
output = t.safe_substitute(d)               # this will not give error
#output = t.substitute(d)                    # this will give error




fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# output Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f


# t = BatchRename(fmt)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=date, n=i, f=ext)
#     print('{0} --> {1}'.format(filename, newname))