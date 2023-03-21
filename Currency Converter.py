import tkinter as tk
from tkinter import ttk
import requests

# Create a list of currencies to select from
CURRENCIES = [
    "NGN", "USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "HKD", "NZD"
]

# Define the font to use
FONT = "Exo"

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")
        master.geometry("345x300")
        master.configure(bg="#154c79")
        master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create the currency selection labels and comboboxes
        from_label = tk.Label(self.master, text="From:", font=(FONT, 12), bg="#154c79")
        from_label.place(x=20, y=10)
        self.from_combobox = ttk.Combobox(self.master, values=CURRENCIES, font=(FONT, 12), width=10)
        self.from_combobox.place(x=20, y=40)
        self.from_combobox.current(0)

        to_label = tk.Label(self.master, text="To:", font=(FONT, 12), bg="#154c79")
        to_label.place(x=200, y=10)
        self.to_combobox = ttk.Combobox(self.master, values=CURRENCIES, font=(FONT, 12), width=10)
        self.to_combobox.place(x=200, y=40)
        self.to_combobox.current(1)

        # Create the amount entry field and convert button
        self.amount_entry = tk.Entry(self.master, font=(FONT, 12), width=15)
        self.amount_entry.place(x=100, y=70)

        convert_button = tk.Button(self.master, text="Convert", font=(FONT, 12), command=self.convert, bg="white")
        convert_button.place(x=140, y=100)

        # Create the result label
        self.result_label = tk.Label(self.master, text="", font=(FONT, 12), bg="#154c79")
        self.result_label.place(x=10, y=200)

    def convert(self):
        # Get the currency codes from the comboboxes
        from_currency = self.from_combobox.get()
        to_currency = self.to_combobox.get()

        # Get the amount to convert
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid amount")
            return

        # Make the API request to get the exchange rate #https://v6.exchangerate-api.com/v6/2c0c790a08235c6dc6d915c6/latest/
        try:
            response = requests.get(f"https://api.currencyfreaks.com/latest?apikey=e72cf52d136d4ab8b38b42279c4fe3e6{from_currency}") 
            data = response.json()
            exchange_rate = data["rates"][to_currency]
        except:
            self.result_label.config(text="Error getting exchange rate")
            return

        # Calculate the converted amount and display the result
        converted_amount = amount * exchange_rate
        self.result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

root = tk.Tk()
# icon = tk.ImageTk.PhotoImage(tk.Image.open('icon.png'))
# root.iconphoto(False, False)
converter = CurrencyConverter(root)
root.mainloop()