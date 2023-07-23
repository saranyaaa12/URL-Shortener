import pyshorteners
import tkinter as tk


root = tk.Tk()
root.title("Minz URL Shortener")
root.geometry("400x400+550+230")
root.configure(bg="light blue")
root.resizable(False, False)


#function for shortening url 
def shorten_url():
    url = originalUrl.get()
    newUrl = pyshorteners.Shortener().tinyurl.short(url)
    shortenedUrl.insert(tk.END, newUrl)


#App name
tk.Label(root, text="MINZ URL SHORTENER", font=("calibri",14,"bold"), fg="black", bg="light blue").pack(pady=5)


#Instruction text
tk.Label(root, text="Copy and Paste the Url you wish to shorten: ", font=("calibri",14,"bold"), fg="white", bg="black").pack( pady=5)


#Original url
originalUrl = tk.Entry(root, font=("calibri",12), width=50, bd=5)
originalUrl.pack(pady=10, padx=20)


#Generate button
tk.Button(root, text="GENERATE URL", font=("times new roman",12, "bold"), command=shorten_url).place(x=120, y=170)


#New url text
tk.Label(root, text="New Shortened Url: ", font=("calibri",14,"bold"), fg="white", bg="black").place(x=110, y=220)


#Shortened url
shortenedUrl = tk.Entry(root, font=("calibri",12), width=45, bd=1, bg="light blue")
shortenedUrl.place(x=17, y=270)


root.mainloop()