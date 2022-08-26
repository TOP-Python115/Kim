from datetime import datetime as dt
import inspect


def counter(func):
    
    def wrapper(*args, **kwargs):
        file_path ="D:/python projects/hw/06.14/log2.txt"
        time_now = dt.now().strftime('%d/%m/%Y, %H:%M:%S')
        saved_args = locals()
        with open(file_path, 'a') as f_in:
            f_in.write(str(time_now) + '\n' + func.__name__ + '\n' + str(Person.__str__(p1)) + '\n' + str(saved_args['args'][2]))
        
    return wrapper 
    
class Person:
    def __init__(self, name: str, login: str, email:str):
        self.name = name
        self.login = login
        self.email = email
    
    def __str__(self):
        return f"name: {self.name}, login: {self.login}, email: {self.email}"
        
    
class TxtMsgSender:
    @counter
    @staticmethod
    def message(Person, text):
        return Person, text
         


p1 = Person("Dima", "asf", "mail.ru")
t1 = TxtMsgSender()
t1.message(p1, "hello")

 

   
