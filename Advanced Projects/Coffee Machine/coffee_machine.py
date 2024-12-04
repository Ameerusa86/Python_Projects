import tkinter as tk

class CoffeeMachineApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Coffee Machine")

        self.water = 1000
        self.coffee_beans = 500
        self.milk = 1000
        self.cups = 10

        self.create_widgets()

    def create_widgets(self):
        self.label_status = tk.Label(self.master, text="Welcome to the Coffee Machine")
        self.label_status.pack()

        self.label_water = tk.Label(self.master, text=f"Water: {self.water}ml")
        self.label_water.pack()

        self.label_coffee_beans = tk.Label(self.master, text=f"Coffee Beans: {self.coffee_beans}g")
        self.label_coffee_beans.pack()

        self.label_milk = tk.Label(self.master, text=f"Milk: {self.milk}ml")
        self.label_milk.pack()

        self.label_cups = tk.Label(self.master, text=f"Cups: {self.cups}")
        self.label_cups.pack()

        self.entry_coffee_type = tk.Entry(self.master)
        self.entry_coffee_type.pack()

        self.button_make_coffee = tk.Button(self.master, text="Make Coffee", command=self.make_coffee)
        self.button_make_coffee.pack()

        self.button_refill = tk.Button(self.master, text="Refill", command=self.refill)
        self.button_refill.pack()

        self.button_exit = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.button_exit.pack()

    def make_coffee(self):
        coffee_type = self.entry_coffee_type.get().lower()
        if coffee_type == "espresso":
            if self.water < 50 or self.coffee_beans < 20 or self.cups < 1:
                self.label_status.config(text="Sorry, not enough ingredients to make espresso.")
                return
            self.water -= 50
            self.coffee_beans -= 20
            self.cups -= 1
            self.label_status.config(text="Espresso is ready!")
        elif coffee_type == "latte":
            if self.water < 100 or self.coffee_beans < 20 or self.milk < 50 or self.cups < 1:
                self.label_status.config(text="Sorry, not enough ingredients to make latte.")
                return
            self.water -= 100
            self.coffee_beans -= 20
            self.milk -= 50
            self.cups -= 1
            self.label_status.config(text="Latte is ready!")
        elif coffee_type == "cappuccino":
            if self.water < 100 or self.coffee_beans < 20 or self.milk < 100 or self.cups < 1:
                self.label_status.config(text="Sorry, not enough ingredients to make cappuccino.")
                return
            self.water -= 100
            self.coffee_beans -= 20
            self.milk -= 100
            self.cups -= 1
            self.label_status.config(text="Cappuccino is ready!")
        else:
            self.label_status.config(text="Invalid coffee type.")

        self.update_display()

    def refill(self):
        self.water = 1000
        self.coffee_beans = 500
        self.milk = 1000
        self.cups = 10
        self.label_status.config(text="Refilled successfully.")
        self.update_display()

    def update_display(self):
        self.label_water.config(text=f"Water: {self.water}ml")
        self.label_coffee_beans.config(text=f"Coffee Beans: {self.coffee_beans}g")
        self.label_milk.config(text=f"Milk: {self.milk}ml")
        self.label_cups.config(text=f"Cups: {self.cups}")

def main():
    root = tk.Tk()
    app = CoffeeMachineApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
