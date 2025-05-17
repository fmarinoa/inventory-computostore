import tkinter as tk
from tkinter import messagebox

from app.controllers.product_controller import ProductController


class HomeView:
    def __init__(self, root, username):
        self.root = root
        self.root.title(f"Inventario ComputoStore - Bienvenido {username}!")
        self.root.geometry("600x400")

        title_label = tk.Label(self.root, text="Lista de Productos", font=("Arial", 16))
        title_label.pack(pady=10)

        product_frame = tk.Frame(self.root)
        product_frame.pack(pady=10, padx=10, fill="both", expand=True)

        try:
            products = ProductController.list_all_products()
            for product in products:
                product_label = tk.Label(product_frame, text=f"{product.product_code} - {product.name}")
                product_label.pack(anchor="w")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los productos: {e}")
