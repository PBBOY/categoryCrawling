import math

def calc_dev_price(start_price, end_price, product_count, dash = ''):

    print(dash,start_price, '~', end_price, ':', product_count)

    if product_count < 800:
        # start Parsing
        # print(dash,'result: ', start_price, end_price, product_count)

        return True

    else:
        half_pric = math.ceil((start_price + end_price)/ 2)

        calc_dev_price(start_price, half_pric, math.ceil(product_count/4), '-'+dash)
        print(dash, ' ---------------------------------------')
        calc_dev_price(half_pric, end_price, math.ceil(product_count/2), '-'+dash)




calc_dev_price(0, 50000, 10000)