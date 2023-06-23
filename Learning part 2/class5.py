filename = input('Write file name: ')
contents = input('Write file contents: ')
with open(filename,'w') as file:
    file.write(contents)