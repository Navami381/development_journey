def function_is_leap_year(year):

    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):

            print(True)

    else:
            print(False)

function_is_leap_year(2026)    
function_is_leap_year(2024)        

       