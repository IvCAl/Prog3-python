def concat(arr:list):
    try:
        return  ''.join([str(i) for i in arr])
    except Exception as e:
        print("Error:",e)
        
print(concat([1,2,3,'a','b',4.5])) 