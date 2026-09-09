"""
Add 18% GST Input:[100,250,500,800] Output:[118.0,295.0,590.0,944.0]
"""
numbers=[100,250,500,800]

result=[num+((18/100)*num) for num in numbers] #mapping

print(result)