from tkinter import *
import maktabkhooneh_dl as dl
from tkinter import filedialog


def get_cookie_file():
    global cookie_file
    cookie_file = filedialog.askopenfilename(initialdir="/",
                                             title="Select your cookie File",
                                             filetypes=(("Text files",
                                                         "*.txt*"),
                                                        ("all files",
                                                         "*.*")))


def show_store_url_file():
    store_url_file.place(relx=0.5, rely=0.5, y=50, x=0, anchor=CENTER)


def select_store_url_file():
    global store_urls_file
    store_urls_file = filedialog.askopenfilename(initialdir="/",
                                                 title="Select your store_url File",
                                                 filetypes=(("Text files",
                                                             "*.txt*"),
                                                            ("all files",
                                                             "*.*")))


def start_download():
    global low_quality, mp3, store_urls, no_download, is_course_range, cookie_file, store_urls_file, url
    low_quality, mp3, store_urls, no_download, is_course_range = low_quality.get(), mp3.get(), store_urls.get(), \
        no_download.get(), is_course_range.get()
    url = str(inp_url.get())
    range_start, range_end = str(inp_range_start.get()), str(inp_range_end.get())
    print(low_quality, mp3, store_urls, no_download, is_course_range, cookie_file, store_urls_file, url)

    dl.main(cookie_file, url, low_quality, mp3, store_urls, store_urls_file, no_download, is_course_range, range_start,
            range_end)

window = Tk()
window.title("maktabkhooneh-dl")
window.iconbitmap("")

low_quality = BooleanVar()
mp3 = BooleanVar()
store_urls = BooleanVar()
no_download = BooleanVar()
is_course_range = BooleanVar()
cookie_file = StringVar()
store_urls_file = StringVar()
url = StringVar()

button_explore = Button(window, text="choose cookie File", command=get_cookie_file)
checkbutton_low_quality = Checkbutton(window, text='low quality', variable=low_quality, onvalue=True, offvalue=False)
checkbutton_mp3 = Checkbutton(window, text='mp3', variable=mp3, onvalue=True, offvalue=False)
checkbutton_store_urls = Checkbutton(window, text='store urls', variable=store_urls, onvalue=True, offvalue=False,
                                     command=show_store_url_file)
checkbutton_no_download = Checkbutton(window, text='no download', variable=no_download, onvalue=True, offvalue=False)
inp_url = Entry(window, font="arial 18")
inp_text = Label(window, text="course url : ", font="arial 16")
store_url_file = Button(window, text="choose store url file", command=select_store_url_file)
checkbutton_range = Checkbutton(window, text='range ?', variable=is_course_range, onvalue=True, offvalue=False)
inp_range_start = Entry(window, font="arial 18")
inp_start_text = Label(window, text="range start : ", font="arial 16")
inp_range_end = Entry(window, font="arial 18")
inp_end_text = Label(window, text="range end : ", font="arial 16")
start_download_btn = Button(window, text="start Download", command=start_download)

button_explore.place(relx=0.5, rely=0.5, y=-100, x=0, anchor=CENTER)
checkbutton_low_quality.place(relx=0.5, rely=0.5, y=-100, x=110, anchor=CENTER)
checkbutton_mp3.place(relx=0.5, rely=0.5, y=-100, x=200, anchor=CENTER)
checkbutton_store_urls.place(relx=0.5, rely=0.5, y=-100, x=-110, anchor=CENTER)
checkbutton_no_download.place(relx=0.5, rely=0.5, y=-100, x=-200, anchor=CENTER)
inp_text.place(relx=0.5, rely=0.5, y=-200, x=-200, anchor=CENTER)
inp_url.place(relx=0.5, rely=0.5, y=-200, x=0, anchor=CENTER)
checkbutton_range.place(relx=0.5, rely=0.5, y=50, x=0, anchor=CENTER)
inp_range_start.place(relx=0.5, rely=0.5, y=100, x=0, anchor=CENTER)
inp_start_text.place(relx=0.5, rely=0.5, y=100, x=-200, anchor=CENTER)
inp_range_end.place(relx=0.5, rely=0.5, y=150, x=0, anchor=CENTER)
inp_end_text.place(relx=0.5, rely=0.5, y=150, x=-200, anchor=CENTER)
start_download_btn.place(relx=0.5, rely=0.5, y=0, x=0, anchor=CENTER)

window.geometry(f"{int(window.winfo_screenwidth() * 0.75)}x{int(window.winfo_screenheight() * 0.75)}")
window.mainloop()
