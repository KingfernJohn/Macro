from pkgutil import ModuleInfo
import pyautogui, time
print()
amount_s = input("Amount: ")
amount_s = int(amount_s)
text = input("Text: ")
print()
time.sleep(2)
for i in range(amount_s):
    pyautogui.write(text, interval=0.00069)
    pyautogui.press("enter")
quit()