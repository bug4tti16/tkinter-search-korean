import customtkinter as ctk
from jamo import h2j
from pynput.keyboard import Key, Controller
from functools import partial

class SEARCH_FRAME(ctk.CTkFrame):
    def __init__(self,container,entrycontainer,users,number_of_buttons):
        super().__init__(container,width=300)
        self.QUEUE=None
        self.N=number_of_buttons
        self.ENTRY=ctk.CTkEntry(entrycontainer,font=('suit',16,'bold'),placeholder_text='입력...')
        self.BUTTON=self.BUTTONS(number_of_buttons)
        self.ENTRY.bind('<Return>',lambda event:self.ENTER_PRESSED(users))
        self.ENTRY.bind('<KeyRelease>',lambda event:self.KEY_PRESSED(users))
        for x in self.BUTTON:
            x.pack(fill='x',side='bottom')
                
    def BUTTONS(self,n):
        l=[]
        for i in range (n):
            l.append(ctk.CTkButton(self,fg_color='transparent',text='',command=None,text_color=('Black','white'),state='disabled',font=('suit',16,'bold')))
        return l
    
    def UPDATE_BUTTONS(self,userlist):
        if len(userlist)>self.N:
            for x in range (self.N):
                self.BUTTON[x].configure(text=f"{userlist[x]}")
                self.BUTTON[x].configure(command=partial(self.RETURN_UID,userlist[x]))
                self.BUTTON[x].configure(state='normal')

        else:        
            for x in range (len(userlist)):
                self.BUTTON[x].configure(text=f"{userlist[x]}")
                self.BUTTON[x].configure(command=partial(self.RETURN_UID,userlist[x]))
                self.BUTTON[x].configure(state='normal')
    
    def CLEAR_BUTTONS(self):
        for x in self.BUTTON:
            x.configure(text='',command=None,state='disabled')
    
    def CLEAR_ENTRY(self):
        Controller().press(Key.right)
        self.ENTRY.delete(0,'end')

    #엔터 입력시
    def ENTER_PRESSED(self,ul):
        Controller().press(Key.right)
        entered=(self.ENTRY.get())
        if entered!='':
            self.CHECK_NAME(h2j(entered),ul)

    #이름 확인
    def CHECK_NAME(self,NAME,ul):
        output=[]
        for x in ul:
            if NAME==h2j(x):
                output.append(x)
        if len(output)>1:
            self.UPDATE_BUTTONS(output)
        if len(output)==1:
            self.RETURN_UID(output[0])
        
    #타자 입력시
    def KEY_PRESSED(self,ul):
        self.CLEAR_BUTTONS()
        entered=h2j(self.ENTRY.get())
        if entered=="":
            pass
        else:
            self.CHECK_SYLABLE(entered,ul)

    #이름 확인 (자모)
    def CHECK_SYLABLE(self,TYPE,ul):
        output=[]
        output2=[]
        for users in ul:
            cnt=0
            if len(TYPE)<=len(h2j(users)):
                for x in range (len(TYPE)):
                    if list(TYPE)[x]==list(h2j(users))[x]:
                        cnt+=1
                if cnt==len(TYPE):
                    output.append(users)
                if cnt>1 and cnt==len(TYPE)-1:
                    output2.append(users)
        output=output+output2
        if len(output)>0:
            self.UPDATE_BUTTONS(output)

    #이름 표출
    def RETURN_UID(self,UID):
        if UID!=None:
            self.QUEUE=UID
            print (UID)
        self.CLEAR_BUTTONS()
        self.CLEAR_ENTRY()




if __name__ =="__main__":

    l=['포르쉐','포르리','포세이돈','벤틀리','벤츠','비엠더블유','아우디','아이언맨','오펠','현대','기아','케이지 모빌리티','대우']
    root=ctk.CTk()
    s=SEARCH_FRAME(root,root,l,5)
    s.pack()
    s.ENTRY.pack()
    root.mainloop()