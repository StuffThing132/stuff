from tkinter import *

root = Tk()

root.title("Driving License")
root.geometry("400x250")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_vehicle_type = Label(root)

def myLicense():
    id_value = 19827198349
    print(type(id_value))
    name = "Winnie the Pooh"
    print(type(name)) 
    dob = "21 August 1921"
    print(type(dob))
    pin = 451478
    print(type(pin))
    address = "Disney Land, Hong kong"
    print(type(address))
    vehicle_type = ["Two","Four"]
    print(type(vehicle_type))
    
    label_id['text'] = id_value
    label_name['text'] = name
    label_dob['text'] = dob
    label_pin['text'] = pin
    label_address['text'] = address
    label_vehicle_type['text'] = vehicle_type
    
    
button1 = Button(root, text = "Show my Driving License", command=myLicense)


canvas.pack()

root.mainloop()