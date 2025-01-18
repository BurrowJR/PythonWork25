def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

'''
The first call to bar_code_scanner prints 'Product2' because the '113' matches the case on line 5
The second call to bar_code_scanner prints 'Product not found!' since the 142 is an integer instead of a string '142' it will print the default case on line 9 '''