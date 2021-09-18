
from tkinter import*
import time

class B():
    def __init__(self):
        self.r_w, self.r_h = "600", "400"
        self.r_x, self.r_y = "10", "100"
        self.root_size = self.r_w + "x" + self.r_h + "+" + self.r_x + "+" + self.r_y
        self.root_title = "PLANNNER -- TK -- V2"
        self.root = Tk()
        print("Tk() >> root >> run")

        self.step = 50
        self.x_pos_p = 0
        self.y_pos_p = 0

        self.color_bg = 'white'
        self.color_fg = 'black'

        self.click_themes = 0
        self.color_mis_if_ok = 'green'
        self.color_mis_if_fail = 'red'

        
    def init_lbl(self):
        self.arr_text_mission = ['stand up !>                        6:50',
                                 'sleeping write !>               6:50',
                                 'teeth !>                              6:55',
                                 'power lesson !>                7:10',
                                 '20 uppi !>                          7:15',
                                 '20 downi !>                       7:15',
                                 'tea !>                                  7:20',
                                 'meditation !>                    7:30',
                                 'python coding !>             7:40',
                                 'clearing and exit !>          8:00']
        
        self.m1 = Label(self.f_mis, bg = 'blue')
        self.m2 = Label(self.f_mis)
        self.m3 = Label(self.f_mis)
        self.m4 = Label(self.f_mis)
        self.m5 = Label(self.f_mis)
        self.m6 = Label(self.f_mis)
        self.m7 = Label(self.f_mis)
        self.m8 = Label(self.f_mis)
        self.m9 = Label(self.f_mis)
        self.m10 = Label(self.f_mis)
        
        self.arr_label_for = [self.m1,
                              self.m2,
                              self.m3,
                              self.m4,
                              self.m5,
                              self.m6,
                              self.m7,
                              self.m8,
                              self.m9,
                              self.m10,]
##############################################################
    def com_for_btn_Y(self, name_btnf, name_btn, num_mis):
        name_btnf['bg'] = 'white'
        name_btnf['text'] = 'F'
        name_btn['bg'] = self.color_mis_if_ok
        self.arr_label_for[num_mis]['bg'] = self.color_mis_if_ok
        name_btn['text'] = 'OK'

        
    def com_bt_mis1(self):
        self.com_for_btn_Y(self.b1f, self.b1, 0)
        
    def com_bt_mis2(self):
        self.com_for_btn_Y(self.b2f, self.b2, 1)
        
    def com_bt_mis3(self):
        self.com_for_btn_Y(self.b3f, self.b3, 2)
        
    def com_bt_mis4(self):
        self.com_for_btn_Y(self.b4f, self.b4, 3)
        
    def com_bt_mis5(self):
        self.com_for_btn_Y(self.b5f, self.b5, 4)
        
    def com_bt_mis6(self):
        self.com_for_btn_Y(self.b6f, self.b6, 5)
        
    def com_bt_mis7(self):
        self.com_for_btn_Y(self.b7f, self.b7, 6)
        
    def com_bt_mis8(self):
        self.com_for_btn_Y(self.b8f, self.b8, 7)
        
    def com_bt_mis9(self):
        self.com_for_btn_Y(self.b9f, self.b9, 8)
        
    def com_bt_mis10(self):
        self.com_for_btn_Y(self.b10f, self.b10, 9)
        

##############################################################

##############################################################
    def com_for_btn_F(self, name_btn, name_btnf, num_mis):
        name_btn['bg'] = 'white'
        name_btn['text'] = 'F'
        name_btnf['bg'] = self.color_mis_if_fail
        self.arr_label_for[num_mis]['bg'] = self.color_mis_if_fail
        name_btn['text'] = 'OK'

        
    def com_bt_mis1f(self):
        self.com_for_btn_F(self.b1, self.b1f, 0)
        
    def com_bt_mis2f(self):
        self.com_for_btn_F(self.b2, self.b2f, 1)
        
    def com_bt_mis3f(self):
        self.com_for_btn_F(self.b3, self.b3f, 2)
        
    def com_bt_mis4f(self):
        self.com_for_btn_F(self.b4, self.b4f, 3)
        
    def com_bt_mis5f(self):
        self.com_for_btn_F(self.b5, self.b5f, 4)
        
    def com_bt_mis6f(self):
        self.com_for_btn_F(self.b6, self.b6f, 5)
        
    def com_bt_mis7f(self):
        self.com_for_btn_F(self.b7, self.b7f, 6)
        
    def com_bt_mis8f(self):
        self.com_for_btn_F(self.b8, self.b8f, 7)
        
    def com_bt_mis9f(self):
        self.com_for_btn_F(self.b9, self.b9f, 8)
        
    def com_bt_mis10f(self):
        self.com_for_btn_F(self.b10, self.b10f, 9)
        


##############################################################
        

    def init_btn_ok(self):
        self.arr_btn_com = [self.com_bt_mis1,
                            self.com_bt_mis2,
                            self.com_bt_mis3,
                            self.com_bt_mis4,
                            self.com_bt_mis5,
                            self.com_bt_mis6,
                            self.com_bt_mis7,
                            self.com_bt_mis8,
                            self.com_bt_mis9,
                            self.com_bt_mis10,]
        
        self.b1 = Button(self.f_mis_ok, text = 'Y')
        self.b2 = Button(self.f_mis_ok, text = 'Y')
        self.b3 = Button(self.f_mis_ok, text = 'Y')
        self.b4 = Button(self.f_mis_ok, text = 'Y')
        self.b5 = Button(self.f_mis_ok, text = 'Y')
        self.b6 = Button(self.f_mis_ok, text = 'Y')
        self.b7 = Button(self.f_mis_ok, text = 'Y')
        self.b8 = Button(self.f_mis_ok, text = 'Y')
        self.b9 = Button(self.f_mis_ok, text = 'Y')
        self.b10 = Button(self.f_mis_ok, text = 'Y')
        
        self.arr_btn_for = [self.b1,
                              self.b2,
                              self.b3,
                              self.b4,
                              self.b5,
                              self.b6,
                              self.b7,
                              self.b8,
                              self.b9,
                              self.b10,]



##############################################################

    def init_btn_fail(self):
        self.arr_btn_comf = [self.com_bt_mis1f,
                            self.com_bt_mis2f,
                            self.com_bt_mis3f,
                            self.com_bt_mis4f,
                            self.com_bt_mis5f,
                            self.com_bt_mis6f,
                            self.com_bt_mis7f,
                            self.com_bt_mis8f,
                            self.com_bt_mis9f,
                            self.com_bt_mis10f,]
        
        self.b1f = Button(self.f_mis_fail, text = 'F')
        self.b2f = Button(self.f_mis_fail, text = 'F')
        self.b3f = Button(self.f_mis_fail, text = 'F')
        self.b4f = Button(self.f_mis_fail, text = 'F')
        self.b5f = Button(self.f_mis_fail, text = 'F')
        self.b6f = Button(self.f_mis_fail, text = 'F')
        self.b7f = Button(self.f_mis_fail, text = 'F')
        self.b8f = Button(self.f_mis_fail, text = 'F')
        self.b9f = Button(self.f_mis_fail, text = 'F')
        self.b10f = Button(self.f_mis_fail, text = 'F')
        
        self.arr_btn_forf = [self.b1f,
                              self.b2f,
                              self.b3f,
                              self.b4f,
                              self.b5f,
                              self.b6f,
                              self.b7f,
                              self.b8f,
                              self.b9f,
                              self.b10f,]


    def init_win(self):
        pass
        
    def init_param_win(self):
        self.root.geometry(self.root_size)
        self.root.title(self.root_title)

    def init_frames(self):
        self.f_watch = Frame(self.root, bg = 'blue', relief = 'groove', bd = 2)
        self.f_watch.place(x = 0,y = 0, width = 400, height = 400)
        
        self.f_watch_local = Frame(self.f_watch, bg = 'blue', relief = 'groove', bd = 2)
        self.f_watch_local.place(x = 0,y = 350, width = 200, height = 50)
        
        self.f_watch_optimal = Frame(self.f_watch,bg = 'blue', relief = 'groove', bd = 2)
        self.f_watch_optimal.place(x = 200,y = 350, width = 200, height = 50)
        
        self.f_mis = Frame(self.root, bg = 'blue', relief = 'groove', bd = 2)
        self.f_mis.place(x = 400,y = 0, width = 160, height = 200)
        
        self.f_mis_ok = Frame(self.root, bg = 'blue', relief = 'groove', bd = 2)
        self.f_mis_ok.place(x = 560,y = 0, width = 20, height = 200)
            
        self.f_mis_fail = Frame(self.root, bg = 'blue', relief = 'groove', bd = 2)
        self.f_mis_fail.place(x = 580,y = 0, width = 20, height = 200)

        self.f_list_note = Frame(self.root, bg = 'blue', relief = 'groove', bd = 2)
        self.f_list_note.place(x = 400,y = 200, width = 200, height = 200)

    def init_notes(self):
        self.arr_note_text = ['Drawing Profile and more',
                              'Sport easy',
                              'Reading books',
                              'Coding Python, C#, HTML and more',
                              'Sciense, Psihology, Programming',
                              'Have dreams',
                              'Satanic, Anarhys',
                              'Logical see in live',
                              "Don't Static",
                              'and there',]
        self.Pos_note = 0
        for i in range(10):
            self.n = Label(self.f_list_note, text = self.arr_note_text[i])
            self.n.config(anchor = 'w')
            self.n.place(x = 0,y = self.Pos_note, width = 200, height = 20)
            self.Pos_note += 20



    def init_lb_and_bt_for_mission(self):
        self.POS = 0
        for i in range(10):
            self.arr_label_for[i] = Label(self.f_mis, text = self.arr_text_mission[i])
            self.arr_label_for[i].config(anchor = 'w')
            self.arr_label_for[i].place(x = 0,y = self.POS, width = 160, height = 20)
            self.arr_btn_for[i].place(x = 0,y = self.POS, width = 20, height = 20)
            self.arr_btn_for[i]['command'] = self.arr_btn_com[i]
            self.arr_btn_forf[i].place(x = 0,y = self.POS, width = 20, height = 20)
            self.arr_btn_forf[i]['command'] = self.arr_btn_comf[i]
            self.POS += 20



        
    def init_watch(self):
        l_name_watch = Label(self.f_watch, text = 'TIME NOW', font = 'None 30')
        l_name_watch.place(x = 0,y = 0, width = 400, height = 170)

        self.watch = Label(self.f_watch, font = 'magneto 58')
        self.watch.place(x = 0,y = 100, width = 400, height = 250)

        self.watch_local = Label(self.f_watch_local)
        self.watch_local.place(x = 0,y = 0, width = 200, height = 50)

        self.watch_optimal = Label(self.f_watch_optimal)
        self.watch_optimal.place(x = 0,y = 0, width = 200, height = 50)
        
    def tick_time(self):
        self.root.after(1,self.tick_time)
        self.watch['text'] = time.strftime('%H:%M:%S')
        self.watch_local['text'] = time.strftime('%H:%M:%S')
        self.watch_optimal['text'] = time.strftime('%H:%M:%S')
        
        
    def loop_win(self):
        self.root.mainloop()




b = B()

b.init_win()

b.init_param_win()
b.init_frames()
b.init_lbl()
b.init_btn_ok()
b.init_btn_fail()
b.init_lb_and_bt_for_mission()
b.init_notes()
b.init_watch()
b.tick_time()



b.loop_win()
