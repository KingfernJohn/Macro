from pkgutil import ModuleInfo
import pyautogui, time
print()
amount_s = input("Amount: ")
amount_s = int(amount_s)
text = input("Text: ")
print()
input("-Press enter to start the timer- ")
print()
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1\n")
time.sleep(1)
for i in range(amount_s):
    pyautogui.write(text_s, interval=0.001)
    pyautogui.press("enter")
