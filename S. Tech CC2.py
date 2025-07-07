from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox

class CreditCard:

    def __init__ (self,master):
        master.title("Credit Card")
        master.geometry("1000x500")
        master.configure(bg='#141E46')

        self.master = master
        self.card_number = StringVar()
        self.card_name = StringVar()
        self.credit_limit = IntVar()
        self.min_pay = IntVar()
        self.total_tagihan = 0
        self.credit_new = 0

        self.picture = PhotoImage(file="kartunih.png")
        self.picture_label = tk.Label(self.master, image=self.picture, bg='#141E46')
        self.picture_label.place(x=645,y=10)

        tk.Label(master,text="Card Number", bg='#141E46', fg='white').place(x=30, y=20)
        tk.Entry(master, textvariable=self.card_number, width=80, bg='#FFF5E0').place(x=150, y=20)

        tk.Label(master,text="Card Name", bg='#141E46', fg='white').place(x=30, y=60)
        tk.Entry(master, textvariable=self.card_name, width=80, bg='#FFF5E0').place(x=150, y=60)

        tk.Label(master, text="Credit Limit: ", bg='#141E46', fg='white').place(x=30, y=100)
        tk.Entry(master, textvariable=self.credit_limit, width=80, bg='#FFF5E0').place(x=150, y=100)

        tk.Label(master, text="Minimum Payment: ", bg='#141E46', fg='white').place(x=30, y=140)
        tk.Entry(master,bg='#FFF5E0',width=80,state='readonly').place(x=150,y=140)

        tk.Button(master, text="SUBMIT", width=85, bg='blue',command=self.layout).place(x=30, y=200)
        tk.Button(master, text="CHECK REMAIN KREDIT", width=19, bg='#FF6969', fg='#FFF5E0',command=self.check_remain_kredit).place(x=30, y=300)
        tk.Button(master, text="PURCHASE", width=19, bg='#FF6969', fg='#FFF5E0',command=self.purchase).place(x=425, y=300)
        tk.Button(master, text="PAY", width=19, bg='#FF6969', fg='#FFF5E0',command=self.pay).place(x=825, y=300)
        tk.Button(master, text="EXIT", width=85, bg='red', fg='white',command=master.destroy).place(x=200, y=450)

        self.label_nomor_kartu = Label(master, font=("Credit Card", 16), bg='#4f689e')
        self.label_nomor_kartu.place(x=670, y=30)
        self.label_nama_kartu = Label(master, font=("Credit Card", 16), bg='#5b76ad')
        self.label_nama_kartu.place(x=670, y=175)
        self.label_min_payment = Label(master, width=68, bg='#FFF5E0')
        self.label_min_payment.place(x=150, y=140)
        self.label_tagihan = Label(master, text="", font=("Helvetica", 10), bg='#141E46', fg='white')
        self.label_tagihan.place(x=650, y=240)
        self.layout()

    def layout(self):
        card_number = self.card_number.get()
        card_name = self.card_name.get()

        if card_name and not card_name.isalpha() and card_number and not card_number.isdigit():
            messagebox.showwarning("Warning", "Tolong inputkan card number dan card name dengan benar")
            return
        
        # Memastikan nama kartu hanya berisi huruf
        if card_name and not card_name.replace(" ", "").isalpha():
            messagebox.showwarning("Warning", "Tolong masukkan huruf saja pada card name")
            return

        if card_number and not card_number.isdigit():
            messagebox.showwarning("Warning", "Tolong masukkan angka saja pada card number")
            return
        
        if card_number and (not card_number.isdigit() or len(card_number) != 12):
            messagebox.showwarning("Warning", "Tolong masukkan angka sebanyak 12 digit pada card number")
            return
        
        if card_name and (not card_name.replace(" ", "").isalpha() or len(card_number) > 30):
            messagebox.showwarning("Warning", "Tolong masukkan huruf sebanyak 14" )
            return

        self.label_nomor_kartu.config(text=card_number)
        self.label_nama_kartu.config(text=card_name)
        self.label_min_payment.config(text=f"{int(self.credit_limit.get() * 0.1)}")
        self.update_tagihan_label()

    def purchase(self):
        pembayaran_barang = simpledialog.askinteger("Purchase", "Masukkan nominal anda:")
        sisa_kredit = self.credit_limit.get() - self.credit_new
        if pembayaran_barang <= sisa_kredit:
            self.total_tagihan += pembayaran_barang
            self.credit_new += pembayaran_barang
            messagebox.showinfo("Info","Purchase berhasil")
            self.update_tagihan_label()
        else:
            self.check_remain_kredit()
            if sisa_kredit == 0 :
                messagebox.showwarning("Warning",f"SISA KREDIT ANDA NOL ,GAUSAH BELANJA LAGI BAYAR TAGIHAN ANDA!")
            elif pembayaran_barang > sisa_kredit:
                messagebox.showwarning("Error","Purchase melebihi credit limit")
    
    def pay(self):
        pembayaran_tagihan = simpledialog.askinteger("Payment", "Masukkan nominal bayar tagihan:")
        min_pay = self.credit_limit.get() * 0.1

        if pembayaran_tagihan >= min_pay:
            if pembayaran_tagihan <= self.total_tagihan:
                self.total_tagihan -= pembayaran_tagihan
                messagebox.showinfo("Info","Pembayaran Berhasil")
                self.update_tagihan_label()
            else:
                messagebox.showwarning("Warning","Pembayaran melebihi tagihan")
        else:
                messagebox.showerror("Error","Pembayaran dibawah min pembayaran")

    def check_remain_kredit(self):
        sisa_kredit = self.credit_limit.get() - self.credit_new
        if sisa_kredit == 0:
            messagebox.showwarning("Warning",f"SISA KREDIT ANDA NOL, GAUSAH BELANJA LAGI!")
        else:
            messagebox.showinfo("Remaining Credit", f"Sisa Kredit Anda : Rp.{sisa_kredit}")


    def update_tagihan_label(self):
        self.label_tagihan.config(text=f"Tagihan Kartu Kredit Anda : Rp. {self.total_tagihan}")

    def validate_card_number(self, new_value):
        # Callback function to validate the input as numeric
        if new_value.isdigit() or new_value == "":
            return True
        else:
            print("Tolong masukkan angka saja")
            return False


root = Tk()
gui = CreditCard(root)
root.mainloop()

