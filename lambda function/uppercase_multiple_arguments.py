first_names = ['john', 'jane', 'alice']
last_names = ['doe', 'smith', 'cooper']
full_names = list(map(lambda f, l: (f + ' ' + l).upper(), first_names, last_names))
print("Full Names:", full_names)
