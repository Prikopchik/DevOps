import tkinter as tk
import requests
from tkinter import messagebox

def send_data():
    data = entry_send.get()
    if not data:
        messagebox.showwarning("Предупреждение", "Поле ввода не может быть пустым.")
        return
    try:
        response = requests.post('http://localhost:5000/api/data', json={'data': data})
        result = response.json()
        messagebox.showinfo("Результат", result.get('message', 'Нет сообщения от сервера.'))
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось отправить данные: {e}")

def get_data():
    try:
        response = requests.get('http://localhost:5000/api/data')
        if response.status_code == 200:
            result = response.json()
            received_text.delete(1.0, tk.END)
            received_text.insert(tk.END, result.get('data', 'Нет данных от сервера.'))
        else:
            messagebox.showerror("Ошибка", "Не удалось получить данные с сервера.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные: {e}")

root = tk.Tk()
root.title("Frontend 2.0")

send_frame = tk.Frame(root)
send_frame.pack(pady=10)

label_send = tk.Label(send_frame, text="Введите текст для отправки на сервер:")
label_send.pack(side=tk.LEFT, padx=5)

entry_send = tk.Entry(send_frame, width=40)
entry_send.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(send_frame, text="Отправить", command=send_data)
send_button.pack(side=tk.LEFT, padx=5)

get_frame = tk.Frame(root)
get_frame.pack(pady=10)

get_button = tk.Button(get_frame, text="Получить данные", command=get_data)
get_button.pack()

received_label = tk.Label(root, text="Полученные данные:")
received_label.pack(pady=5)

received_text = tk.Text(root, height=10, width=60)
received_text.pack(pady=5)

root.mainloop()
