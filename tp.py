'''import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkmacosx import Button  # Better buttons for macOS

def handle_login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "abhi@giet.edu" and password == "1234":
        messagebox.showinfo("Success", "Welcome to Giet Bucks!")
    elif email == "" or password == "":
        messagebox.showwarning("Error", "Please fill in all fields")
    else:
        messagebox.showerror("Failed", "Invalid Credentials")

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show='')
        toggle_btn.config(text="Hide")

root = tk.Tk()
root.title("Giet Bucks Student Portal")
root.geometry('400x650')
root.configure(background='#00704A')

# Logo Handling
try:
    img = Image.open('star.png')
    img = img.resize((120, 100))
    img_tk = ImageTk.PhotoImage(img)
    tk.Label(root, image=img_tk, bg='#00704A').pack(pady=(30, 10))
except Exception as e:
    tk.Label(root, text="[ Logo ]", bg='#00704A', fg='white').pack(pady=20)

tk.Label(root, text="GIET BUCKS", font=('Helvetica', 28, 'bold'), bg='#00704A', fg='white').pack()
tk.Label(root, text="Student Login", font=('Helvetica', 14), bg='#00704A', fg='#FFD700').pack(pady=(0, 20))

# Email Field
tk.Label(root, text="Institutional Email", font=('Arial', 12), bg='#00704A', fg='white').pack(anchor='w', padx=50)
email_entry = tk.Entry(root, font=('Arial', 16), width=20, borderwidth=0, highlightthickness=2)
email_entry.pack(pady=5)

# Password Field
tk.Label(root, text="Password", font=('Arial', 12), bg='#00704A', fg='white').pack(anchor='w', padx=50, pady=(15, 0))
pass_frame = tk.Frame(root, bg='#00704A')
pass_frame.pack()

password_entry = tk.Entry(pass_frame, font=('Arial', 16), width=15, show="*", borderwidth=0, highlightthickness=2)
password_entry.pack(side='left', pady=5)

# Using tkmacosx Button for toggle as well to keep it consistent
toggle_btn = Button(pass_frame, text="Show", command=toggle_password, font=('Arial', 10), 
                    bg='white', borderless=1, width=50)
toggle_btn.pack(side='right', padx=5)

# Login Button - SIZE DEFINED HERE
login_btn = Button(root, text="LOGIN", font=('Arial', 16, 'bold'), 
                   bg='#FFD700', fg='black', borderless=1, 
                   activebackground='#e6c200', 
                   command=handle_login,
                   width=200, height=50) 

login_btn.pack(pady=40)

# Footer
tk.Label(root, text="©️ 2026 GIET University", font=('Arial', 10), bg='#00704A', fg='#a3c9bb').pack(side='bottom', pady=10)

root.mainloop()'''
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Safe import for macOS button
try:
    from tkmacosx import Button
except:
    Button = tk.Button

def handle_login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "abhi@giet.edu" and password == "1234":
        messagebox.showinfo("Success", "Welcome to Giet Bucks!")
    elif email == "" or password == "":
        messagebox.showwarning("Error", "Please fill in all fields")
    else:
        messagebox.showerror("Failed", "Invalid Credentials")

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show='')
        toggle_btn.config(text="Hide")

# Main Window
root = tk.Tk()
root.title("Giet Bucks Student Portal")
root.geometry('400x650')
root.configure(background='#00704A')

# Logo Handling (Fixed)
try:
    img = Image.open('images.jpeg')
    img = img.resize((120, 100))
    img_tk = ImageTk.PhotoImage(img)

    logo_label = tk.Label(root, image=img_tk, bg='#00704A')
    logo_label.image = img_tk  # IMPORTANT (prevents image disappearing)
    logo_label.pack(pady=(30, 10))

except:
    tk.Label(root, text="[ Logo ]", bg='#00704A', fg='white').pack(pady=20)

# Title
tk.Label(root, text="GIET BUCKS", font=('Helvetica', 28, 'bold'),
         bg='#00704A', fg='white').pack()

tk.Label(root, text="Student Login", font=('Helvetica', 14),
         bg='#00704A', fg='#FFD700').pack(pady=(0, 20))

# Email Field
tk.Label(root, text="Institutional Email", font=('Arial', 12),
         bg='#00704A', fg='white').pack(anchor='w', padx=50)

email_entry = tk.Entry(root, font=('Arial', 16), width=25,
                       borderwidth=0, highlightthickness=2)
email_entry.pack(pady=5)

# Password Field
tk.Label(root, text="Password", font=('Arial', 12),
         bg='#00704A', fg='white').pack(anchor='w', padx=50, pady=(15, 0))

pass_frame = tk.Frame(root, bg='#00704A')
pass_frame.pack()

password_entry = tk.Entry(pass_frame, font=('Arial', 16), width=18,
                          show="*", borderwidth=0, highlightthickness=2)
password_entry.pack(side='left', pady=5)

toggle_btn = Button(pass_frame, text="Show", command=toggle_password,
                    font=('Arial', 10), bg='white', borderless=1,
                    width=60)
toggle_btn.pack(side='right', padx=5)

# Login Button (Fixed Size)
login_btn = Button(root, text="LOGIN",
                   font=('Arial', 16, 'bold'),
                   bg='#FFD700', fg='black',
                   activebackground='#e6c200',
                   command=handle_login,
                   width=200, height=45)

login_btn.pack(pady=40)

# Footer
tk.Label(root, text="©️ 2026 GIET University",
         font=('Arial', 10),
         bg='#00704A', fg='#a3c9bb').pack(side='bottom', pady=10)

root.mainloop()