from tkinter import *


class Application(Frame):
    """ГУІ пріложеніе с кнопкамі."""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bt_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn["text"] = "Количесвто щелчков: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        self.bt_clicks += 1
        self.bttn["text"] = "Количество щелчков: " + str(self.bt_clicks)
        return self.bttn["text"]

root = Tk()
root.title("Бесполезность.")
root.geometry("300x300")
app = Application(root)
root.mainloop()
