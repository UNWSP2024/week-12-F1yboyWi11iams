# A long-distance provider charges the following rates for telephone calls:
# Rate Category                             Rate per Minute
# Daytime (6:00 A.M. through 5:59 P.M.)         $0.02
# Evening (6:00 P.M.  through 11:59 P.M.)       $0.12
# Off-Peak (midnight through 5:59 P.M.) 	    $0.05
# Write a GUI application that allows the user to select a rate category (from a set of radio buttons),
# and enter the number of minutes of the call into an Entry widget. An info dialog box should display the
# charge for the call.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.DoubleVar()

        self.radio_var.set(0)

        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Daytime (6:00 A.M. through 5:59 P.M): $0.02',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Evening (6:00 P.M.  through 11:59 P.M.): $0.12',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Off-Peak (midnight through 5:59 P.M.): $0.05',
                                       variable=self.radio_var,
                                       value=3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.time_entry = tkinter.StringVar
        self.time_label = tkinter.Label(self.mid_frame,
                                          text='Enter the total call time in minutes:')
        self.time_entry = tkinter.Entry(self.mid_frame,
                                        width = 10)
        self.time_label.pack(side='left')
        self.time_entry.pack(side='left')

        self.get_price_button = tkinter.Button(self.bottom_frame,
                                        text='Click for Charges',
                                        command=self.calc_charges)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        self.get_price_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calc_charges(self):
        total = 0
        print(self.radio_var.get())
        total = self.time_entry * self.radio_var.get()
        # if self.rb1.get() == 1:
        #     total = self.time_entry * 0.02
        # if self.rb2.get() == 1:
        #     total = self.time_entry * 0.12
        # if self.rb3.get() == 1:
        #     total = self.time_entry * 0.05
        tkinter.messagebox.showinfo('Total Charges',f'Your charges: ${total}')

if __name__ == '__main__':
    my_gui = MyGUI()
