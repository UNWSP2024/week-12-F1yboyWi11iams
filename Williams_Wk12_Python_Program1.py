# Write a GUI program that calculates a car's gas mileage. The program's window
# should have Entry widgets that let the user enter the number of gallons of
# gas the car holds, and the number of miles it can be driven on a full tank.
# When a Calculate MPG button is clicked, the program should display the number
# of miles that the car may be driven per gallon of gas. Use the following formula
# to calculate miles per gallon: MPG = miles / gallons.

import tkinter

class MPGGUI:
    def __init__(self):

        # Create main window
        self.main_window = tkinter.Tk()

        # Create frames
        self.miles_frame = tkinter.Frame(self.main_window)
        self.gallons_frame = tkinter.Frame(self.main_window)
        self.mpg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack widgets
        self.miles_label = tkinter.Label(self.miles_frame,
                                         text='Enter how many miles the car can go on one full tank of gas:')
        self.miles_entry = tkinter.Entry(self.miles_frame,
                                           width=10)
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.gallons_label = tkinter.Label(self.gallons_frame,
                                           text='Enter how many gallons of gas the fuel tank can hold:')
        self.gallons_entry = tkinter.Entry(self.gallons_frame,
                                           width=10)
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        self.result_label = tkinter.Label(self.mpg_frame,
                                          text='Miles per gallon of gas:')
        self.mpg = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mpg_frame,
                                         textvariable=self.mpg)
        self.result_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # Create and pack button widgets
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Miles per Gallon',
                                          command=self.calc_mpg)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.miles_frame.pack()
        self.gallons_frame.pack()
        self.mpg_frame.pack()
        self.button_frame.pack()

        # Start the main loop
        tkinter.mainloop()

    # The calc_mpg method is the callback function for
    # the calc_button widget.

    def calc_mpg(self):
        # Get two values and store as variables
        self.miles = float(self.miles_entry.get())
        self.gallons = float(self.gallons_entry.get())

        # Calculate MPG
        self.milespergallon = self.miles / self.gallons

        # Update mpg_label widget by storing value of self.milespergallon
        # in the StringVar object referenced by mpg
        self.mpg.set(self.milespergallon)

# Create an instance of teh MPG class
if __name__ == '__main__':
    mpggui = MPGGUI()