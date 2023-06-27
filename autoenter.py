import pyautogui, pyperclip, random, time
print("Tool Spam 1.0")
msg1=["Xin lỗi","Cảm ơn"]
msg = input("Nhập nội dung cần spam: ").split(" || ")
n = int(input("Nhập số lần Spam =)) "))
m = float(input("Nhập thời gian delay: "))

print("Chuẩn bị")
#Đếm ngược 5 giây1


for i in range(5,0,-1):
 print(i,end="...",flush='True')
 time.sleep(1)

print("Bắt đầu")

#SPAM
for i in range(n):
 pyperclip.copy(random.choice(msg1))
 pyautogui.hotkey("ctrl","v")
 pyautogui.press("enter")
 pyautogui.press("a")
 pyautogui.press("del")
# time.sleep(m) #Delay

