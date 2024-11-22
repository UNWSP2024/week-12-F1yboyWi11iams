# Joe's Automotive performs the following routine maintenance service:
# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler replacement - $200.00
# Tire Rotation - $20.00
# Write a GUI with check buttons that allows the user to select any or all of these services.
# When the user clicks a button, the total charges should be displayed.

import tkinter
import tkinter.messagebox

class CarService_GUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames. One for the check buttons
        # and another for teh regular Button widgets
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create seven IntVar objects to use with
        # the check buttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # Set IntVar object prices
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # Create check button widgets in top_frame
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Oil Change - $30.00',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Lube Job - $20.00',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Radiator Flush - $40.00',
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                       text='Transmission Fluid - $100.00',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                                       text='Inspection - $35.00',
                                       variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame,
                                       text='Muffler replacement - $200.00',
                                       variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame,
                                       text='Tire Rotation - $20.00',
                                       variable=self.cb_var7)

        # Pack Checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Create a Get Price button and a Quit button
        self.getprice_button = tkinter.Button(self.bottom_frame,
                                              text='Get Price',
                                              command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack buttons
        self.getprice_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start mainloop
        tkinter.mainloop()

    # show_choice method is callback for Get Price button

    def show_choice(self):
        # Create a message string
        self.message = 'Your total:\n'

        # Determine which checkbuttons are selected and
        # build the message string accordingly.
        total = 0
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'
        if self.cb_var4.get() == 1:
            self.message = self.message + '4\n'
        if self.cb_var5.get() == 1:
            self.message = self.message + '5\n'
        if self.cb_var6.get() == 1:
            self.message = self.message + '6\n'
        if self.cb_var7.get() == 1:
            self.message = self.message + '7\n'

            tkinter.messagebox.showinfo('Total', self.message)

if __name__ == '__main__':
    carservice_gui = CarService_GUI()
