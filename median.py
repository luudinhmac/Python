def median(arr1,arr2):
    # xac dinh mang co kich thuoc nho hon
    if len(arr1) > len(arr2):
        arr1,arr2 = arr2,arr1
    n = len(arr1)
    m = len(arr2)
    start =0 # Chỉ số bắt đầu của mảng arr1
    end = n # chỉ số kết thúc của mảng arr1
    while start <= end:
        mid1 = (start+end)//2 # chỉ mục giữa của arr1
        # chỉ mục giữa của mảng arr2
        mid2 = (m+n+1)//2 -mid1       
        # Xác định giá trị leftMax1 và rightMin1       
        leftMax1 = float('inf') if mid1 ==0 else arr1[mid1-1]
        rightMin1 = float('inf') if mid1 ==n else arr1[mid1]
        leftMax2 = float('inf') if mid2 ==0 else arr2[mid2-1]
        rightMin2 = float('inf') if mid2 ==n else arr2[mid2]

        if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
            # Trường hợp tổng số phần tử là lẻ
            if (n+m)%2 ==1:
                return max(leftMax1, leftMax2)
            # Trường hợp tổng số phần tử là chẵn
            else:
                return (max(leftMax1,leftMax2) + min(rightMin1,rightMin2))/2
        elif leftMax1 > rightMin2:
            end = mid1 -1  # di chuyen sang ben trai tren arr1
        else:
            start = mid1 +1 # di chuyen sang ben phai arr1
    return None

# 1 3    5 7
# mid1  =2  
# left max1 = m1[1] =3 
# right min1 =m[2] =5

# mid2 =2
# 2 4    6 8
# left max2 = m2[1] = 4
# right min2 = m[2] = 6
x = "Hello"[0]


m1 = [1,3,5,7]
m2 = [2,4]
print(median(m1,m2))
