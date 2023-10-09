from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox, Style
import pytube

window = Tk()
window.geometry('400x520+340+100')
window.title('Downloader')
icon = PhotoImage(file=r"D:\MSA\Python Projects\downloader\photos\download.png")
window.iconphoto(False, icon)
window.resizable(False, False)

def download_video():
    url = e_1.get()
    quality = combobox.get()
    yt = pytube.YouTube(url)
    streams = yt.streams.filter(res=quality)
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4",
                                             filetypes=[("MP4 Files", "*.mp4"), ("All Files", "*.*")])
    if file_path:
        stream = streams.first()
        stream.download(output_path=file_path)
        print("File downloaded successfully.")
    else:
        print("File download canceled.")


main_text = Label(window, text="Download your favorite movies\nand TV shows with our downloader app\nfrom youtube",
                  font=("Bodoni MT", 14), bg="#00C957", fg="#050505")
main_text.pack(fill=X)

image = PhotoImage(file=r"D:\MSA\Python Projects\downloader\photos\download.png")
label = Label(window, image=image, pady=5)
label.pack()

text_1 = Label(window, text="Url of video :", font=("Bodoni MT", 15), fg="#050505")
text_1.place(x=15, y=210)

text_2 = Label(window, text="Quality of video :", font=("Bodoni MT", 15), fg="#050505")
text_2.place(x=15, y=250)

e_1 = Entry(window, font=("Bodoni MT", 15), width= 20, bg= '#00C957', fg= '#050505')
e_1.place(x=135, y=210)

qualities = ['720p', '360p', '240p', '144p']
style= Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#00C957", background= "white")
combobox = Combobox(window, values=qualities, style="TCombobox")
combobox.place(x=170, y=255)

download_video_button = Button(window, text="Download Video", font=("Bodoni MT", 15), fg="#050505", bg="#00C957", command=download_video)
download_video_button.place(x=120, y=290)

window.mainloop()


