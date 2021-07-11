import tkinter as tk
from PIL import Image, ImageTk
import random
import winsound

class Main():
    def __init__(self,master=None):
        self.master = master
        self.master.geometry("750x500")
        self.load_datas()
        self.make_frames()
        self.mp3 = {"グー":"datas/pya1.wav","チョキ":"datas/pya2.wav","パー":"datas/pya3.wav"}
        self.hand_to_num = {"グー":1,"チョキ":2,"パー":3}
        self.num_to_hand = {1:"グー",2:"チョキ",3:"パー"}

    def open_image(self, path):
        _image = Image.open(path).crop((0,0,500,400))
        _image = _image.resize((250,200)) 
        _image = ImageTk.PhotoImage(_image)
        # _image = _image.subsample(2,2)
        return _image

    def load_datas(self):
        self.G_image = self.open_image("datas/hinana.png") 
        self.T_image = self.open_image("datas/madoka.png") 
        self.P_image = self.open_image("datas/toru.png") 
        self.images = {"グー":self.G_image,"チョキ":self.T_image,"パー":self.P_image}

    def make_frames(self):
        self.G_frame = tk.Frame(self.master,bg="#000000",width=50,height=50)
        self.T_frame = tk.Frame(self.master,bg="#000000",width=50,height=50)
        self.P_frame = tk.Frame(self.master,bg="#000000",width=50,height=50)
        self.S_frame = tk.Frame(self.master,bg="#000000",width=100,height=100)
        self.make_buttons()
        self.pack_frames()

    def make_buttons(self):
        self.G_button = tk.Button(
            self.G_frame,
            text = "グー",
            compound="top",
            image=self.G_image,
            command = lambda:self.judgment("グー")
        )
        self.T_button = tk.Button(
            self.T_frame,
            text = "チョキ",
            compound="top",
            image=self.T_image,
            command = lambda:self.judgment("チョキ")
        )
        self.P_button = tk.Button(
            self.P_frame,
            text = "パー",
            compound="top",
            image=self.P_image,
            command = lambda:self.judgment("パー")
        )
        self.S_button = tk.Button(
            self.S_frame,
            text="CPU",
            compound="top"
        )
        self.pack_buttons()

    def pack_frames(self):
        self.G_frame.pack(side=tk.TOP,pady=5)
        self.T_frame.pack(side=tk.LEFT,padx=5)
        self.P_frame.pack(side=tk.RIGHT,padx=5)
        self.S_frame.pack(side=tk.TOP,pady=10)

    def pack_buttons(self):
        self.G_button.pack(fill=tk.BOTH)
        self.T_button.pack(fill=tk.BOTH)
        self.P_button.pack(fill=tk.BOTH)
        self.S_button.pack(fill=tk.BOTH)

    def judgment(self,st):
        player = self.hand_to_num[st]
        cpu = random.randint(1, 3)
        judg = player - cpu
        if judg == 0:
            print(f"{st}であいこ")
        elif judg == -1 or judg == 2:
            print(f"{st}でかち")
        else:
            print(f"{st}でまけ")

        self.S_button["image"] = self.images[self.num_to_hand[cpu]]
        # winsound.PlaySound(self.mp3[st], winsound.SND_FILENAME)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()