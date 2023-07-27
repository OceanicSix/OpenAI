import tkinter as tk
import req
import json

def sendReq():
    api_key=api_var.get()
    role=role_var.get()
    prompt=prompt_entry.get("1.0", tk.END)
    resp= req.makeReq(api_key, role, prompt)
    resp_entry.delete("1.0", tk.END)
    resp_entry.insert(tk.INSERT,resp)

# Define control+A behavior

def select_all_key(event):
    event.widget.select_range(0, tk.END)
    return 'break'

def select_all_role(event):
    event.widget.select_range(0, tk.END)
    return 'break'

def select_all_input(event):
    event.widget.tag_add(tk.SEL, "1.0", tk.END)
    return 'break'

def select_all_resp(event):
    event.widget.tag_add(tk.SEL, "1.0", tk.END)
    return 'break'


if __name__ == '__main__':
    window_object = tk.Tk()  # create main window

    # Open window having dimension 100x100 (width x height)
    window_object.geometry('900x500')

    window_object.title("ChatGPT Beta")
    api_var = tk.StringVar()
    role_var = tk.StringVar()

    prompt_var = tk.StringVar()
    resp_var = tk.StringVar()

    # Set default value for API key entry and role entry
    try:
        config_file=open("config.json", "r")
        conf=json.load(config_file)
        api_var.set(conf["api_key"])
        role_var.set(conf["role"])
        config_file.close()
    except Exception as e:
        print(e)
        print("Didn't find config file, user need to input config manually")
    finally:
        apikey_label = tk.Label(window_object, text='OpenAPI key', font=('calibre', 10, 'bold')).place(x=40,y=40)
        apikey_entry = tk.Entry(window_object, textvariable=api_var, font=('calibre', 10, 'normal'), width=80)
        apikey_entry.place(x=40,y=60)

        role_label = tk.Label(window_object, text='ChatGPT role', font=('calibre', 10, 'bold')).place(x=40,y=80)
        role_entry = tk.Entry(window_object, textvariable=role_var, font=('calibre', 10, 'normal'), width=80)
        role_entry.place(x=40,y=100)

        prompt_label = tk.Label(window_object, text='User input', font=('calibre', 10, 'bold')).place(x=40,y=120)
        prompt_entry = tk.Text(window_object, font=('Arial', 10, 'normal'))
        prompt_entry.place(x=40,y=140,height=100,width=800)

        resp_label = tk.Label(window_object, text='ChatGPT reply', font=('calibre', 10, 'bold')).place(x=40, y=320)
        resp_entry = tk.Text(window_object, font=('Arial', 10, 'normal'))
        resp_entry.place(x=40, y=340, height=100, width=800)

        # Submit button
        btn = tk.Button(window_object, text='Submit !', bd='5',command=sendReq).place(x=40,y=260)

        # Bind ctrl+A to select all user input
        apikey_entry.bind('<Control-KeyRelease-a>', select_all_key)
        role_entry.bind('<Control-KeyRelease-a>', select_all_role)
        prompt_entry.bind('<Control-KeyRelease-a>',select_all_input)
        resp_entry.bind('<Control-KeyRelease-a>',select_all_resp)

        window_object.mainloop()