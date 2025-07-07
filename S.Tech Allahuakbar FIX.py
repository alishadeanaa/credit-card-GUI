from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox
import customtkinter
from PIL import ImageTk

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


        tk.Label(master,text="Card Number", bg='#141E46', fg='white').place(x=30, y=20)
        tk.Entry(master, textvariable=self.card_number, width=80, bg='#FFF5E0').place(x=150, y=20)

        tk.Label(master,text="Card Name", bg='#141E46', fg='white').place(x=30, y=60)
        tk.Entry(master, textvariable=self.card_name, width=80, bg='#FFF5E0').place(x=150, y=60)

        tk.Label(master, text="Credit Limit: ", bg='#141E46', fg='white').place(x=30, y=100)
        tk.Entry(master, textvariable=self.credit_limit, width=80, bg='#FFF5E0').place(x=150, y=100)

        tk.Label(master, text="Minimum Payment: ", bg='#141E46', fg='white').place(x=30, y=140)
        tk.Entry(master,bg='#FFF5E0',width=80,state='readonly').place(x=150,y=140)
        
        

        customtkinter.CTkButton(master, text="SUBMIT", width=600,command=self.layout, font=("sans serif bold", 12)).place(x=30, y=200)
        tk.Button(master, text="CHECK REMAIN KREDIT", width=19, bg='#FF6969', fg='#FFF5E0',command=self.check_remain_kredit).place(x=30, y=300)
        tk.Button(master, text="PURCHASE", width=19, bg='#FF6969', fg='#FFF5E0',command=self.purchase).place(x=425, y=300)
        tk.Button(master, text="PAY", width=19, bg='#FF6969', fg='#FFF5E0',command=self.pay).place(x=825, y=300)
        tk.Button(master, text="EXIT", width=85, bg='red', fg='white',command=master.destroy).place(x=200, y=450)


    def layout(self):


        card_number = self.card_number.get()
        card_name = self.card_name.get()
        credit_limit = self.credit_limit.get()

        
        
        # apabila terjadi kesalahan penulisan dalam nama kartu dan nomor  kartu
        if card_name and not card_name.isalpha() and card_number and not card_number.isdigit():
            messagebox.showwarning("Warning", "Tolong inputkan card number dan card name dengan benar")
            return
        
        # Memastikan nama kartu hanya berisi huruf, replace agar spasi terbaca
        if card_name and not card_name.replace(" ", "").isalpha():
            messagebox.showwarning("Warning", "Tolong masukkan huruf saja pada card name")
            return

        # memastikan nomor kartu adalah sebuah angka
        if card_number and not card_number.isdigit():
            messagebox.showwarning("Warning", "Tolong masukkan angka saja pada card number")
            return

        # memastikan banyak angka harus 12 sesuai nomor kartu kredit biasanya
        if card_number and (not card_number.isdigit() or len(card_number) != 12):
            messagebox.showwarning("Warning", "Tolong masukkan angka sebanyak 12 digit pada card number")
            return
        # memastikan nama kartu sepanjang 22 huruf
        if card_name and (not card_name.replace(" ", "").isalpha() or len(card_name) > 22):
            messagebox.showwarning("Warning", "Tolong masukkan huruf sebanyak 22" )
            return
        # memastikan card number card name dan credit limit sudah terisi
        if card_name == "" or card_number == "" or credit_limit == 0:
            messagebox.showwarning("Warning", "Tolong inputkan card number, card name, dan credit limit cc Anda!")
        else:
            self.picture = ImageTk.PhotoImage(file="kartunih.png")
            self.picture_label = tk.Label(root, image=self.picture, bg='#141E46')
            self.picture_label.place(x=645,y=10)

            self.label_nomor_kartu = Label(root, font=("Credit Card", 16), bg='#4f689e')
            self.label_nomor_kartu.place(x=670, y=30)
            self.label_nama_kartu = Label(root, font=("Credit Card", 16), bg='#5b76ad')
            self.label_nama_kartu.place(x=670, y=175)
            self.label_min_payment = Label(root, width=68, bg='#FFF5E0')
            self.label_min_payment.place(x=150, y=140)
            self.label_tagihan = Label(root, text="", font=("Helvetica", 10), bg='#141E46', fg='white')
            self.label_tagihan.place(x=650, y=240)

            self.label_nomor_kartu.config(text=card_number)
            self.label_nama_kartu.config(text=card_name)
            self.label_min_payment.config(text=f"{int(self.credit_limit.get() * 0.1)}")
            self.update_tagihan_label()
        

    def purchase(self):
        pembayaran_barang = simpledialog.askinteger("Purchase", "Masukkan nominal anda:")
        if pembayaran_barang is None:
            messagebox.showinfo("INFO!", "pembayaran barang dibatalkan")
            return
        sisa_kredit = self.credit_limit.get() - self.credit_new
        if pembayaran_barang <= sisa_kredit:
            self.total_tagihan += pembayaran_barang
            self.credit_new += pembayaran_barang
            messagebox.showinfo("Info","Purchase berhasil")
            self.update_tagihan_label()
        else:
            if sisa_kredit == 0 :
                self.check_remain_kredit()
                return 
            
            if pembayaran_barang > sisa_kredit:
                messagebox.showwarning("Error","Purchase melebihi credit limit")
    
    def pay(self):
        pembayaran_tagihan = simpledialog.askinteger("Payment", "Masukkan nominal bayar tagihan:")
        if pembayaran_tagihan is None:
            messagebox.showinfo("INFO!", "pembayaran tagihan dibatalkan")
            return
        min_pay = self.credit_limit.get() * 0.1

        if pembayaran_tagihan >= min_pay:
            if pembayaran_tagihan <= self.total_tagihan:
                self.total_tagihan -= pembayaran_tagihan
                messagebox.showinfo("Info","Pembayaran tagihan Berhasil")
                self.update_tagihan_label()
            else:
                messagebox.showwarning("Warning","Pembayaran melebihi tagihan")
        else:
                messagebox.showerror("Error","Pembayaran dibawah min pembayaran")

    def check_remain_kredit(self):
        sisa_kredit = self.credit_limit.get() - self.credit_new
        if sisa_kredit == 0:
            messagebox.showwarning("Warning",f"Mohon maaf sisa kredit anda pada bulan ini: Rp. {sisa_kredit}")
        else:
            messagebox.showinfo("Remaining Credit", f"Sisa Kredit Anda : Rp.{sisa_kredit}")


    def update_tagihan_label(self):
        self.label_tagihan.config(text=f"Tagihan Kartu Kredit Anda : Rp. {self.total_tagihan}")



root = Tk()
gui = CreditCard(root)
root.mainloop()

