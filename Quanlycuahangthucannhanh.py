
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import simpledialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# danh sach dữ lieu
danh_sach_nhan_vien = []
drink_list = []
invoice_list = []

# Tạo dữ liệu người dùng (mật khẩu cho mỗi người dùng)
users = {
    'admin': 'admin',
    'user1': 'password1'
}

def login_window():
    # Tạo cửa sổ đăng nhập
    login_root = tk.Tk()
    login_root.title("Đăng Nhập")
    login_root.geometry('400x250')

    # Tạo các widget cho cửa sổ đăng nhập
    tk.Label(login_root, text="Tên Đăng Nhập:", font=("Arial", 12)).pack(pady=10)
    username_entry = tk.Entry(login_root, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(login_root, text="Mật Khẩu:", font=("Arial", 12)).pack(pady=10)
    password_entry = tk.Entry(login_root, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        # Kiểm tra thông tin đăng nhập
        if username in users and users[username] == password:
            login_root.destroy()  # Đóng cửa sổ đăng nhập
            main_window()  # Mở cửa sổ chính
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu sai!")

    # Nút đăng nhập
    tk.Button(login_root, text="Đăng Nhập", command=login, width=20, height=2, bg="#98a77c").pack(pady=20)

    login_root.mainloop()

def main_window():
    root = tk.Tk()

    root.title("Hệ Thống Quản Lý Cửa Hàng Thư Ăn Nhanh")
    root.geometry('1100x900')

    button_frame = tk.Frame(root, height=50, bg="lightgreen")
    button_frame.pack(side="top", fill="x")

    HienThi_frame = tk.Frame(root, bg="white")
    HienThi_frame.pack(side="top", fill="both", expand=True)

    # Buttons

    tk.Button(button_frame, text="Nhân Viên", width=20, height=2,fg='white',font=("Bahnschrift SemiLight SemiConde",12, "bold"), bg="dodgerblue", command=lambda: hien_thi_nhan_vien(HienThi_frame)).grid(row=0,column=0,padx=5,pady=5,stick="e")
    tk.Button(button_frame, text="Danh Sách Thức Ăn", width=20, height=2,fg='white',font=("Bahnschrift SemiLight SemiConde",12, "bold") ,bg="dodgerblue", command=lambda: hien_thi_thuc_an(HienThi_frame)).grid(row=0,column=1,padx=5,pady=5,stick="e")
    tk.Button(button_frame, text="Hoá Đơn", width=20, height=2,fg='white',font=("Bahnschrift SemiLight SemiConde",12, "bold"), bg="dodgerblue", command=lambda: hien_thi_hoa_don(HienThi_frame)).grid(row=0,column=2,padx=5,pady=5,stick="e")
    tk.Button(button_frame, text="Tính Doanh Thu", width=20, height=2,fg='white',font=("Bahnschrift SemiLight SemiConde",12, "bold"), bg="dodgerblue", command=lambda: hien_thi_doanh_thu(HienThi_frame)).grid(row=0,column=3,padx=5,pady=5,stick="e")
    tk.Button(button_frame, text="Quản lý kho", width=20, height=2, fg='white',font=("Bahnschrift SemiLight SemiConde", 12, "bold"), bg="dodgerblue",command=lambda: hien_thi_quan_ly_kho(HienThi_frame)).grid(row=0, column=4, padx=5, pady=5, stick="e")
    root.mainloop()


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Nhân Viên
# Danh sách nhân viên mẫu
danh_sach_nhan_vien = [
    {"Mã Nhân Viên": "NV001", "Họ Tên": "Nguyễn Văn A", "CCCD": "123456789", "Số Giờ Làm": "160", "Chức Vụ": "Nhân Viên", "Lương Cơ Bản": 20000, "Tổng Lương": 3200000},
    {"Mã Nhân Viên": "NV002", "Họ Tên": "Trần Thị B", "CCCD": "987654321", "Số Giờ Làm": "180", "Chức Vụ": "Nhân Viên", "Lương Cơ Bản": 20000, "Tổng Lương": 3600000},
    {"Mã Nhân Viên": "NV003", "Họ Tên": "Phạm Minh C", "CCCD": "135792468", "Số Giờ Làm": "150", "Chức Vụ": "Quản Lý", "Lương Cơ Bản": 50000, "Tổng Lương": 7500000},
    {"Mã Nhân Viên": "NV004", "Họ Tên": "Lê Thị D", "CCCD": "246813579", "Số Giờ Làm": "170", "Chức Vụ": "Nhân Viên", "Lương Cơ Bản": 20000, "Tổng Lương": 3400000},
    {"Mã Nhân Viên": "NV005", "Họ Tên": "Võ Quốc E", "CCCD": "987651234", "Số Giờ Làm": "160", "Chức Vụ": "Quản Lý", "Lương Cơ Bản": 50000, "Tổng Lương": 8000000}
]

def xoa_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Quản Lý Nhân Viên
def hien_thi_nhan_vien(HienThi_frame):
    # Xóa frame cũ
    xoa_frame(HienThi_frame)

    # Tiêu đề
    tk.Label(HienThi_frame, text="Quản Lý Nhân Viên", font=("Arial Black", 17, "bold"), fg="blue", bg="lightyellow", relief="groove", bd=9).pack(pady=10)

    # Tạo bảng Treeview
    columns = ("Mã Nhân Viên", "Họ Tên", "CCCD", "Số Giờ Làm", "Chức Vụ", "Lương Cơ Bản", "Tổng Lương")
    tree = ttk.Treeview(HienThi_frame, columns=columns, show="headings", height=20)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")

    tree.pack(pady=10, fill="both", expand=True)

    # Cập nhật danh sách Treeview
    def cap_nhat_danh_sach_nhan_vien():
        tree.delete(*tree.get_children())
        for nhan_vien in danh_sach_nhan_vien:
            tree.insert("", "end", values=(
                nhan_vien["Mã Nhân Viên"],
                nhan_vien["Họ Tên"],
                nhan_vien["CCCD"],
                nhan_vien["Số Giờ Làm"],
                nhan_vien["Chức Vụ"],
                nhan_vien["Lương Cơ Bản"],
                nhan_vien["Tổng Lương"]
            ))

    # Thêm nhân viên
    def them_nhan_vien():
        def luu_nhan_vien():
            ma_nv = entry_ma_nv.get()
            ten_nv = entry_ten_nv.get()
            cccd = entry_cccd.get()
            so_gio_lam = entry_so_gio_lam.get()
            chuc_vu = combo_chuc_vu.get()

            if not ma_nv or not ten_nv or not cccd or not so_gio_lam or not chuc_vu:
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
                return

            # Tính lương cơ bản và tổng lương
            luong_co_ban = 20000 if chuc_vu == "Nhân Viên" else 50000
            tong_luong = int(so_gio_lam) * luong_co_ban

            # Thêm nhân viên vào danh sách
            danh_sach_nhan_vien.append({
                "Mã Nhân Viên": ma_nv,
                "Họ Tên": ten_nv,
                "CCCD": cccd,
                "Số Giờ Làm": so_gio_lam,
                "Chức Vụ": chuc_vu,
                "Lương Cơ Bản": luong_co_ban,
                "Tổng Lương": tong_luong
            })

            cap_nhat_danh_sach_nhan_vien()
            them_nv_window.destroy()
            messagebox.showinfo("Thành Công", "Nhân Viên đã được thêm!")

        them_nv_window = tk.Toplevel()
        them_nv_window.title("Thêm Nhân Viên")
        them_nv_window.geometry("400x400")

        tk.Label(them_nv_window, text="Mã Nhân Viên:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
        entry_ma_nv = tk.Entry(them_nv_window)
        entry_ma_nv.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(them_nv_window, text="Họ Tên:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
        entry_ten_nv = tk.Entry(them_nv_window)
        entry_ten_nv.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(them_nv_window, text="CCCD:").grid(row=2, column=0, pady=5, padx=5, sticky="w")
        entry_cccd = tk.Entry(them_nv_window)
        entry_cccd.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(them_nv_window, text="Số Giờ Làm:").grid(row=3, column=0, pady=5, padx=5, sticky="w")
        entry_so_gio_lam = tk.Entry(them_nv_window)
        entry_so_gio_lam.grid(row=3, column=1, pady=5, padx=5)

        tk.Label(them_nv_window, text="Chức Vụ:").grid(row=4, column=0, pady=5, padx=5, sticky="w")
        combo_chuc_vu = ttk.Combobox(them_nv_window, values=["Nhân Viên", "Quản Lý"], state="readonly")
        combo_chuc_vu.grid(row=4, column=1, pady=5, padx=5)

        tk.Button(them_nv_window, text="Lưu Nhân Viên", command=luu_nhan_vien).grid(row=5, column=0, columnspan=2, pady=10)

    # Xóa nhân viên
    def xoa_nhan_vien():
        selected = tree.selection()
        if not selected:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên để xóa!")
            return

        for item in selected:
            ma_nv = tree.item(item, "values")[0]
            danh_sach_nhan_vien[:] = [nv for nv in danh_sach_nhan_vien if nv["Mã Nhân Viên"] != ma_nv]

        cap_nhat_danh_sach_nhan_vien()
        messagebox.showinfo("Thành Công", "Nhân Viên đã được xóa!")

    # Sửa nhân viên
    def sua_nhan_vien():
        selected = tree.selection()
        if not selected:
            messagebox.showerror("Lỗi", "Vui lòng chọn nhân viên để sửa!")
            return

        item = selected[0]
        ma_nv = tree.item(item, "values")[0]
        nhan_vien = next((nv for nv in danh_sach_nhan_vien if nv["Mã Nhân Viên"] == ma_nv), None)

        if nhan_vien:
            def luu_sua():
                nhan_vien["Họ Tên"] = entry_ten_nv.get()
                nhan_vien["CCCD"] = entry_cccd.get()
                nhan_vien["Số Giờ Làm"] = entry_so_gio_lam.get()
                nhan_vien["Chức Vụ"] = combo_chuc_vu.get()

                luong_co_ban = 20000 if nhan_vien["Chức Vụ"] == "Nhân Viên" else 50000
                nhan_vien["Lương Cơ Bản"] = luong_co_ban
                nhan_vien["Tổng Lương"] = int(nhan_vien["Số Giờ Làm"]) * luong_co_ban

                cap_nhat_danh_sach_nhan_vien()
                sua_nv_window.destroy()
                messagebox.showinfo("Thành Công", "Nhân Viên đã được sửa!")

            sua_nv_window = tk.Toplevel()
            sua_nv_window.title("Sửa Nhân Viên")
            sua_nv_window.geometry("400x400")

            tk.Label(sua_nv_window, text="Họ Tên:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
            entry_ten_nv = tk.Entry(sua_nv_window)
            entry_ten_nv.insert(0, nhan_vien["Họ Tên"])
            entry_ten_nv.grid(row=0, column=1, pady=5, padx=5)

            tk.Label(sua_nv_window, text="CCCD:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
            entry_cccd = tk.Entry(sua_nv_window)
            entry_cccd.insert(0, nhan_vien["CCCD"])
            entry_cccd.grid(row=1, column=1, pady=5, padx=5)

            tk.Label(sua_nv_window, text="Số Giờ Làm:").grid(row=2, column=0, pady=5, padx=5, sticky="w")
            entry_so_gio_lam = tk.Entry(sua_nv_window)
            entry_so_gio_lam.insert(0, nhan_vien["Số Giờ Làm"])
            entry_so_gio_lam.grid(row=2, column=1, pady=5, padx=5)

            tk.Label(sua_nv_window, text="Chức Vụ:").grid(row=3, column=0, pady=5, padx=5, sticky="w")
            combo_chuc_vu = ttk.Combobox(sua_nv_window, values=["Nhân Viên", "Quản Lý"], state="readonly")
            combo_chuc_vu.set(nhan_vien["Chức Vụ"])
            combo_chuc_vu.grid(row=3, column=1, pady=5, padx=5)

            tk.Button(sua_nv_window, text="Lưu Sửa", command=luu_sua).grid(row=4, column=0, columnspan=2, pady=10)

    # Tìm kiếm nhân viên
    def tim_kiem_nhan_vien():
        keyword = tk.simpledialog.askstring("Tìm Kiếm", "Nhập Mã Nhân Viên:")
        if keyword:
            tree.delete(*tree.get_children())
            for nhan_vien in danh_sach_nhan_vien:
                if keyword.lower() in nhan_vien["Mã Nhân Viên"].lower():
                    tree.insert("", "end", values=(
                        nhan_vien["Mã Nhân Viên"],
                        nhan_vien["Họ Tên"],
                        nhan_vien["CCCD"],
                        nhan_vien["Số Giờ Làm"],
                        nhan_vien["Chức Vụ"],
                        nhan_vien["Lương Cơ Bản"],
                        nhan_vien["Tổng Lương"]
                    ))

    # Các nút chức năng
    button_frame = tk.Frame(HienThi_frame)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Thêm Nhân Viên", command=them_nhan_vien, width=20, font=("Bahnschrift SemiLight SemiConde",13, "bold"), bg="lightgreen").grid(row=0, column=0, padx=5)
    tk.Button(button_frame, text="Xóa Nhân Viên", command=xoa_nhan_vien, width=20,font=("Bahnschrift SemiLight SemiConde",13, "bold") ,bg="lightcoral").grid(row=0, column=1, padx=5)
    tk.Button(button_frame, text="Sửa Nhân Viên", command=sua_nhan_vien, width=20,font=("Bahnschrift SemiLight SemiConde",13, "bold") ,bg="lightblue").grid(row=0, column=2, padx=5)
    tk.Button(button_frame, text="Tìm Kiếm", command=tim_kiem_nhan_vien, width=20,font=("Bahnschrift SemiLight SemiConde",13, "bold") ,bg="lightyellow").grid(row=0, column=3, padx=5)

    # Hiển thị danh sách ban đầu
    cap_nhat_danh_sach_nhan_vien()

def xoa_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Thức Ăn
drink_list = [{"Mã Thức Ăn": "TA001", "Tên Thức Ăn": "Gà rán", "Giá Thức Ăn(VNĐ)": 35000},
    {"Mã Thức Ăn": "TA002", "Tên Thức Ăn": "Burger Zinger", "Giá Thức Ăn(VNĐ)": 20000},
    {"Mã Thức Ăn": "TA003", "Tên Thức Ăn": "Nước ngọt", "Giá Thức Ăn(VNĐ)": 20000},
    {"Mã Thức Ăn": "TA004", "Tên Thức Ăn": "Khoai tây chiên", "Giá Thức Ăn(VNĐ)": 15000},
    {"Mã Thức Ăn": "TA005", "Tên Thức Ăn": "Mì ý", "Giá Thức Ăn(VNĐ)": 45000},
]

def hien_thi_thuc_an(HienThi_frame):
    # Xóa frame cũ
    for widget in HienThi_frame.winfo_children():
        widget.destroy()

    # Tạo tab control
    tab_control = ttk.Notebook(HienThi_frame)
    tab_control.pack(expand=1, fill="both")

    # Tạo tab "Quản Lý Thức Ăn"
    tab_quan_ly = ttk.Frame(tab_control)
    tab_control.add(tab_quan_ly, text="Quản Lý Thức Ăn")

    # Tạo tab "Danh Sách Thức Ăn"
    tab_danh_sach = ttk.Frame(tab_control)
    tab_control.add(tab_danh_sach, text="Danh Sách Thức Ăn")

    # ----- Nội dung Tab "Quản Lý Thức Ăn" -----
    ttk.Label(tab_quan_ly, text="Quản Lý Thức Ăn", font=("Helvetica", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    # Các trường nhập liệu
    ttk.Label(tab_quan_ly, text="Mã Thức Ăn:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    Mahang = ttk.Entry(tab_quan_ly, width=30)
    Mahang.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(tab_quan_ly, text="Tên Thức Ăn:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    TenN = ttk.Entry(tab_quan_ly, width=30)
    TenN.grid(row=2, column=1, padx=10, pady=5)

    ttk.Label(tab_quan_ly, text="Giá (VNĐ):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    GiaN = ttk.Entry(tab_quan_ly, width=30)
    GiaN.grid(row=3, column=1, padx=10, pady=5)

    # Nút "Thêm Thức Ăn"
    def them_thuc_an():
        if not Mahang.get() or not TenN.get() or not GiaN.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        try:
            int(GiaN.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Giá thức ăn phải là số!")
            return
        drink_list.append({
            "Mã Thức Ăn": Mahang.get(),
            "Tên Thức Ăn": TenN.get(),
            "Giá Thức Ăn(VNĐ)": GiaN.get()
        })
        cap_nhat_danh_sach()
        Mahang.delete(0, tk.END)
        TenN.delete(0, tk.END)
        GiaN.delete(0, tk.END)
        messagebox.showinfo("Thành Công", "Thức Ăn đã được thêm!")

    ttk.Button(tab_quan_ly, text="Thêm Thức Ăn", command=them_thuc_an).grid(row=4, column=0, columnspan=2, pady=10)

    # ----- Nội dung Tab "Danh Sách Thức Ăn" -----
    ttk.Label(tab_danh_sach, text="Danh Sách Thức Ăn", font=("Helvetica", 18, "bold")).pack(pady=10)
    danh_sach_thuc_an = tk.Listbox(tab_danh_sach, font=("Helvetica", 12), width=80, height=20)
    danh_sach_thuc_an.pack(padx=10, pady=10)

    # Nút "Xóa Thức Ăn"
    def xoa_thuc_an():
        selected_index = danh_sach_thuc_an.curselection()
        if not selected_index:
            messagebox.showerror("Lỗi", "Vui lòng chọn thức ăn để xóa!")
            return
        del drink_list[selected_index[0]]
        cap_nhat_danh_sach()
        messagebox.showinfo("Thành Công", "Thức Ăn đã được xóa!")

    ttk.Button(tab_danh_sach, text="Xóa Thức Ăn", command=xoa_thuc_an).pack(pady=10)

    # Hàm cập nhật danh sách
    def cap_nhat_danh_sach():
        danh_sach_thuc_an.delete(0, tk.END)
        for thuc_an in drink_list:
            try:
                gia_thuc_an = "{:,.0f}".format(int(thuc_an["Giá Thức Ăn(VNĐ)"])).replace(",", ".")
            except ValueError:
                gia_thuc_an = "Không hợp lệ"
            danh_sach_thuc_an.insert(
                tk.END, f"{thuc_an['Mã Thức Ăn']} - {thuc_an['Tên Thức Ăn']} - {gia_thuc_an} VNĐ"
            )

    cap_nhat_danh_sach()

kho_hang=[
        {"Tên Thức Ăn": "Gà Rán", "Số Lượng": 50},
        {"Tên Thức Ăn": "Khoai Tây Chiên", "Số Lượng": 100},
        {"Tên Thức Ăn": "Nước Ngọt", "Số Lượng": 200}
]

# Function to manage stock (inventory)
def kiem_tra_kho(selected_items, so_luong):
    global kho_hang
    kho = {item['Tên Thức Ăn']: item['Số Lượng'] for item in kho_hang}

    for idx, qty in zip(selected_items, so_luong):
        ten_mon = kho_hang[idx]["Tên Thức Ăn"]
        so_luong_kho = kho.get(ten_mon, 0)

        # In ra để kiểm tra
        print(f"Tên món: {ten_mon}, Số lượng yêu cầu: {qty}, Số lượng trong kho: {so_luong_kho}")
        if qty > so_luong_kho:
            messagebox.showwarning("Cảnh báo", f"Số lượng {ten_mon} bán ra vượt quá số lượng trong kho!")
            return False, ten_mon, so_luong_kho

    return True, "", 0


def hien_thi_quan_ly_kho(HienThi_frame):
    clear_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Quản Lý Kho", font=("Arial", 17, "bold"), fg="blue", bg="lightyellow",
             relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    def cap_nhat_kho():
        ten_thuc_an = thuc_an_combobox.get()
        so_luong_nhap = int(so_luong_nhap_entry.get())

        # Check if the item already exists in the inventory
        thuc_an = next((item for item in kho_hang if item['Tên Thức Ăn'] == ten_thuc_an), None)
        if thuc_an:
            thuc_an['Số Lượng'] += so_luong_nhap  # Update existing item quantity
        else:
            # Add new item to the inventory if it doesn't exist
            kho_hang.append({"Tên Thức Ăn": ten_thuc_an, "Số Lượng": so_luong_nhap})

        messagebox.showinfo("Thành Công", f"Đã nhập thêm {so_luong_nhap} {ten_thuc_an} vào kho!")
        cap_nhat_danh_sach_kho()  # Update the stock list UI

    # Add new item to inventory
    def them_thuc_an_moi():
        ten_thuc_an_moi = ten_thuc_an_moi_entry.get()
        so_luong_moi = int(so_luong_moi_entry.get())
        if ten_thuc_an_moi and so_luong_moi:
            kho_hang.append({"Tên Thức Ăn": ten_thuc_an_moi, "Số Lượng": so_luong_moi})
            messagebox.showinfo("Thành Công", f"Đã thêm mới {ten_thuc_an_moi} với số lượng {so_luong_moi} vào kho!")
            cap_nhat_danh_sach_kho()  # Update the stock list UI
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")

    # Update stock list view
    def cap_nhat_danh_sach_kho():
        kho_listbox.delete(0, tk.END)
        for item in kho_hang:
            kho_listbox.insert(tk.END, f"{item['Tên Thức Ăn']} | Số Lượng: {item['Số Lượng']}")

    # Add components to the UI
    tk.Label(HienThi_frame, text="Chọn Thức Ăn:", relief="solid", bd=2).grid(row=1, column=0, pady=5)
    thuc_an_combobox = ttk.Combobox(HienThi_frame, values=[item['Tên Thức Ăn'] for item in kho_hang])
    thuc_an_combobox.grid(row=1, column=1, pady=5)

    tk.Label(HienThi_frame, text="Nhập Số Lượng:", relief="solid", bd=2).grid(row=2, column=0, pady=5)
    so_luong_nhap_entry = tk.Entry(HienThi_frame)
    so_luong_nhap_entry.grid(row=2, column=1, pady=5)

    # For new item
    tk.Label(HienThi_frame, text="Tên Thức Ăn Mới:", relief="solid", bd=2).grid(row=3, column=0, pady=5)
    ten_thuc_an_moi_entry = tk.Entry(HienThi_frame)
    ten_thuc_an_moi_entry.grid(row=3, column=1, pady=5)

    tk.Label(HienThi_frame, text="Số Lượng Mới:", relief="solid", bd=2).grid(row=4, column=0, pady=5)
    so_luong_moi_entry = tk.Entry(HienThi_frame)
    so_luong_moi_entry.grid(row=4, column=1, pady=5)

    tk.Button(HienThi_frame, text="Cập Nhật Kho", command=cap_nhat_kho, width=20, height=2).grid(row=5, column=0, columnspan=2, pady=10)
    tk.Button(HienThi_frame, text="Thêm Thức Ăn Mới", command=them_thuc_an_moi, width=20, height=2).grid(row=6, column=0, columnspan=2, pady=10)

    kho_listbox = tk.Listbox(HienThi_frame, width=60, height=10)
    kho_listbox.grid(row=7, column=0, columnspan=2, pady=10)

    cap_nhat_danh_sach_kho()  # Initial list update


# Hoá Đơn
def hien_thi_hoa_don(HienThi_frame):
    clear_frame(HienThi_frame)
    tk.Label(HienThi_frame, text="Quản Lý Hoá Đơn", font=("Arial", 17, "bold"), fg="blue", bg="lightyellow", relief="groove", bd=9).grid(row=0, column=0, columnspan=4, pady=10)

    ten_khach_hang = tk.Entry(HienThi_frame)
    tk.Label(HienThi_frame, text="Tên Khách Hàng:", relief="solid", bd=2).grid(row=1, column=0, pady=5)
    ten_khach_hang.grid(row=1, column=1, pady=5)

    nhan_vien_combobox = ttk.Combobox(HienThi_frame, values=[nv["Mã Nhân Viên"] for nv in danh_sach_nhan_vien])
    tk.Label(HienThi_frame, text="Chọn Nhân Viên:", relief="solid", bd=2).grid(row=2, column=0, pady=5)
    nhan_vien_combobox.grid(row=2, column=1, pady=5)

    tk.Label(HienThi_frame, text="Chọn Thức Ăn:", relief="solid", bd=2).grid(row=3, column=0, pady=5)
    thuc_an_listbox = tk.Listbox(HienThi_frame, selectmode=tk.MULTIPLE, width=40, height=6)
    thuc_an_listbox.grid(row=3, column=1, pady=5)
    for tu in drink_list:
        thuc_an_listbox.insert(tk.END, tu["Tên Thức Ăn"])

    tk.Label(HienThi_frame, text="Số Lượng (phân cách bằng dấu phẩy):", relief="solid", bd=2).grid(row=4, column=0, pady=5)

    # Input field for quantity
    so_luong_entry = tk.Entry(HienThi_frame, width=20)
    so_luong_entry.grid(row=4, column=1, pady=5)

    # Increase quantity button
    def tang_so_luong():
        current_value = so_luong_entry.get()
        try:
            so_luong = list(map(int, current_value.split(','))) if current_value else [0]
            if len(so_luong) < len(thuc_an_listbox.curselection()):
                so_luong.append(1)
            else:
                so_luong[-1] += 1
            so_luong_entry.delete(0, tk.END)
            so_luong_entry.insert(0, ','.join(map(str, so_luong)))
        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng phải là số và cách nhau bằng dấu phẩy!")

    tk.Button(HienThi_frame, text="+", command=tang_so_luong, width=3).grid(row=4, column=2, pady=5)

    # Decrease quantity button
    def giam_so_luong():
        current_value = so_luong_entry.get()
        try:
            so_luong = list(map(int, current_value.split(','))) if current_value else [0]
            if so_luong:
                if so_luong[-1] > 1:
                    so_luong[-1] -= 1
                else:
                    so_luong.pop()
            so_luong_entry.delete(0, tk.END)
            so_luong_entry.insert(0, ','.join(map(str, so_luong)))
        except ValueError:
            messagebox.showerror("Lỗi", "Số lượng phải là số và cách nhau bằng dấu phẩy!")

    tk.Button(HienThi_frame, text="-", command=giam_so_luong, width=3).grid(row=4, column=3, pady=5)

    # Date and discount code inputs
    ngay_hoa_don = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    tk.Label(HienThi_frame, text="Ngày Lập Hóa Đơn:", relief="solid").grid(row=1, column=2, pady=5)
    ngay_hoa_don.grid(row=2, column=2, pady=5)

    ma_giam_gia = ["GIAM10", "GIAM20", "GIAM30"]
    ma_giam_gia_combobox = ttk.Combobox(HienThi_frame, values=ma_giam_gia)
    ma_giam_gia_combobox.set("Chọn mã giảm giá")
    tk.Label(HienThi_frame, text="Mã Giảm Giá:", relief="solid", bd=2).grid(row=5, column=0, pady=5)
    ma_giam_gia_combobox.grid(row=5, column=1, pady=5)

    danh_sach_hoa_don_listbox = tk.Listbox(HienThi_frame, width=120, height=10)
    danh_sach_hoa_don_listbox.grid(row=6, column=0, columnspan=4, pady=10)

    # Update invoice list display
    def cap_nhat_danh_sach_hoa_don():
        danh_sach_hoa_don_listbox.delete(0, tk.END)
        for hoa_don in invoice_list:
            if 'Chi Tiết Thức Ăn' in hoa_don:
                chi_tiet = ", ".join(f"{tu['Thức Ăn']} ({tu['Số Lượng']}x {tu['Giá Thức Ăn(VNĐ)']:,} VNĐ)" for tu in
                                     hoa_don['Chi Tiết Thức Ăn'])
                tong_tien_dinh_dang = "{:,.0f}".format(hoa_don['Tổng Tiền']).replace(",", ".")
                danh_sach_hoa_don_listbox.insert(
                    tk.END,
                    f"Khách Hàng: {hoa_don['Tên Khách Hàng']} | NV: {hoa_don['Nhân Viên']} | "
                    f"Thức Ăn : {chi_tiet} | Tổng Tiền : {tong_tien_dinh_dang} VNĐ | Giảm Giá: {hoa_don['Giảm Giá']}% |"
                    f"Ngày Lập: {hoa_don['Ngày Lập']}"
            )

    def them_hoa_don():
        khach_hang = ten_khach_hang.get()
        nhan_vien = nhan_vien_combobox.get()
        selected_items = thuc_an_listbox.curselection()
        so_luong_text = so_luong_entry.get()
        ma_giam = ma_giam_gia_combobox.get()
        ngay = ngay_hoa_don.get()

        if khach_hang and nhan_vien and selected_items and so_luong_text:
            try:
                so_luong = list(map(int, so_luong_text.split(',')))
                chi_tiet_thuc_an = []
                tong_tien = 0
                for i, idx in enumerate(selected_items):
                    ten_thuc_an = thuc_an_listbox.get(idx)
                    thuc_an = next((tu for tu in drink_list if tu['Tên Thức Ăn'] == ten_thuc_an), None)
                    gia = int(thuc_an['Giá Thức Ăn(VNĐ)'])
                    tong_tien += so_luong[i] * gia
                    chi_tiet_thuc_an.append({"Thức Ăn": ten_thuc_an, "Số Lượng": so_luong[i], "Giá Thức Ăn(VNĐ)": gia})

                giam_gia = int(ma_giam.replace("GIAM", "")) if ma_giam in ma_giam_gia else 0
                tong_tien -= tong_tien * giam_gia / 100

                invoice_list.append({
                    "Tên Khách Hàng": khach_hang,
                    "Nhân Viên": nhan_vien,
                    "Chi Tiết Thức Ăn": chi_tiet_thuc_an,
                    "Tổng Tiền": tong_tien,
                    "Giảm Giá": giam_gia,
                    "Ngày Lập": ngay
                })

                cap_nhat_danh_sach_hoa_don()
                messagebox.showinfo("Thành Công", "Hóa đơn đã được thêm!")
            except ValueError:
                messagebox.showerror("Lỗi", "Số lượng phải là số và cách nhau bằng dấu phẩy!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin hóa đơn!")

    def xoa_hoa_don():
        select_idx = danh_sach_hoa_don_listbox.curselection()
        if select_idx:
            confirm = messagebox.askyesno("Xác Nhận", "Bạn có chắc chắn muốn xóa hóa đơn này?")
            if confirm:
                idx = invoice_list[select_idx[0]]
                invoice_list.remove(idx)
                cap_nhat_danh_sach_hoa_don()
                messagebox.showinfo("Thành Công", "Hoá đơn đã được xóa!")
            else:
                messagebox.showerror("Lỗi", "Vui lòng chọn hoá đơn để xóa!")


    def sua_hoa_don():
        chi_so_chon = danh_sach_hoa_don_listbox.curselection()
        if chi_so_chon:
            hoa_don_chon = invoice_list[chi_so_chon[0]]
            hoa_don_chon["Tên Khách Hàng"] = ten_khach_hang.get()
            hoa_don_chon["Nhân Viên"] = nhan_vien_combobox.get()
            cap_nhat_danh_sach_hoa_don()
            messagebox.showinfo("Thành Công", "Hoá đơn đã được sửa!")
        else:
            messagebox.showerror("Lỗi", "Vui lòng chọn hoá đơn để sửa!")

    tk.Button(HienThi_frame, text="Thêm Hoá Đơn", command=them_hoa_don, width=35, height=2, bg="#98a77c").grid(row=7, column=0, padx=5, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Xóa Hoá Đơn", command=xoa_hoa_don, width=35, height=2, bg="#98a77c").grid(row=7, column=1, padx=5, pady=10, sticky="e")
    tk.Button(HienThi_frame, text="Sửa Hoá Đơn", command=sua_hoa_don, width=35, height=2, bg="#98a77c").grid(row=7, column=2, padx=5, pady=10, sticky="e")

    cap_nhat_danh_sach_hoa_don()
# Doanh Thu
invoice_list = [
    {"Ngày Lập": "2024-12-01", "Tổng Tiền": 200000},
    {"Ngày Lập": "2024-12-02", "Tổng Tiền": 300000},
    {"Ngày Lập": "2024-12-03", "Tổng Tiền": 500000},
    # Thêm dữ liệu nếu cần
]

def hien_thi_doanh_thu(HienThi_frame):
    # Xóa nội dung cũ của frame
    for widget in HienThi_frame.winfo_children():
        widget.destroy()

    # Tiêu đề
    tk.Label(
        HienThi_frame,
        text="Tính Doanh Thu",
        font=("Arial", 17, "bold"),
        fg="#7B68EE",
        bg="lightyellow",
        relief="groove",
        bd=9
    ).grid(row=0, column=0, columnspan=3, pady=10)

    # Ngày bắt đầu và kết thúc
    tk.Label(HienThi_frame, text="Chọn Ngày Bắt Đầu:").grid(row=1, column=0, pady=5, sticky="w", padx=10)
    ngay_bat_dau = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    ngay_bat_dau.grid(row=1, column=1, pady=5, padx=10)

    tk.Label(HienThi_frame, text="Chọn Ngày Kết Thúc:").grid(row=2, column=0, pady=5, sticky="w", padx=10)
    ngay_ket_thuc = DateEntry(HienThi_frame, date_pattern="yyyy-mm-dd")
    ngay_ket_thuc.grid(row=2, column=1, pady=5, padx=10)

    # Hàm tính doanh thu
    def tinh_doanh_thu():
        try:
            start_date = datetime.strptime(ngay_bat_dau.get(), "%Y-%m-%d")
            end_date = datetime.strptime(ngay_ket_thuc.get(), "%Y-%m-%d")
            if start_date > end_date:
                messagebox.showerror("Lỗi", "Ngày bắt đầu phải nhỏ hơn ngày kết thúc!")
                return

            tong_tien = sum(
                hoa_don["Tổng Tiền"] for hoa_don in invoice_list
                if start_date <= datetime.strptime(hoa_don["Ngày Lập"], "%Y-%m-%d") <= end_date
            )
            messagebox.showinfo("Doanh Thu", f"Tổng Doanh Thu: {tong_tien:,} VNĐ")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng chọn ngày hợp lệ!")

    # Nút tính doanh thu
    tk.Button(
        HienThi_frame,
        text="Tính Doanh Thu",
        command=tinh_doanh_thu,
        width=20,
        height=2,
        bg="#7CFC00"
    ).grid(row=3, column=1, pady=10)

    # Khung vẽ biểu đồ
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=HienThi_frame)
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=3, pady=20)

    # Hàm vẽ biểu đồ doanh thu theo ngày
    def ve_bieu_do_ngay():
        ax.clear()
        ngay = [hoa_don["Ngày Lập"] for hoa_don in invoice_list]
        tien = [hoa_don["Tổng Tiền"] for hoa_don in invoice_list]
        ax.bar(ngay, tien, color="blue")
        ax.set_title("Doanh Thu Từng Ngày")
        ax.set_xlabel("Ngày")
        ax.set_ylabel("Doanh Thu (VNĐ)")
        canvas.draw()

    # Hàm vẽ biểu đồ doanh thu theo tuần
    def ve_bieu_do_tuan():
        ax.clear()
        tuan = ["Tuần 1", "Tuần 2", "Tuần 3", "Tuần 4"]  # Giả định
        doanh_thu_tuan = [sum(t["Tổng Tiền"] for t in invoice_list if int(t["Ngày Lập"].split("-")[2]) in range(1, 8)),
                          1000000, 1200000, 900000]  # Ví dụ
        ax.bar(tuan, doanh_thu_tuan, color="green")
        ax.set_title("Doanh Thu Từng Tuần")
        ax.set_xlabel("Tuần")
        ax.set_ylabel("Doanh Thu (VNĐ)")
        canvas.draw()

    # Hàm vẽ biểu đồ doanh thu theo tháng
    def ve_bieu_do_thang():
        ax.clear()
        thang = ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4"]  # Giả định
        doanh_thu_thang = [1000000, 1500000, 1200000, 1800000]  # Ví dụ
        ax.bar(thang, doanh_thu_thang, color="orange")
        ax.set_title("Doanh Thu Từng Tháng")
        ax.set_xlabel("Tháng")
        ax.set_ylabel("Doanh Thu (VNĐ)")
        canvas.draw()

    # Nút vẽ biểu đồ
    tk.Button(
        HienThi_frame,
        text="Vẽ Biểu Đồ Ngày",
        command=ve_bieu_do_ngay,
        width=20,
        height=2,
        bg="#ADD8E6"
    ).grid(row=5, column=0, pady=10)

    tk.Button(
        HienThi_frame,
        text="Vẽ Biểu Đồ Tuần",
        command=ve_bieu_do_tuan,
        width=20,
        height=2,
        bg="#90EE90"
    ).grid(row=5, column=1, pady=10)

    tk.Button(
        HienThi_frame,
        text="Vẽ Biểu Đồ Tháng",
        command=ve_bieu_do_thang,
        width=20,
        height=2,
        bg="#FFB6C1"
    ).grid(row=5, column=2, pady=10)
login_window()
#main_window()


