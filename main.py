size = int(input("Enter the size of the star: "))-1
recovery = size
char_to_use = input("Enter the symbol of the star's mini particle: ")
space_count = size
while space_count > -1:
    print((" "*space_count)+char_to_use*(2*(size-space_count)+1))
    space_count-=1
size = recovery
space_count = size
while space_count > -1:
    print((" "*(size-space_count+1))+(char_to_use*(2*(space_count)-1)))
    space_count-=1
