
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import mysql.connector
class LoginScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.master.geometry("500x300")
        self.master.title("Real Estate Management System")

        # # create a canvas to display the background image
        self.canvas = tk.Canvas(self.master, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack()

        # load the background image file and create a PhotoImage objecth
        self.bg_image = Image.open("Img.png")
        self.bg_image2 = self.bg_image.resize((1300,900))
        self.bg_image3 = ImageTk.PhotoImage(self.bg_image2)
        # use a label to display the image as a background
        self.canvas.create_image(0, 0, image=self.bg_image3, anchor=tk.NW)

        # create labels and entry widgets for username and password
        self.lbl_username = tk.Label(self.canvas, text="Username",bg="light blue",width=10,height=1)
        self.lbl_username.place(x=250, y=100)
        self.ent_username = tk.Entry(self.canvas,width=35)
        self.ent_username.place(x=350, y=100)

        self.lbl_password = tk.Label(self.canvas, text="Password",bg="light blue",width=10,height=1)
        self.lbl_password.place(x=250, y=150)
        self.ent_password = tk.Entry(self.canvas, show="*",width=35)
        self.ent_password.place(x=350, y=150)




        # # create buttons for user login and admin login
        self.btn_user_login = tk.Button(self.canvas, text="User Login", command=self.user_login, bg="#62CDFF",width=10)
        self.btn_user_login.place(x=380, y=200)

        # bind <Return> event to user_login function
        self.master.bind('<Return>', lambda event: self.user_login())

        
    def user_login(self):
        users = {"Anvesh": "anvesh@69" , "Nishi": "nishi@64"}
        # check if username and password are valid for user login
        username = self.ent_username.get()
        password = self.ent_password.get()


        if username in users and users[username] == password:
            root.destroy()          # if valid login, open user management screen
        
        else:
            # Error message if credentials are invalid
            messagebox.showerror("Error", "Invalid username or password")
        self.destroy()


# create the main window and show the login screen
root = tk.Tk()
app = LoginScreen(master=root)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width,height))
app.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import mysql.connector


# from PIL import ImageTk, Image


def sell_upd():
    root1.withdraw()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="epitomeofmanliness@JIRAIYA",
        database="mumbai"
    )

# Create cursor
    mycursor = mydb.cursor()


# Create Tkinter window
    root = tk.Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                root.winfo_screenheight()))
    root.configure(bg="#FFF6CC")
    root.title("Sell Property")

    #### Set background image
    # global background_image
    # bg_image = Image.open("sell_main.png")
    # bg_image = bg_image.resize(
    #     (root.winfo_screenwidth(), root.winfo_screenheight()))
    
    # background_image = ImageTk.PhotoImage(bg_image)
    # background_label = tk.Label(root, image=background_image)
    # background_label.place(x=0, y=0)

    # self.canvas = tk.Canvas(self.master, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    # self.canvas.pack()

        # load the background image file and create a PhotoImage object
    # self.bg_image = Image.open("sell_main.png")
    # self.bg_image2 = self.bg_image.resize((1300,900))
    # self.bg_image3 = ImageTk.PhotoImage(self.bg_image2)
    # # use a label to display the image as a background
    # self.canvas.create_image(0, 0, image=self.bg_image3, anchor=tk.NW)

    # Create labels and input fields
    id_label = tk.Label(root, text="ID:", font=("Arial", 14), bg='white')
    id_label.place(x=root.winfo_screenwidth()*0.2,
                y=root.winfo_screenheight()*0.15)
    id_entry = tk.Entry(root, font=("Arial", 14))
    id_entry.place(x=root.winfo_screenwidth()*0.3,
                y=root.winfo_screenheight()*0.15)
    price_label = tk.Label(root, text="Price:", font=("Arial", 14), bg='white')
    price_label.place(x=root.winfo_screenwidth()*0.2,
                    y=root.winfo_screenheight()*0.2)
    price_entry = tk.Entry(root, font=("Arial", 14))
    price_entry.place(x=root.winfo_screenwidth()*0.3,
                    y=root.winfo_screenheight()*0.2)

    bhk_label = tk.Label(root, text="BHK:", font=("Arial", 14), bg='white')
    bhk_label.place(x=root.winfo_screenwidth()*0.2,
                    y=root.winfo_screenheight()*0.25)
    bhk_entry = tk.Entry(root, font=("Arial", 14))
    bhk_entry.place(x=root.winfo_screenwidth()*0.3,
                    y=root.winfo_screenheight()*0.25)

    address_label = tk.Label(root, text="Address:", font=("Arial", 14), bg='white')
    address_label.place(x=root.winfo_screenwidth()*0.2,
                        y=root.winfo_screenheight()*0.3)
    address_entry = tk.Entry(root, font=("Arial", 14))
    address_entry.place(x=root.winfo_screenwidth()*0.3,
                        y=root.winfo_screenheight()*0.3)

    location_label = tk.Label(root, text="Location:",
                            font=("Arial", 14), bg='white')
    location_label.place(x=root.winfo_screenwidth()*0.2,
                        y=root.winfo_screenheight()*0.35)
    location_entry = tk.Entry(root, font=("Arial", 14))
    location_entry.place(x=root.winfo_screenwidth()*0.3,
                        y=root.winfo_screenheight()*0.35)

    rent_label = tk.Label(root, text="Rent:", font=("Arial", 14), bg='white')
    rent_label.place(x=root.winfo_screenwidth()*0.2,
                    y=root.winfo_screenheight()*0.4)
    rent_entry = tk.Entry(root, font=("Arial", 14))
    rent_entry.place(x=root.winfo_screenwidth()*0.3,
                    y=root.winfo_screenheight()*0.4)
    
                # Add a "Back" button to the top left corner of the window

    back_button = Button(root, text="Back", command= lambda: (root.destroy(),root1.deiconify()))
    back_button.place(x=10,y=10)


    # Function to select image from device and display path


    def select_image():
        global image_path
        image_path = filedialog.askopenfilename()
        image_path_label.config(text=image_path)


    image_label = tk.Label(root, text="Image:", font=("Arial", 14), bg='white')
    image_label.place(x=root.winfo_screenwidth()*0.2,
                    y=root.winfo_screenheight()*0.45)
    image_button = tk.Button(root, text="Select Image",
                            font=("Arial", 14), command=select_image)
    image_button.place(x=root.winfo_screenwidth()*0.3,
                    y=root.winfo_screenheight()*0.45,width=150,height=30)

    image_path_label = tk.Label(root, font=("Arial", 12), bg='white',height=2)
    image_path_label.place(x=root.winfo_screenwidth()*0.42,
                        y=root.winfo_screenheight()*0.45)
    # Function to add prop
    # Get values from input fields


    def add_property():
        id = id_entry.get()
        price = price_entry.get()
        bhk = bhk_entry.get()
        address = address_entry.get()
        location = location_entry.get()
        rent = rent_entry.get()
        # Check if all fields are filled
        if id == "" or price == "" or bhk == "" or address == "" or location == "" or rent == "" or image_path == "":
            messagebox.showerror(
                "Error", "Please fill all fields and select an image")
            return

        # Insert property into MySQL database
        sql = "INSERT INTO mumbai_prop (id ,price, bhk, address, location, rent, image_path) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
        val = (id, price, bhk, address, location, rent, image_path)
        mycursor.execute(sql, val,)
        mydb.commit()

        # Show success message
        messagebox.showinfo("Success", "Property added successfully")

        # Clear input fields
        id_entry.delete(0, 'end')
        price_entry.delete(0, 'end')
        bhk_entry.delete(0, 'end')
        address_entry.delete(0, 'end')
        location_entry.delete(0, 'end')
        rent_entry.delete(0, 'end')
        image_path_label.config(text="")


    submit_button = tk.Button(root, text="Submit", font=(
        "Arial", 14), command=add_property)
    submit_button.place(x=root.winfo_screenwidth()*0.5,
                        y=root.winfo_screenheight()*0.5)
    
    root.mainloop()









def rent_upd():
    root1.destroy()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="epitomeofmanliness@JIRAIYA",
        database="mumbai"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Define the Tkinter interface
    root = Tk()
    root.geometry("1280x720")
    root.title("Real Estate Management")

    def show_property_info(id):
        # Query the database for the property information using the property ID
        cursor.execute("SELECT * FROM mumbai_prop WHERE id=%s", (id,))
        property = cursor.fetchone()

        # Create a new interface to display the property information
        property_info = Toplevel()
        property_info.geometry("800x360")
        property_info.title(property[2])

        # Create a frame to hold the property image and information
        frame = Frame(property_info)
        frame.grid(row=0, column=0, sticky="nsew")

        # Display the property image
        img = Image.open(property[5])
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)
        img_label = Label(frame, image=img)
        img_label.image = img
        img_label.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

        # Display the property information
        # Add a text widget to display contact information
        contact_text = Text(frame, height=15, width=50)

        info_label = Label(
            frame, text=f"Rent : Rs.{property[6]}/month", font="Cooper 18 ")
        info_label.grid(row=0, column=1, padx=15, pady=10, sticky="w")

        info_label = Label(
            frame, text=f"BHK : {property[3]}\nFurniture : Semi Furnished\nAddress : {property[4]}\nCar Parking : Yes\nLift Availability:Yes", font="Cooper 14 ", bg="white")
        info_label.grid(row=1, column=1, padx=45, pady=10, sticky="w")

        contact_text.insert(
            END, "Contact us:\nPhone:- +91 9011926665\nEmail: user123@gmail.com")
        contact_text.grid(row=1, column=1, columnspan=2,
                          padx=10, pady=10, sticky="w")

        # Configure the grid to expand vertically
        property_info.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)

    # Define the search function

    def search(*args):
        # Clear the existing properties
        for widget in frame.winfo_children():
            widget.destroy()

        # Get the search query
        query = location_entry.get()

        # Query the database for properties in the given location
        cursor.execute(
            "SELECT * FROM mumbai_prop WHERE location LIKE %s", (f"%{query}%",))

        # Display the properties
        row = 0
        col = 0
        for i, property in enumerate(cursor):
            # Get the image of the property
            img = Image.open(property[5])
            img = img.resize((150, 150))
            img = ImageTk.PhotoImage(img)

            # Create a button for the property with the image
            btn = Button(frame, image=img,
                         command=lambda id=property[0]: show_property_info(id))
            btn.image = img
            btn.grid(row=row, column=col, padx=10, pady=10)

            # Display the information of the property below the image button
            info_label = Label(
                frame, text=f"BHK: {property[3]}\nRent: {property[6]}/month")
            info_label.grid(row=row+1, column=col, padx=10, pady=10)

            # Increment the column and row counters
            col += 1
            if col == 5:
                col = 0
                row += 2

    # Add a "Back" button to the top left corner of the window

    # back_button = Button(root, text="Back", command= lambda: (root.destroy(),root1.deiconify()))
    # back_button.place(x=10,y=10)

    # Define the location label and entry box
    location_label = Label(root, text="Enter Location:")
    location_label.pack(pady=10)
    location_entry = ttk.Entry(root, width=50)
    location_entry.pack()

    # Bind the Enter key to the search function
    location_entry.bind("<Return>", search)

    # Define the search button
    search_button = Button(root, text="Search", command=search)
    search_button.pack(pady=10)

    # Define the frame for displaying the properties
    frame = Frame(root)
    frame.pack(pady=10)

    # Run the Tkinter main loop
    root.mainloop()










def buy_upd():
    root1.destroy()

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="epitomeofmanliness@JIRAIYA",
        database="mumbai"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Define the Tkinter interface
    root = Tk()
    root.geometry("1280x720")
    root.title("Real Estate Management")

    def show_property_info(id):
        # Query the database for the property information using the property ID
        cursor.execute("SELECT * FROM mumbai_prop WHERE id=%s", (id,))
        property = cursor.fetchone()

        # Create a new interface to display the property information
        property_info = Toplevel()
        property_info.geometry("800x360")
        property_info.title(property[2])

        # Create a frame to hold the property image and information
        frame = Frame(property_info)
        frame.grid(row=0, column=0, sticky="nsew")

        # Display the property image
        img = Image.open(property[5])
        img = img.resize((300, 300))
        img = ImageTk.PhotoImage(img)
        img_label = Label(frame, image=img)
        img_label.image = img
        img_label.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

        # Display the property information
        # Add a text widget to display contact information
        contact_text = Text(frame, height=15, width=50)

        info_label = Label(
            frame, text=f"Price : Rs.{property[1]}/-", font="Cooper 18 ")
        info_label.grid(row=0, column=1, padx=15, pady=10, sticky="w")

        info_label = Label(
            frame, text=f"BHK : {property[3]}\nFurniture : Semi Furnished\nAddress : {property[4]}\nCar Parking : Yes\nLift Availability:Yes", font="Cooper 14 ", bg="white")
        info_label.grid(row=1, column=1, padx=45, pady=10, sticky="w")

        contact_text.insert(
            END, "Contact us:\nPhone:- +91 9011926665\nEmail: user123@gmail.com")
        contact_text.grid(row=1, column=1, columnspan=2,
                          padx=10, pady=10, sticky="w")

        # Configure the grid to expand vertically
        property_info.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)



    # Define the search function

    def search(*args):
        # Clear the existing properties
        for widget in frame.winfo_children():
            widget.destroy()

        # Get the search query
        query = location_entry.get()

        # Query the database for properties in the given location
        cursor.execute(
            "SELECT * FROM mumbai_prop WHERE location LIKE %s", (f"%{query}%",))

        # Display the properties
        row = 0
        col = 0
        for i, property in enumerate(cursor):
            # Get the image of the property
            img = Image.open(property[5])
            img = img.resize((150, 150))
            img = ImageTk.PhotoImage(img)

            # Create a button for the property with the image
            btn = Button(frame, image=img,
                         command=lambda id=property[0]: show_property_info(id))
            btn.image = img
            btn.grid(row=row, column=col, padx=10, pady=10)

            # Display the information of the property below the image button
            info_label = Label(
                frame, text=f"BHK: {property[3]}\nPrice: {property[1]}")
            info_label.grid(row=row+1, column=col, padx=10, pady=10)

            # Increment the column and row counters
            col += 1
            if col == 5:
                col = 0
                row += 2
                            # Add a "Back" button to the top left corner of the window

    # back_button = Button(root, text="Back", command= lambda: (root.destroy(),root1.deiconify()))
    # back_button.place(x=10,y=10)

    # Define the location label and entry box
    location_label = Label(root, text="Enter Location:")
    location_label.pack(pady=10)
    location_entry = ttk.Entry(root, width=50)
    location_entry.pack()

    # Bind the Enter key to the search function
    location_entry.bind("<Return>", search)

    # Define the search button
    search_button = Button(root, text="Search", command=search)
    search_button.pack(pady=10)

    # Define the frame for displaying the properties
    frame = Frame(root)
    frame.pack(pady=10)

    # Run the Tkinter main loop
    root.mainloop()


# create main window
root1 = tk.Tk()
root1.title("Real Estate")
width = root1.winfo_screenwidth()
height = root1.winfo_screenheight()
root1.geometry("%dx%d" % (width, height))
# root.geometry("500x300")

# load background image
bg_image = Image.open("img2.png")
bg_image2 = bg_image.resize((1300, 900))
bg_image3 = ImageTk.PhotoImage(bg_image2)

# create label with background image
bg_label = tk.Label(root1, image=bg_image3)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# create button to buy properties
buy1 = tk.PhotoImage(file=("Buy.png"))
navin_label = tk.Label(image=buy1)

buy_button = tk.Button(root1, image=buy1, command=buy_upd)
buy_button.place(x=450, y=425, width=100, height=100)


# create button to sell properties
sell1 = tk.PhotoImage(file=("Sell.png"))
navin_label2 = tk.Label(image=sell1)
sell_button = tk.Button(root1, image=sell1, command=sell_upd)
sell_button.place(x=590, y=425, width=100, height=100)

# create button to rent properties
rent1 = tk.PhotoImage(file=("Rent.png"))
navin_label1 = tk.Label(image=rent1)
rent_button = tk.Button(root1, image=rent1, command=rent_upd)
rent_button.place(x=730, y=425, width=100, height=100)
root1.mainloop()
