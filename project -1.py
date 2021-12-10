a = []
for i in range (1 ,5):
    a.append(int(input('nhập '+str(i) + ': ')))
def so_xuat_hien_nhieu_nhat(a):    
    b =[]
    for i in range(len(a)-1): 
        b.append(a.count(a[i]))
    for i in range(len(b)-1):
        if b[i] == min(b):
            c = 'không tồn tại'
        elif b[i] == max(b):
            c = a[i]
    return c        
def sap_xep_tu_be_den_lon(a):
    a.sort()
    return a
def sap_xep_tu_lon_den_be(a):
    a.sort(reverse=True)
    return a


print ("số lớn nhất là: ",max(a))
print ("số nhỏ nhất là: ",min(a))
print('giá trị xuất hiện nhiều nhất: ',so_xuat_hien_nhieu_nhat(a))
print('sắp xếp từ bé đến lớn:', sap_xep_tu_be_den_lon(a))
print('sắp xếp từ lớn đến bé:', sap_xep_tu_lon_den_be(a))