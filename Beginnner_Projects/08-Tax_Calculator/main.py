import customtkinter as ctk


class TaxCalculatorApp:
    def __init__(self):
        # Initialize the application window
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280x200")
        self.window.resizable(False, False)

        # Widget padding configuration
        padding_params = {"padx": 20, "pady": 10}

        # Income label and entry
        self.income_label = ctk.CTkLabel(self.window, text="Income:")
        self.income_label.grid(row=0, column=0, **padding_params)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **padding_params)

        # Tax rate label and entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text="Tax Rate (%):")
        self.tax_rate_label.grid(row=1, column=0, **padding_params)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **padding_params)

        # Result label and entry
        self.result_label = ctk.CTkLabel(self.window, text="Tax Amount:")
        self.result_label.grid(row=2, column=0, **padding_params)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")
        self.result_entry.grid(row=2, column=1, **padding_params)

        # Calculate button
        self.calculate_button = ctk.CTkButton(
            self.window, text="Calculate", command=self.calculate_tax
        )
        self.calculate_button.grid(row=3, column=1, **padding_params)

    def update_result(self, text: str):
        """Updates the result entry with the provided text."""
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        """Calculates the total tax based on the income and tax rate."""
        try:
            income = float(self.income_entry.get())
            tax_rate = float(self.tax_rate_entry.get())
            tax_amount = income * (tax_rate / 100)
            formatted_tax = f"${tax_amount:,.2f}"
            self.update_result(formatted_tax)
        except ValueError:
            self.update_result("Invalid input")

    def run(self):
        """Runs the tkinter application."""
        self.window.mainloop()


if __name__ == "__main__":
    tax_calculator_app = TaxCalculatorApp()
    tax_calculator_app.run()
