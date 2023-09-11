from tkinter import *
import maktabkhooneh_dl as dl
from tkinter import filedialog


def get_cookie_file():
    cookie_file = filedialog.askopenfilename(initialdir="/",
                                             title="Select your cookie File",
                                             filetypes=(("Text files",
                                                         "*.txt*"),
                                                        ("all files",
                                                         "*.*")))


window = Tk()
window.title("maktabkhooneh-dl")
window.iconbitmap("")
low_quality = None
mp3 = None
store_urls = None
no_download = None

button_explore = Button(window, text="choose cookie File", command=get_cookie_file)
checkbutton_low_quality = Checkbutton(window, text='low quality', variable=low_quality, onvalue=True, offvalue=False)
checkbutton_mp3 = Checkbutton(window, text='mp3', variable=mp3, onvalue=True, offvalue=False)
checkbutton_store_urls = Checkbutton(window, text='store urls', variable=store_urls, onvalue=True, offvalue=False, )
checkbutton_no_download = Checkbutton(window, text='no download', variable=no_download, onvalue=True, offvalue=False)

button_explore.place(relx=0.5, rely=0.5, y=-100, x=0, anchor=CENTER)
checkbutton_low_quality.place(relx=0.5, rely=0.5, y=-100, x=110, anchor=CENTER)
checkbutton_mp3.place(relx=0.5, rely=0.5, y=-100, x=200, anchor=CENTER)
checkbutton_store_urls.place(relx=0.5, rely=0.5, y=-100, x=-110, anchor=CENTER)
checkbutton_no_download.place(relx=0.5, rely=0.5, y=-100, x=-200, anchor=CENTER)

window.geometry(f"{int(window.winfo_screenwidth() * 0.75)}x{int(window.winfo_screenheight() * 0.75)}")
window.mainloop()
