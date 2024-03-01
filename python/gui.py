import tkinter as tk
from tkinter import messagebox

def cons_form_show_message():
    messagebox.showinfo("Message", "공사형태\n 1. 외선불요 : 외선공사가 필요없음 \n 2. 외선소요 : 설계서작성을 하고 외선공사가 필요함 \n 3. 선공급")

def cons_clcd_show_message():
    messagebox.showinfo("Message", "공사비 유형은? \n 1. 표준시설부담금 : 당사부담이므로 고객부담이 없다.-> 한전 측에서 모든 비용을 부담 \n 2. 설계유형부담금 \n 3. 설계조정부담금 : 설계에 따라서 비용분담을 하게된다.")

def tips_show_message():
    messagebox.showinfo("Message", "휴전안내시행은 MCS 직원 중에 가장 낮은 직위의 직원한테 배분한다.")


# Create the main application window
root = tk.Tk()
root.title("KEPCO_DATA_KNOWLEDGE")

# Create a button and add it to the window
btn_cons_clcd = tk.Button(root, text="공사비유형", command=cons_clcd_show_message)
btn_cons_form = tk.Button(root, text="공사형태", command=cons_form_show_message)
btn_tip1 = tk.Button(root, text="정휴전", command=tips_show_message)
btn_cons_clcd.pack(pady=20)
btn_cons_form.pack(pady=20)
btn_tip1.pack(pady=10)

# Start the main event loop
root.mainloop()
