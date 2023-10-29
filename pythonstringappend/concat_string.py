from io import StringIO
 
 
 
concat_str = StringIO()
 
 
 
concat_str.write('This ')
 
concat_str.write('example ')
 
concat_str.write('is ')
 
concat_str.write('for ')

concat_str.write('StringIO')
 
 
 
print(concat_str.getvalue())