import tkinter as tk
from unittest import result

root = tk.Tk()
root.title("Let's be SECRET :)")
root.geometry('800x230')
root.config(bg = 'black')

#################################################### Functions section ####################################################################
                                                                                                                                   
def cesar_clicked():

    welcom.destroy()
    choose.destroy()
    cesar.destroy()
    num.destroy()
    reflection.destroy()

    output = tk.StringVar()

    def en_clicked():
        text = text_box.get()
        key = int(key_box.get())

        encoded_label = tk.Label(text = 'Encoded text = ', fg = 'green', bg = 'black',font = ('Consolas',14))
        encoded_label.place(x = 2, y = 130)

        result = ''
        for i in range(len(text)):
            ans = ord(text[i]) + key
            if ord(text[i]) > 64 and ord(text[i]) < 91:
                while ans > 90:
                    ans -= 25
                result += chr(ans)
            elif ord(text[i]) > 96 and ord(text[i]) < 123:
                while ans > 122:
                    ans -= 25
                result += chr(ans)
            else:
                result += text[i]

        output.set(result)

        result_label = tk.Label(textvariable = output, fg = 'white', bg = 'black',font = ('Consolas',14))
        result_label.place(x = 150, y = 130)

        #copy the result 
        def copy_button(result):
            root.clipboard_clear()
            root.clipboard_append(result)
        tk.Button(text='Copy', command=lambda: copy_button(result), fg = 'green', bg = 'black',font = ('Consolas',13) ).place(x = 10, y = 175)


    def de_clicked():
        text = text_box.get()
        key = int(key_box.get())

        decoded_label = tk.Label(text = 'Decoded text = ', fg = 'green', bg = 'black',font = ('Consolas',14))
        decoded_label.place(x = 2, y = 130)

        result = ''
        for i in range(len(text)):
            ans = ord(text[i]) - key
            if ord(text[i]) > 64 and ord(text[i]) < 91:
                while ans < 65:
                    ans += 25
                result += chr(ans)
            elif ord(text[i]) > 96 and ord(text[i]) < 123:
                while ans < 97:
                    ans += 25
                result += chr(ans)
            else:
                result += text[i]

        output.set(result)

        result_label = tk.Label(textvariable = output, fg = 'white', bg = 'black',font = ('Consolas',14))
        result_label.place(x = 150, y = 130)

        #copy the result 
        def copy_button(result):
            root.clipboard_clear()
            root.clipboard_append(result)
        tk.Button(text='Copy', command=lambda: copy_button(result), fg = 'green', bg = 'black',font = ('Consolas',13) ).place(x = 10, y = 175)




    text_label = tk.Label(text = 'Enter your text (only english): ', fg = 'green', bg = 'black',font = ('Consolas',14))
    text_label.place(x = 2, y = 10)

    text_box = tk.Entry(width= 40, fg = 'white', bg = 'black',font = ('Consolas',14)) 
    text_box.place(x = 335, y = 10)

    key_label = tk.Label(text = 'Enter your key: ', fg = 'green', bg = 'black',font = ('Consolas',14))
    key_label.place(x = 2, y = 50)

    key_box = tk.Entry(width= 25, fg = 'white', bg = 'black',font = ('Consolas',14))
    key_box.place(x = 170, y = 50)

    pas_label = tk.Label(text = "Choose 'en' or 'de' (encoding or decoding): ", fg = 'green', bg = 'black',font = ('Consolas',14))
    pas_label.place(x = 2, y = 90)

    en = tk.Button(text = 'en', fg = 'white', bg = 'black',font = ('Consolas',14), command=en_clicked)
    en.place(x = 450 , y = 90)

    de = tk.Button(text = 'de', fg = 'white', bg = 'black',font = ('Consolas',14), command=de_clicked)
    de.place(x = 500 , y = 90)





def num_clicked():
    welcom.destroy()
    choose.destroy()
    cesar.destroy()
    num.destroy()
    reflection.destroy()

    output = tk.StringVar()

    def en_clicked():
        adad_dic = {"a" : '26', "b" : '25', "c" : '24', "d" : '23', "e" : '22', "f" : '21', "g" : '20', "h" : '19', "i" : '18', "j" : '17', "k" : '16', "l" : '15', "m" : '14', "n" : '13', "o" : '12', "p" : '11', "q" : '10', "r" : '9', "s" : '8', "t" : '7', "u" : '6', "v" : '5', "w" : '4', "x" : '3', "y" : '2', "z" : '1'}
        text = text_box.get()

        result = ''
        for i in text:
            if i in adad_dic:
                result += adad_dic[i]
            else:
                if ord(i) > 64 and ord(i) < 91:
                    result += adad_dic[i.lower()]
                else:
                    result += i
            result += "~"

        output.set(result)

        encoded_label = tk.Label(text = 'Encoded text = ', fg = 'green', bg = 'black',font = ('Consolas',14))
        encoded_label.place(x = 2, y = 90)

        result_label = tk.Label(textvariable = output, fg = 'white', bg = 'black',font = ('Consolas',14))
        result_label.place(x = 150, y = 90)

        #copy the result 
        def copy_button(result):
            root.clipboard_clear()
            root.clipboard_append(result)
        tk.Button(text='Copy', command=lambda: copy_button(result), fg = 'green', bg = 'black',font = ('Consolas',13) ).place(x = 10, y = 135)

    def de_clicked():
        char_dic = {'26' : "a", '25' : "b", '24' : "c", '23' : "d", '22' : "e", '21' : "f", '20' : "g", '19' : "h", '18' : "i", '17' : "j", '16' : "k", '15' : "l", '14' : "m", '13' : "n", '12' : "o", '11' : "p", '10' : "q", '9' : "r", '8' : "s", '7' : "t", '6' : "u", '5' : "v", '4' : "w", '3' : "x", '2' : "y", '1' : "z"}
        text = text_box.get()

        result = ''
        text = text.split('~')
        for i in text:
            if i in char_dic:
                result += char_dic[i]
            else:
                result += i
        
        output.set(result)

        encoded_label = tk.Label(text = 'Encoded text = ', fg = 'green', bg = 'black',font = ('Consolas',14))
        encoded_label.place(x = 2, y = 90)

        result_label = tk.Label(textvariable = output, fg = 'white', bg = 'black',font = ('Consolas',14))
        result_label.place(x = 150, y = 90)

        #copy the result 
        def copy_button(result):
            root.clipboard_clear()
            root.clipboard_append(result)
        tk.Button(text='Copy', command=lambda: copy_button(result), fg = 'green', bg = 'black',font = ('Consolas',13) ).place(x = 10, y = 135)


    text_label = tk.Label(text = 'Enter your text (only english): ', fg = 'green', bg = 'black',font = ('Consolas',14))
    text_label.place(x = 2, y = 10)

    text_box = tk.Entry(width= 40, fg = 'white', bg = 'black',font = ('Consolas',14)) 
    text_box.place(x = 335, y = 10)

    pas_label = tk.Label(text = "Choose 'en' or 'de' (encoding or decoding): ", fg = 'green', bg = 'black',font = ('Consolas',14))
    pas_label.place(x = 2, y = 50)

    en = tk.Button(text = 'en', fg = 'white', bg = 'black',font = ('Consolas',14), command=en_clicked)
    en.place(x = 450 , y = 50)

    de = tk.Button(text = 'de', fg = 'white', bg = 'black',font = ('Consolas',14), command=de_clicked)
    de.place(x = 500 , y = 50)


def reflection_clicked():
    
    welcom.destroy()
    choose.destroy()
    cesar.destroy()
    num.destroy()
    reflection.destroy()
     

    output = tk.StringVar()

    def enorde_cilcked():
        
        result1 = text_box2.get()
        result2 = result1[::-1]
        output.set(result2)

        result_label2 = tk.Label(text = 'result:', fg = 'green', bg = 'black',font = ('Consolas',14))
        result_label2.place(x = 20, y = 130)

        result_label3 = tk.Label(textvariable=output, fg = 'white', bg = 'black',font = ('Consolas',14))
        result_label3.place(x = 100, y = 130)

        def copy_button(result2):
            root.clipboard_clear()
            root.clipboard_append(result2)
        b_copy = tk.Button(text='Copy', command=lambda: copy_button(result2), fg = 'green', bg = 'black',font = ('Consolas',13) )
        b_copy.place(x = 20, y = 175)
    
    


    text_label2 = tk.Label(text = 'Enter your text (only english): ', fg = 'green', bg = 'black',font = ('Consolas',14))
    text_label2.place(x = 20, y = 20)

    text_box2 = tk.Entry(width= 40, fg = 'white', bg = 'black',font = ('Consolas',14)) 
    text_box2.place(x = 345, y = 20)
    
    b_deoren = tk.Button(text = 'decoding or encoding',fg = 'white', bg = 'black',font = ('Consolas',14), command = enorde_cilcked)
    b_deoren.place(x=20,y=70)

    

#################################################################################################################################

welcom = tk.Label(root,text = "Welcom to <Let's be SECRET>", fg = 'green', bg = 'black',font = ('Consolas',15))
welcom.place(x = 260, y = 2)

choose = tk.Label(root,text = "choose one of the options to encode/decode your text: ",  fg = 'green', bg = 'black',font = ('Consolas',13))
choose.place(x = 170, y = 30)

cesar = tk.Button(root,text = 'Cesar', fg = 'green', bg = 'black',font = ('Consolas',15), command=cesar_clicked)
cesar.place(x = 187, y = 80)


num = tk.Button(root,text = 'Numcode', fg = 'green', bg = 'black',font = ('Consolas',15), command=num_clicked)
num.place(x = 312, y = 80)

reflection = tk.Button(root,text = 'Reflection', fg = 'green', bg = 'black',font = ('Consolas',15), command=reflection_clicked)
reflection.place(x = 452, y = 80)



root.mainloop()