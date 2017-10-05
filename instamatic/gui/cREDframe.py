from Tkinter import *


class ExperimentalcRED(LabelFrame):
    """docstring for ExperimentalSED"""
    def __init__(self, parent):
        LabelFrame.__init__(self, parent, text="Continuous rotation electron diffraction")
        self.parent = parent

        self.init_vars()

        Label(self, width=30,text="Exposure time").grid(row=4, column=0)
        self.exposure_time = Entry(self, width=70, textvariable=self.var_exposure_time)
        self.exposure_time.grid(row=4, column=1)

        self.CollectionButton = Button(self, text="Start Collection", command=self.start_collection, anchor=W)
        self.CollectionButton.grid(row=10, column=0)

        self.CollectionStopButton = Button(self, text="Stop Collection", command=self.stop_collection, anchor=W, state=DISABLED)
        self.CollectionStopButton.grid(row=11 , column=0)

        self.lb_coll1 = Label(self, width=60, text="Now you can start to rotate the goniometer at any time.", fg="red")
        self.lb_coll2 = Label(self, width=60, text="Click STOP COLLECTION BEFORE removing your foot from the pedal!", fg="red")
        
    def init_vars(self):
        self.var_exposure_time = DoubleVar(value=0.5)

    def set_trigger(self, trigger=None):
        self.triggerEvent = trigger

    def set_events(self, startEvent=None, stopEvent=None):
        self.startEvent = startEvent
        self.stopEvent = stopEvent

    def start_collection(self):
        print "Start button pressed"
        # TODO: make a pop up window with the STOP button?
        self.CollectionStopButton.config(state=NORMAL)
        self.CollectionButton.config(state=DISABLED)
        self.lb_coll1.grid(row=10, column=1)
        self.lb_coll2.grid(row=11, column=1)
        self.startEvent.set()
        self.triggerEvent.set()

    def stop_collection(self):
        print "Stop button pressed"
        self.CollectionStopButton.config(state=DISABLED)
        self.CollectionButton.config(state=NORMAL)
        self.lb_coll1.grid_forget()
        self.lb_coll2.grid_forget()
        self.stopEvent.set()

    def get_expt(self):
        return self.var_exposure_time.get()


if __name__ == '__main__':
    root = Tk()
    ExperimentalcRED(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
