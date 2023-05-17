import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *
from PIL import Image , ImageTk
import sys
import os

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Family Court")
        self.attributes('-fullscreen',True)
        self.geometry(f"{1080}x{580}")
        
        # app_w =1080
        # app_h =580
        # screen_w = self.winfo_screenwidth()
        # screen_h = self.winfo_screenheight()
        # x=(screen_w / 2) - (app_w / 2)
        # y=(screen_h / 2) - (app_h / 2)
        
        # self.geometry(f"{app_w}x{app_h}+{int(x)}+{int(y)}")
        # self.eval('tk::PlaceWindow . center')
        # bg = PhotoImage(file="law1.png")
        # limg= Label(self, i=bg)
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
       
         # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
       
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Family Court", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
       
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Incubation",command=self.sidebar_button1_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
       
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Alimony",command=self.sidebar_button2_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Restart",fg_color="#FF5D5D",command=self.reset)
        self.sidebar_button_2.grid(row=9, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Exit",fg_color="#FF5D5D",command=self.destroy)
        self.sidebar_button_2.grid(row=10, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[ "Dark","Light", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
       
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button2_event(self):
        self.button1_frame = customtkinter.CTkFrame(self, width=820, corner_radius=0)
        self.button1_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.button1_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.button1_frame, text="Alimony", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.radiobutton_frame = customtkinter.CTkFrame(self.button1_frame)
        self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.ans1_frame = customtkinter.CTkFrame(self,width=140, corner_radius=0)
        self.ans1_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.ans1_frame.grid_rowconfigure(10, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.ans1_frame, text="Answer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=2, padx=20, pady=(20, 10))
        
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_var1 = tkinter.IntVar(value=0)
        self.radio_var2 = tkinter.IntVar(value=0)
        self.radio_var3 = tkinter.IntVar(value=0)
        self.radio_var4 = tkinter.IntVar(value=0)
        self.radio_var5 = tkinter.IntVar(value=0)
        self.radio_var6 = tkinter.IntVar(value=0)
        self.radio_var7= tkinter.IntVar(value=0)
        self.radio_var8 = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Does the mother have the incubation?" )
        self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var, value= 1 ,command=self.q1_ans)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=5, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var, value= 2,command=self.q1_ans)
        self.radio_button_2.grid(row=1, column=3, pady=10, padx=5, sticky="n")

        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Is the child under 2 years?" )
        self.label_radio_group.grid(row=2, column=1, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_7 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var1, value= 1 ,command=self.q1_ans)
        self.radio_button_7.grid(row=2, column=2, pady=10, padx=5, sticky="n")
        self.radio_button_8 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var1, value= 2,command=self.q1_ans)
        self.radio_button_8.grid(row=2, column=3, pady=10, padx=5, sticky="n")

        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="is the wife staying in the house?" )
        self.label_radio_group.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var2, value= 1 ,command=self.q1_ans)
        self.radio_button_1.grid(row=3, column=2, pady=10, padx=5, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var2, value= 2,command=self.q1_ans)
        self.radio_button_2.grid(row=3, column=3, pady=10, padx=5, sticky="n")

        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Is the husband rich enough to pay a servant?" )
        self.label_radio_group.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var3, value= 1 ,command=self.q1_ans)
        self.radio_button_1.grid(row=4, column=2, pady=10, padx=5, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var3, value= 2,command=self.q1_ans)
        self.radio_button_2.grid(row=4, column=3, pady=10, padx=5, sticky="n")


        self.scaling_label = customtkinter.CTkLabel(self.radiobutton_frame, text="What is the kind of divorce?", anchor="w")
        self.scaling_label.grid(row=5, column=1, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.radiobutton_frame ,values=[" ","Normal divorce", "Divorced for harm", "Wife divorced the Husband", "None of the above",],
                                                               command=self.divorce_ans)
        self.scaling_optionemenu.grid(row=6, column=1, padx=20, pady=(10, 20))

        

    def sidebar_button1_event(self):
        self.button1_frame = customtkinter.CTkFrame(self, width=820, corner_radius=0)
        self.button1_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.button1_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.button1_frame, text="Incubation", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.radiobutton_frame = customtkinter.CTkFrame(self.button1_frame)
        self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.ans1_frame = customtkinter.CTkFrame(self,width=140, corner_radius=0)
        self.ans1_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.ans1_frame.grid_rowconfigure(10, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.ans1_frame, text="Answer", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=2, padx=20, pady=(20, 10))
        
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_var1 = tkinter.IntVar(value=0)
        self.radio_var2 = tkinter.IntVar(value=0)
        self.radio_var3 = tkinter.IntVar(value=0)
        self.radio_var4 = tkinter.IntVar(value=0)
        self.radio_var5 = tkinter.IntVar(value=0)
        self.radio_var6 = tkinter.IntVar(value=0)
        self.radio_var7= tkinter.IntVar(value=0)
        self.radio_var8 = tkinter.IntVar(value=0)
       
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Do you have a girl under 17 or a boy under 15?" )
        self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var, value= 1 ,command=self.q2_ans)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=5, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var, value= 2,command=self.q2_ans)
        self.radio_button_2.grid(row=1, column=3, pady=10, padx=5, sticky="n")

        
    def q1_ans(self):
        self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
        self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
        self.ans2_frame.grid_rowconfigure(10, weight=1)
        if((str(self.radio_var.get()))== "1"):
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="husband will pay money for kids incubation \nhusband will pay money for kids to live a suitable life" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
            self.radio_button_7 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var1, value= 1 ,command=self.q1_ans)
            self.radio_button_7.grid(row=2, column=2, pady=10, padx=5, sticky="n")
            self.radio_button_8 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var1, value= 2,command=self.q1_ans)
            self.radio_button_8.grid(row=2, column=3, pady=10, padx=5, sticky="n")
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var2, value= 1 ,command=self.q1_ans)
            self.radio_button_1.grid(row=3, column=2, pady=10, padx=5, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var2, value= 2,command=self.q1_ans)
            self.radio_button_2.grid(row=3, column=3, pady=10, padx=5, sticky="n")
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var3, value= 1 ,command=self.q1_ans)
            self.radio_button_1.grid(row=4, column=2, pady=10, padx=5, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var3, value= 2,command=self.q1_ans)
            self.radio_button_2.grid(row=4, column=3, pady=10, padx=5, sticky="n")
        elif((str(self.radio_var.get()))== "2"):
            self.radio_button_7 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var1, value= 1 ,command=self.q1_ans,state = DISABLED)
            self.radio_button_7.grid(row=2, column=2, pady=10, padx=5, sticky="n")
            self.radio_button_8 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var1, value= 2,command=self.q1_ans, state= DISABLED)
            self.radio_button_8.grid(row=2, column=3, pady=10, padx=5, sticky="n")
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var2, value= 1 ,command=self.q1_ans, state=DISABLED)
            self.radio_button_1.grid(row=3, column=2, pady=10, padx=5, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var2, value= 2,command=self.q1_ans, state=DISABLED)
            self.radio_button_2.grid(row=3, column=3, pady=10, padx=5, sticky="n")
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var3, value= 1 ,command=self.q1_ans, state=DISABLED)
            self.radio_button_1.grid(row=4, column=2, pady=10, padx=5, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var3, value= 2,command=self.q1_ans, state=DISABLED)
            self.radio_button_2.grid(row=4, column=3, pady=10, padx=5, sticky="n")
        if((str(self.radio_var1.get()))== "1"):
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="husband will pay for breastfeeding" )
            self.logo_label.grid(row=2, column=2, padx=20, pady=(20, 10))
        if((str(self.radio_var2.get()))== "2"):
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="husband will pay rent for kids house" )
            self.logo_label.grid(row=3, column=2, padx=20, pady=(20, 10))
        if((str(self.radio_var3.get()))== "1"):
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="husband will pay for a servant" )
            self.logo_label.grid(row=4, column=2, padx=20, pady=(20, 10))
   
    def divorce_handle(self):
        self.ans3_frame = customtkinter.CTkFrame(self.ans2_frame,width=140, corner_radius=0)
        self.ans3_frame.grid(row=5, column=2, rowspan=4, sticky="nsew")
        self.ans3_frame.grid_rowconfigure(10, weight=1)
        if((str(self.radio_var4.get()))== "2"):
            self.logo_label = customtkinter.CTkLabel(self.ans3_frame, text="husband pay 24 month expense of the monthly aliment\nhusband pay 3 month expense of the monthly aliment" )
            self.logo_label.grid(row=5, column=2, padx=20, pady=(20, 10))
        if((str(self.radio_var5.get()))== "1"):
            self.logo_label = customtkinter.CTkLabel(self.ans3_frame, text="husband pay after divorce money" )
            self.logo_label.grid(row=6, column=2, padx=20, pady=(20, 10))
        if((str(self.radio_var6.get()))== "2"):
            self.logo_label = customtkinter.CTkLabel(self.ans3_frame, text="husband pay expense from 2 to 5 years of the monthly aliment\nhusband pay 3 month expense of the monthly aliment" )
            self.logo_label.grid(row=5, column=2, padx=20, pady=(20, 10))
    
    def q2_ans(self):
        if((str(self.radio_var.get()))== "2"):
            self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
            self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
            self.ans2_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="there is no incubation the children free to choose who to live with" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
        else:
            self.radiobutton_frame = customtkinter.CTkFrame(self.button1_frame)
            self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
            
            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Mother check",text_color="#FBE4C9", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="If mother not alive or alive suffering from any of these enter y if not enter n\n1- she is insane\n2- she is proven cheating on her husband\n3- she will travel outside the country and take the kids\n4- she is married to a stranger from the child\n5- she did practice professions that violate religion and the law\n6- She is not trusted, such as if she frequently go out and leave the child alone?")
            self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
          
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var1, value= 1 ,command=self.mother_state)
            self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var1, value= 2,command=self.mother_state)
            self.radio_button_2.grid(row=1, column=3, pady=10, padx=5, sticky="n")

    def mother_state(self):
        if((str(self.radio_var1.get()))== "2"):
            self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
            self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
            self.ans2_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="the mother will have the incubation" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
        else:
            self.radiobutton_frame = customtkinter.CTkFrame(self.button1_frame)
            self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Father check",text_color="#FBE4C9", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="If father not alive or alive suffering from any of these enter y if not enter n\n1- he is insane\n2- he has commit crimes before\n3- he is immoral\n4- he do not have a woman in the house to raise the children\n5- he will travel outside the country and take the kids\n6- it been 6 months before the father raised the case without an acceptable excuse?")
            self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
          
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var2, value= 1 ,command=self.father_state)
            self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var2, value= 2,command=self.father_state)
            self.radio_button_2.grid(row=1, column=3, pady=10, padx=5, sticky="n")
    
    def father_state(self):
        if((str(self.radio_var2.get()))== "2"):
            self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
            self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
            self.ans2_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="the father will have the incubation" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
        else:
            self.radiobutton_frame = customtkinter.CTkFrame(self.button1_frame)
            self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Mother's mother check",text_color="#FBE4C9", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="If mother's mother not alive or alive suffering from any of these enter y if not enter n\n1- she is insane\n2- she is proven cheating on her husband\n3- she will travel outside the country and take the kids\n4- she is married to a stranger from the child\n5- she did practice professions that violate religion and the law\n6- She is not trusted, such as if she frequently go out and leave the child alone?")
            self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
          
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var3, value= 1 ,command=self.mothermother_state)
            self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var3, value= 2,command=self.mothermother_state)
            self.radio_button_2.grid(row=1, column=3, pady=10, padx=5, sticky="n")

    def mothermother_state(self):
        if((str(self.radio_var3.get()))== "2"):
            self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
            self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
            self.ans2_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="the mother's mother will have the incubation" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
        else:
            self.radiobutton_frame = customtkinter.CTkFrame(self.button1_frame)
            self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Father's mother check",text_color="#FBE4C9", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="If father's mother not alive or alive suffering from any of these enter y if not enter n\n1- she is insane\n2- she is proven cheating on her husband\n3- she will travel outside the country and take the kids\n4- she is married to a stranger from the child\n5- she did practice professions that violate religion and the law\n6- She is not trusted, such as if she frequently go out and leave the child alone?")
            self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
          
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var4, value= 1 ,command=self.fathermother_state)
            self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var4, value= 2,command=self.fathermother_state)
            self.radio_button_2.grid(row=1, column=3, pady=10, padx=5, sticky="n")
    
    def fathermother_state(self):
        if((str(self.radio_var4.get()))== "2"):
            self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
            self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
            self.ans2_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="the father's mother will have the incubation" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
        else:
            self.radiobutton_frame = customtkinter.CTkFrame(self.button1_frame)
            self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Mother's sister check",text_color="#FBE4C9", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="If mother's sister not alive or alive suffering from any of these enter y if not enter n\n1- she is insane\n2- she is proven cheating on her husband\n3- she will travel outside the country and take the kids\n4- she is married to a stranger from the child\n5- she did practice professions that violate religion and the law\n6- She is not trusted, such as if she frequently go out and leave the child alone?")
            self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
          
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var5, value= 1 ,command=self.mothersister_state)
            self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var5, value= 2,command=self.mothersister_state)
            self.radio_button_2.grid(row=1, column=3, pady=10, padx=5, sticky="n")
    
    def mothersister_state(self):
        if((str(self.radio_var5.get()))== "2"):
            self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
            self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
            self.ans2_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="the mother's sister will have the incubation" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
        else:
            self.radiobutton_frame = customtkinter.CTkFrame(self.button1_frame)
            self.radiobutton_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Father's sister check",text_color="#FBE4C9", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=1, padx=20, pady=(20, 10))

            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="If father's sister not alive or alive suffering from any of these enter y if not enter n\n1- she is insane\n2- she is proven cheating on her husband\n3- she will travel outside the country and take the kids\n4- she is married to a stranger from the child\n5- she did practice professions that violate religion and the law\n6- She is not trusted, such as if she frequently go out and leave the child alone?")
            self.label_radio_group.grid(row=1, column=1, columnspan=1, padx=10, pady=10, sticky="")
          
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var6, value= 1 ,command=self.fathersister_state)
            self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var6, value= 2,command=self.fathersister_state)
            self.radio_button_2.grid(row=1, column=3, pady=10, padx=5, sticky="n")
    
    def fathersister_state(self):
        if((str(self.radio_var6.get()))== "2"):
            self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
            self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
            self.ans2_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="the father's sister will have the incubation" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
        else:
            self.ans2_frame = customtkinter.CTkFrame(self.ans1_frame,width=140, corner_radius=0)
            self.ans2_frame.grid(row=1, column=2, rowspan=4, sticky="nsew")
            self.ans2_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans2_frame, text="the child will go to a shelter",text_color="#FF5D5D" )
            self.logo_label.grid(row=1, column=2, padx=20, pady=(20, 10))
            
    
    def divorce_ans(self, divorce_type: str):
        if(divorce_type=="Normal divorce"):
            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="If the wife have done any of these defects enter y if not enter n\n1- prevented herself from her husband without a legitimate excuse\n2- left their home without a legitimate excuse\n3- prevented her husband from entering their house without a legitimate excuse\n4- A case was issued restricting her freedom in the rights of her husband\n5- She broke her commitment to her husband?")
            self.label_radio_group.grid(row=7, column=1, columnspan=1, padx=10, pady=10, sticky="")
          
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var4, value= 1 ,command=self.divorce_handle)
            self.radio_button_1.grid(row=7, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var4, value= 2,command=self.divorce_handle)
            self.radio_button_2.grid(row=7, column=3, pady=10, padx=5, sticky="n")
            
            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Is the after divorce money in the marriage contract?")
            self.label_radio_group.grid(row=8, column=1, columnspan=1, padx=10, pady=10, sticky="")
          
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var5, value= 1 ,command=self.divorce_handle)
            self.radio_button_1.grid(row=8, column=2, pady=10, padx=5, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var5, value= 2,command=self.divorce_handle)
            self.radio_button_2.grid(row=8, column=3, pady=10, padx=5, sticky="n")
        
        
        elif(divorce_type=="Divorced for harm"):
            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="If the wife have done any of these defects enter y if not enter n\n1- prevented herself from her husband without a legitimate excuse\n2- left their home without a legitimate excuse\n3- prevented her husband from entering their house without a legitimate excuse\n4- A case was issued restricting her freedom in the rights of her husband\n5- She broke her commitment to her husband?")
            self.label_radio_group.grid(row=7, column=1, columnspan=1, padx=10, pady=10, sticky="")
           
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var6, value= 1 ,command=self.divorce_handle)
            self.radio_button_1.grid(row=7, column=2, pady=10, padx=20, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var6, value= 2,command=self.divorce_handle)
            self.radio_button_2.grid(row=7, column=3, pady=10, padx=5, sticky="n")
            
            self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Is the after divorce money in the marriage contract?")
            self.label_radio_group.grid(row=8, column=1, columnspan=1, padx=10, pady=10, sticky="")
           
            self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="true", variable=self.radio_var5, value= 1 ,command=self.divorce_handle)
            self.radio_button_1.grid(row=8, column=2, pady=10, padx=5, sticky="n")
            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="False", variable=self.radio_var5, value= 2,command=self.divorce_handle)
            self.radio_button_2.grid(row=8, column=3, pady=10, padx=5, sticky="n")
      
        elif(divorce_type=="Wife divorced the Husband"):
            self.ans3_frame = customtkinter.CTkFrame(self.ans2_frame,width=140, corner_radius=0)
            self.ans3_frame.grid(row=6, column=2, rowspan=4, sticky="nsew")
            self.ans3_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans3_frame, text="the wife will give up on all her rights\nthe wife will give husband money before marriage back",text_color="#FF5D5D",font=customtkinter.CTkFont(size=12, weight="bold") )
            self.logo_label.grid(row=6, column=2, padx=20, pady=(20, 10))
      
        elif(divorce_type=="None of the above"):
            self.ans3_frame = customtkinter.CTkFrame(self.ans2_frame,width=140, corner_radius=0)
            self.ans3_frame.grid(row=6, column=2, rowspan=4, sticky="nsew")
            self.ans3_frame.grid_rowconfigure(10, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.ans3_frame, text="That's impossible" ,text_color="#FF5D5D",font=customtkinter.CTkFont(size=12, weight="bold"))
            self.logo_label.grid(row=6, column=2, padx=20, pady=(20, 10))
   
   
    def reset(self):
        self.destroy()
        app = App()
        app.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()
