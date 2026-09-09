class Leapyear:
    def year(self,year):
     if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
       print(year, "is leap year")
     else:
        print(year,"not leap year")

year_instance=Leapyear()
year_instance.year(2024)
year_instance.year(2023)