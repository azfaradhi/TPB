from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from databasebarang import DatabaseBarang
import datetime
import os
import random
import qrcode
import cv2
from pyzbar.pyzbar import decode
import numpy as np


# Inisialisasi
date = datetime.datetime.now().date()
menu = DatabaseBarang.menu
namadibeli = []
hargadibeli = []
banyakdibeli = []
iddibeli = []
totaldibeli = []

class Aplikasi:

    def __init__(self,aplikasi2):

        # Frame Atas
        self.frameatas = Frame(aplikasi2, width=1250, height=100, bg='skyblue')
        self.frameatas.grid(row=0,column=0,sticky="NSEW")
        # Frame invoice
        self.framebawah = ttk.Treeview(aplikasi2, column=('c1','c2','c3','c4','c5'), show='headings', height=25)
        self.framebawah.grid(row=1,column=0,sticky="NSEW")
        # Frame tombol
        self.frametombol = Frame(aplikasi2, width=1250, height=70,bg='lightgrey')
        self.frametombol.grid(row=2,column=0,sticky="NSEW")

        # Tanggal hari ini
        self.date1 = Label(self.frameatas, text = (f'Tanggal: {date}'), font = ('arial', "12"), bg='skyblue')
        self.date1.place(x=10,y=10)
        # Label nama pegawai
        self.labelpegawai = Label(self.frameatas, text="Nama kasir: ", font=('arial',12), bg="skyblue")
        self.labelpegawai.place(x=10,y=50)
        # Input nama pegawai
        self.entrynamapegawai = Entry(self.frameatas, width = 10, font=('arial',12))
        self.entrynamapegawai.place(x=105,y=50)
        # Tombol nama pegawai
        self.tombolnamapegawai = Button(self.frameatas, text='OK', width = 0, height=0, command=self.namakasir)
        self.tombolnamapegawai.place(x=205,y=49)
        # Label id barang
        self.labelidbarang = Label(self.frameatas, text="Kode Item: ", font=('arial',12), bg="skyblue")
        self.labelidbarang.place(x=250,y=10)
        # Input id barang
        self.inputidbarang = Entry(self.frameatas, width = 7, font=('arial',12))
        self.inputidbarang.place(x=375,y=10)
        # Tombol id barang
        self.tombolidbarang = Button(self.frameatas, text='🔍', width = 0, height=0, command=self.inputdatakeinvoice)
        self.tombolidbarang.place(x=445,y=9)
        # Output nama barang
        self.outputnamabarang = Label(self.frameatas, text="", font = ("arial", 15),bg='skyblue')
        self.outputnamabarang.place(x=500,y=10)
        # Output harga barang
        self.outputhargabarang = Label(self.frameatas, text="", font = ("arial", 15),bg='skyblue')
        self.outputhargabarang.place(x=500,y=40)

        # Pembuatan frame invoice
        self.framebawah.column("#1", anchor=CENTER)
        self.framebawah.heading("#1", text="Kode Item")
        self.framebawah.column("#2", anchor=CENTER)
        self.framebawah.heading("#2", text="Nama Item")
        self.framebawah.column("#3", anchor=CENTER)
        self.framebawah.heading("#3", text="Kuantitas")
        self.framebawah.column("#4", anchor=CENTER)
        self.framebawah.heading("#4", text="Harga")
        self.framebawah.column("#5", anchor=CENTER)
        self.framebawah.heading("#5", text="Total")
        
        # Total harga
        self.totalbiaya = Label(self.frameatas, text="", font=('arial',14))
        self.totalbiaya.place(x=0,y=600)

        # Tombol selesai
        self.selesaibelanja = Button(self.frametombol, text='Selesai', font=('arial',12), width = 7, height = 2, command=self.selesailanjutbayar)
        self.selesaibelanja.place(x=20,y=10)

        # Tombol edit barang yang dibeli
        self.editinvoice1 =  Button(self.frametombol, text='Edit Barang', font=('arial',12), width= 13, height=2, command=self.editinvoice)
        self.editinvoice1.place(x=125,y=10)

        # Tombol edit barang yang dibeli
        self.baru = Button(self.frametombol, text='New', font=('arial',12), width= 7, height=2, command=self.new)
        self.baru.place(x=285,y=10)

# TAHAP PENAMBAHAN INVOICE

    def namakasir(self):
        self.namapegawai = self.entrynamapegawai.get()
        self.entrynamapegawai.configure(state='disabled')

    def inputdatakeinvoice(self):
        # Cek kondisi
        if len(self.entrynamapegawai.get()) == 0:
            messagebox.showerror("Error", "Tidak ada nama pegawai!")
        else:
            self.invoice_idbarang = self.inputidbarang.get()
            self.cekadadidatabase = False
            for i in range(100):
                if menu[i][0] == self.invoice_idbarang:
                    self.cekadadidatabase = True
                    self.invoice_namabarang = menu[i][1]
                    self.invoice_hargabarang = menu[i][2]
                    # Print nama dan harga barang pada layar
                    self.outputnamabarang.configure(text=f'Nama barang: {self.invoice_namabarang}')
                    self.outputhargabarang.configure(text=f'Harga barang: {self.invoice_hargabarang}')

            # Cek kondisi boolean
            if self.cekadadidatabase == False:
                messagebox.showerror("Error", "Id tidak ada dalam database")
                self.inputidbarang.delete(0,END)
            # Cek kondisi boolean
            if self.cekadadidatabase:
                self.inputidbarang.configure(state='disabled')
                # Label input banyak barang
                self.labelinputbanyakbarang = Label(self.frameatas, text='Banyak barang: ', font=('arial',12), bg='skyblue')
                self.labelinputbanyakbarang.place(x=250,y=40)
                # Entry input banyak barang
                self.entryinputbanyakbarang = Entry(self.frameatas, width = 7, font=('arial',12))
                self.entryinputbanyakbarang.place(x=375,y=40)
                # Tombol input banyak barang
                self.tombolinputbanyakbarang = Button(self.frameatas,text="🛒", width=0, height=0, command=self.tambahkeinvoice)
                self.tombolinputbanyakbarang.place(x=445,y=39)
                # Total harga
                self.totalbiaya = Label(self.frameatas, text="", font=('arial',30), bg='skyblue')
                self.totalbiaya.place(x=1070,y=50)

    # MENAMBAHKAN BARANG DIBELI PADA LAYAR DAN INVOICE
    def tambahkeinvoice(self):
        self.invoice_banyakperbarang = self.entryinputbanyakbarang.get()
        if self.invoice_banyakperbarang.isdigit():
            if int(self.invoice_banyakperbarang) > 0:
                iddibeli.append(self.invoice_idbarang)
                namadibeli.append(self.invoice_namabarang)
                hargadibeli.append(self.invoice_hargabarang)
                banyakdibeli.append(self.invoice_banyakperbarang)
                totaldibeli.append(float(self.invoice_hargabarang)*float(self.invoice_banyakperbarang))
                self.xi = 0
                self.yi = 50
                self.sum = 0

                self.framebawah.insert('', 'end', text="1", values=(str(self.invoice_idbarang),
                                                                        str(self.invoice_namabarang),
                                                                        str(self.invoice_banyakperbarang),
                                                                        str(self.invoice_hargabarang),
                                                                        str(float(self.invoice_hargabarang)*float(self.invoice_banyakperbarang))))
                for i in range(len(totaldibeli)):
                    self.sum += float(totaldibeli[i])

                # Menghitung total biaya
                self.totalbiaya.configure(text=f'{self.sum}')
                # Hapus
                self.inputidbarang.configure(state='normal')
                self.entryinputbanyakbarang.place_forget()
                self.outputnamabarang.configure(text="")
                self.outputhargabarang.configure(text="")
                self.tombolinputbanyakbarang.destroy()
                self.labelinputbanyakbarang.place_forget()
                self.inputidbarang.focus()
                self.inputidbarang.delete(0,END)

            else:
                messagebox.showinfo('Info', 'Invalid')
                self.inputidbarang.configure(state='normal')
                self.labelinputbanyakbarang.place_forget()
                self.entryinputbanyakbarang.place_forget()
                self.tombolinputbanyakbarang.destroy()
                self.inputidbarang.focus()

                
        else:
            messagebox.showinfo('Info', 'Invalid')
            self.labelinputbanyakbarang.place_forget()
            self.entryinputbanyakbarang.place_forget()
            self.tombolinputbanyakbarang.destroy()
            self.inputidbarang.focus()
            self.inputidbarang.configure(state='normal')

    # EDIT BARANG YANG DIBELI
    def editinvoice(self):
        self.editbarang = Toplevel()
        self.editbarang.geometry('350x200')
        self.editbarang.title("Edit Jumlah Barang")
        self.editbarang.resizable(0,0)
        self.labeltanyaidbarang = Label(self.editbarang, text='Id barang: ', font=('arial', 12))
        self.labeltanyaidbarang.place(x=100,y=50)
        self.entrytanyaidbarang = Entry(self.editbarang, width=6, font=('arial', 12))
        self.entrytanyaidbarang.place(x=200,y=53)
        self.tomboltanyaidbarang = Button(self.editbarang, text='🔍',width=0, height=0, command=self.cekidbarang)
        self.tomboltanyaidbarang.place(x=275,y=50)
    def cekidbarang(self):
        self.cekada = True
        for self.i in iddibeli:
            if self.i == self.entrytanyaidbarang.get():
                self.a = iddibeli.index(self.i)
                self.labeleditbanyakbarang = Label(self.editbarang, text='Kuantitas: ', font=('arial', 12))
                self.labeleditbanyakbarang.place(x=100,y=80)
                self.entryeditbanyakbarang = Entry(self.editbarang, width=6, font=('arial', 12))
                self.entryeditbanyakbarang.place(x=200,y=83)
                self.tomboleditbanyakbarang = Button(self.editbarang, text='ok',width=0, height=0, command=self.finishedit)
                self.tomboleditbanyakbarang.place(x=275,y=80)
                self.idyangbaru = iddibeli[self.a]
                self.namayangbaru = namadibeli[self.a]
                self.kuantitasbaru = int(banyakdibeli[self.a])
                self.hargayangbaru = int(hargadibeli[self.a])
                self.cekada = False
        if self.cekada:
            messagebox.showerror("Error", "Invalid")

    def finishedit(self):
        # Cek kondisi
        if len(iddibeli) == 0:
            messagebox.showerror("Error", "Belum ada barang yang dibeli")
        else:
            self.kuantitasidyangdiubah = self.entryeditbanyakbarang.get()
            self.kuantitasbaru = int(self.kuantitasidyangdiubah) - self.kuantitasbaru
            self.totalbaru = (self.kuantitasbaru*self.hargayangbaru)
            if int(self.kuantitasidyangdiubah) < 0:
                messagebox.showerror("Error", "Invalid")
            else:
                if self.kuantitasbaru == 0:
                    pass
                else:
                    namadibeli.append(self.namayangbaru)
                    hargadibeli.append(self.hargayangbaru)
                    banyakdibeli.append(self.kuantitasbaru)
                    iddibeli.append(self.kuantitasbaru)
                    totaldibeli.append(self.totalbaru)
                    self.framebawah.insert('', 'end', text="1", values=(str(self.idyangbaru),
                                                                    str(self.namayangbaru),
                                                                    str(self.kuantitasbaru),
                                                                    str(self.hargayangbaru),
                                                                    str(self.totalbaru)))
                    self.sum = self.sum + self.totalbaru
                    self.totalbiaya.configure(text=f'{self.sum}')

        self.editbarang.destroy()

    # MEMBUAT TRANSAKSI BARU
    def new(self):
        self.totalbiaya.config(text="\t\t\t\t\t\t\t\t\t")
        namadibeli.clear()
        hargadibeli.clear()
        banyakdibeli.clear()
        iddibeli.clear()
        totaldibeli.clear()
        self.entrynamapegawai.delete(0,END)
        self.sum = 0
        self.entrynamapegawai.configure(state='normal')
        self.entrynamapegawai.delete(0,END)
        for self.item in self.framebawah.get_children():
            self.framebawah.delete(self.item)

    
# TAHAP PEMBAYARAN


    def selesailanjutbayar(self):
        # Cek Kondisi
        if len(iddibeli) == 0:
            messagebox.showerror("Error", "Tidak ada barang yang dibeli")
        else:
            self.pagebayar = Toplevel()
            self.pagebayar.geometry('525x350')
            self.pagebayar.config(bg='skyblue')
            self.pagebayar.title("Bayar Penjualan Pos")
            self.pagebayar.resizable(0,0)

            # Label harga akhir
            self.labelhargakahir = Label(self.pagebayar, text= self.sum, font=('arial',18), bg='skyblue')
            self.labelhargakahir.place(x=400,y=40)
            #Label pilih non tunai
            self.labelpilihnontunai = Label(self.pagebayar, text='Metode Pembayaran: ', font=('arial',12), bg='skyblue')
            self.labelpilihnontunai.place(x=200,y=100)      
            # Opsi Pembayaran
            self.opsi = ['TUNAI',
                        'KREDIT',
                        'LINK AJA', 
                        'MANDIRI DEBIT', 
                        'OVO', 
                        'QRIS BCA', 
                        'SHOPEEPAY']
            self.dropdown = ttk.Combobox(self.pagebayar,values=self.opsi,width = 15)
            self.dropdown.place(x=370,y=100)

            # Tombol fiks pembayaran
            self.tombolfikspembayaran = Button(self.pagebayar, text='🔍', width=0, height=0, command=self.fiks)
            self.tombolfikspembayaran.place(x=500,y=99)

    def fiks(self,*args,**kwargs):
        self.metodepembayaran = self.dropdown.get()
        # Cek Kondisi
        if self.metodepembayaran == "TUNAI":
            self.bayardengantunai()
        if self.metodepembayaran == "KREDIT":
            self.bayardengankredit()
        if self.metodepembayaran == "LINK AJA":
            self.fotoqris()
        if self.metodepembayaran == "MANDIRI DEBIT":
            self.bayardengandebit()
        if self.metodepembayaran == "OVO":
            self.fotoqris()
        if self.metodepembayaran == "QRIS BCA":
            self.fotoqris()
        if self.metodepembayaran == "SHOPEEPAY":
            self.fotoqris()

    # MENGELUARKAN FOTO QRIS
    def fotoqris(self):
        self.cp = cv2.VideoCapture(0)
        self.cp.set(3,360)
        self.cp.set(4,480)

        self.cek = True
        while self.cek:
            self.success,self.frame = self.cp.read()

            if not self.success:
                break

            for self.code in decode(self.frame):
                if (self.code.type == "QRCODE") and (self.code.data.decode('utf-8') == "Foto\qrisbukarimartpng.png"):
                    self.cekbenar = True
                    self.cek = False
                    break
            cv2.imshow('Pembayaran Qris',self.frame)
            cv2.waitKey(1)


        
        if self.cekbenar:
            self.labelpembayaransukses = Label(self.pagebayar, text= 'Pembayaran Sukses!', font=('arial', 12), bg='skyblue')
            self.labelpembayaransukses.place(x=200,y=260)
            # Tombol print struk
            self.tombolprintstruk = Button(self.pagebayar, text="Print Struk", width = 10, height = 1, command=self.buatbill)
            self.tombolprintstruk.place(x=230,y=300)
            # Tombol kembali
            self.tombolprintstruk = Button(self.pagebayar, text="Kembali", width = 7, height = 1, command=self.selesai)
            self.tombolprintstruk.place(x=380,y=300)
    
    def bayardengantunai(self):
        # Label Bayar Tunai
        self.labelbayartunai = Label(self.pagebayar, text="Bayar tunai: ", font=('arial', 12), bg='skyblue')
        self.labelbayartunai.place(x=200,y=140)
        # Entry Bayar Tunai
        self.entrybayartunai = Entry(self.pagebayar, width=12, font=('arial', 12))
        self.entrybayartunai.place(x=370,y=140)
        # Tombol fiks tunai
        self.tombolfikstunai = Button(self.pagebayar, text='🔍', width=0, height=0, command=self.bayardengantunai2)
        self.tombolfikstunai.place(x=500,y=139)

    def bayardengantunai2(self):
        # Cek kondisi
        if len(self.entrybayartunai.get()) == 0:
            messagebox.showerror("Error","Tidak ada input tunai!")
            self.pagebayar.destroy()

        else:
            self.kembalian = int(self.entrybayartunai.get()) - self.sum
            if self.kembalian < 0:
                messagebox.showerror("Error", "Uang tidak cukup")
                self.pagebayar.destroy()
            # Label Kembalian
            self.labelkembalian = Label(self.pagebayar, text="Kembalian: ", font=('arial', 12), bg='skyblue')
            self.labelkembalian.place(x=200,y=180)
            # Label Kembalian
            self.nilaikembalian = Label(self.pagebayar, text= self.kembalian, font=('arial', 12), bg='skyblue')
            self.nilaikembalian.place(x=370,y=180)
            # Label pembayaran sukses
            self.labelpembayaransukses = Label(self.pagebayar, text= 'Pembayaran Sukses!', font=('arial', 12), bg='skyblue')
            self.labelpembayaransukses.place(x=200,y=260)
            # Tombol print struk
            self.tombolprintstruk = Button(self.pagebayar, text="Print Struk", width = 10, height = 1, command=self.buatbill)
            self.tombolprintstruk.place(x=230,y=300)
            # Tombol kembali
            self.tombolprintstruk = Button(self.pagebayar, text="New", width = 7, height = 1, command=self.selesai)
            self.tombolprintstruk.place(x=380,y=300)
    
    def bayardengankredit(self):
        # Label Bayar Kredit
        self.labelbayarkredit = Label(self.pagebayar, text="Bayar kredit: ", font=('arial', 12), bg='skyblue')
        self.labelbayarkredit.place(x=200,y=140)
        # Entry Bayar kredit
        self.entrybayarkredit = Entry(self.pagebayar, width=12, font=('arial', 12))
        self.entrybayarkredit.place(x=370,y=140)
        # Tombol Bayar Kredit
        self.tombolbayarkredit = Button(self.pagebayar, text="🔍", width = 1, height = 1, command=self.konfirmasipembayarankredit)
        self.tombolbayarkredit.place(x=500,y=140)

    def konfirmasipembayarankredit(self):
        # Cek kondisi
        if len(self.entrybayarkredit.get()) == 0:
            messagebox.showerror("Error","Tidak ada input kartu kredit!")
            self.pagebayar.destroy()

        else:
            # Label konfirmasi pembayaran
            self.konfirmasipembayaran1 = Label(self.pagebayar, text="Konfirmasi?", font=('arial', 12), bg='skyblue')
            self.konfirmasipembayaran1.place(x=200,y=200)
            # Tombol konfirmasi pembayaran (ya)
            self.tombolkonfirmasipembayaranya = Button(self.pagebayar, text= 'Ya', width = 3, height = 1, command=self.selesaikonfirmasibayar)
            self.tombolkonfirmasipembayaranya.place(x=370,y=200)
            # Tombol konfirmasi pembayaran (tidak)
            self.tombolkonfirmasipembayarantidak = Button(self.pagebayar, text= 'Tidak', width = 4, height = 1, command=self.tidakjadimetodebayar)
            self.tombolkonfirmasipembayarantidak.place(x=420,y=200)

    def bayardengandebit(self):
        # Label Bayar debit
        self.labelbayardebit = Label(self.pagebayar, text="Bayar Debit: ", font=('arial', 12), bg='skyblue')
        self.labelbayardebit.place(x=200,y=140)
        # Entry Bayar debit
        self.entrybayardebit = Entry(self.pagebayar, width=12, font=('arial', 12))
        self.entrybayardebit.place(x=370,y=140)
        # Tombol Bayar debit
        self.tombolbayardebit = Button(self.pagebayar, text="🔍", width = 1, height = 1, command=self.konfirmasipembayarandebit)
        self.tombolbayardebit.place(x=500,y=140)

    def konfirmasipembayarandebit(self):
        # Cek kondisi
        if len(self.entrybayardebit.get()) == 0:
            messagebox.showerror("Error","Tidak ada input kartu debit!")
            self.pagebayar.destroy()

        else:
            # Label konfirmasi pembayaran
            self.konfirmasipembayaran1 = Label(self.pagebayar, text="Konfirmasi?", font=('arial', 12), bg='skyblue')
            self.konfirmasipembayaran1.place(x=200,y=200)
            # Tombol konfirmasi pembayaran (ya)
            self.tombolkonfirmasipembayaranya = Button(self.pagebayar, text= 'Ya', width = 3, height = 1, command=self.selesaikonfirmasibayar)
            self.tombolkonfirmasipembayaranya.place(x=370,y=200)
            # Tombol konfirmasi pembayaran (tidak)
            self.tombolkonfirmasipembayarantidak = Button(self.pagebayar, text= 'Tidak', width = 4, height = 1, command=self.tidakjadimetodebayar)
            self.tombolkonfirmasipembayarantidak.place(x=420,y=200)

    def konfirmasipembayaran(self):
        # Label konfirmasi pembayaran
        self.konfirmasipembayaran1 = Label(self.pagebayar, text="Konfirmasi?", font=('arial', 12), bg='skyblue')
        self.konfirmasipembayaran1.place(x=200,y=200)
        # Tombol konfirmasi pembayaran (ya)
        self.tombolkonfirmasipembayaranya = Button(self.pagebayar, text= 'Ya', width = 3, height = 1, command=self.selesaikonfirmasibayar)
        self.tombolkonfirmasipembayaranya.place(x=370,y=200)
        # Tombol konfirmasi pembayaran (tidak)
        self.tombolkonfirmasipembayarantidak = Button(self.pagebayar, text= 'Tidak', width = 4, height = 1, command=self.tidakjadimetodebayar)
        self.tombolkonfirmasipembayarantidak.place(x=420,y=200)
    
    def selesaikonfirmasibayar(self):
        # Label pembayaran sukses
        self.labelpembayaransukses = Label(self.pagebayar, text= 'Pembayaran Sukses!', font=('arial', 12), bg='skyblue')
        self.labelpembayaransukses.place(x=200,y=260)
        # Tombol print struk
        self.tombolprintstruk = Button(self.pagebayar, text="Print Struk", width = 10, height = 1, command=self.buatbill)
        self.tombolprintstruk.place(x=230,y=300)
        # Tombol kembali
        self.tombolprintstruk = Button(self.pagebayar, text="Kembali", width = 7, height = 1, command=self.selesai)
        self.tombolprintstruk.place(x=380,y=300)

    # Tombol tidak jadi bayar
    def tidakjadimetodebayar(self):
        self.pagebayar.destroy()

    # Tombol selesai
    def tombolselesai(self):
        self.pagebayar.destroy()

    # PEMMBUATAN STRUK
    def buatbill(self,*args,**kwargs):
        namakasir = self.entrynamapegawai.get()
        saveke = "Struk/temp"
        if not os.path.exists(saveke):
            os.makedirs(saveke)
        # TEMPLATE STRUK BIAYA
        toko = "\t\t\t\t\t\tBUKARI MART\n"
        alamat = "\t\t\t\tJl Caringin No 20 Sayang - Jatinangor\n"
        bm = f"\tBM-POS/{date}/{random.randrange(0,1000)}"
        dt = "\t\t\t\t\t" + str(date) + "\n"
        ksr = "\t" + f"Ksr: {namakasir}"

        table_header = "\n\n\t-----------------------------------------------------------------\n\tSN.\tproduk\t\t\t\t\tKuantitas\tJumlah Harga\n\t-----------------------------------------------------------------"
        final = toko + alamat + bm + dt + ksr + table_header

        file_name = str(saveke) + str(random.randrange(5000, 10000)) + ".rtf"
        f = open(file_name, "w")
        f.write(final)

        r = 1 
        i = 0
        for t in namadibeli:
            f.write("\n\t" + str(r) + "\t" + str(namadibeli[i] + "................................")[:32] + "\t\t" + str(banyakdibeli[i]) + "\t\t" +str(hargadibeli[i])) 
            i+=1 
            r+=1
        f.write("\n\n\tTotal: Rp " + str(self.sum))
        if self.metodepembayaran == "TUNAI":
            f.write("\n\n\tTunai: " + str(self.entrybayartunai.get()))
            f.write("\n\n\tKembalian: " + str(self.kembalian))
        f.write("\n\n\tMetode pembayaran: " + str(self.metodepembayaran))
        f.write("\n\n\t\t\t\t\t  IG: BUMARTOFFICIAL")
        f.write("\n\t\t\t\t\t   0895-3237-29200")
        f.write("\n\n\t\t\t\t\t Kami Melayani Kebutuhan")
        f.write("\n\t\t\t\t\tHarian Sembako dan HORECA")
        f.write("\n\n\t\t\t\t   Terima Kasih Atas Kunjungannya")
        f.write("\n\t\t\t\t     Belanja Senang Harga Menang")
        f.close()
        messagebox.showinfo("ID", f"Sukses Disimpan\n No Trx {bm}")

    
    def selesai(self):
        self.pagebayar.destroy()

image = "Aplikasi/qrisbukarimartpng.png"
app = Tk()
app.title("Bukari Mart")
b = Aplikasi(app)
app.geometry('1250x700')
app.rowconfigure(0, weight=4)
app.columnconfigure(0, weight=1)
app.mainloop()