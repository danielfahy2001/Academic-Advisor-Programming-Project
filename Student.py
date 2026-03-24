from MailingAddress import MailingAddress #remove after debugging
from Email import Email
from Phone import Phone
from Date import Date
#Run this with shift f10 to get a printed student
class Student:
    def __init__(self, name=None, sid=None, mailing_address=None,emails=None,phones=None,bdate=None,adate=None,semester="Spring 2026",major="Undeclared"):
        self.__name = name #String, first, middle, last
        self.__sid = sid #int
        self.__mailing_address = mailing_address #object address
        self.__emails = emails #list of objects, email
        self.__phones = phones #list of objects, phones
        self.__birth_date = bdate #birthdate, use date class
        self.__accept_date = adate #acceptance date, use date class
        self.__semester = semester #string, ie: "Spring 2026"
        self.__major = major #string


    def __str__(self):
        s = f"Name: {self.__name}\n"
        s += f"Student id: {self.__sid}\n"
        s += f"Mailing address: {self.__mailing_address}\n"
        for email in self.__emails:
            s += f"{email}\n"
        for phones in self.__phones:
            s += f"{phones}\n"
        s += f"Birth date: {self.__birth_date}\n"
        s += f"Accept date: {self.__accept_date}\n"
        s += f"Semester: {self.__semester}\n"
        s += f"Major: {self.__major}\n"
        return s
    def get_name(self): #Getter chain, nothing special really.
        return self.__name
    def get_sid(self):
        return self.__sid
    def get_mailing_address(self):
        return self.__mailing_address
    def get_emails(self):
        return self.__emails
    def get_phones(self):
        return self.__phones
    def get_birth_date(self):
        return self.__birth_date
    def get_accept_date(self):
        return self.__accept_date
    def get_semester(self):
        return self.__semester
    def get_major(self):
        return self.__major

    def set_name(self,name): #Setter chain.
        self.__name = name
    def set_sid(self,sid):
        self.__sid = sid
    def set_mailing_address(self,mailing_address):
        self.__mailing_address = mailing_address
    def set_emails(self,emails):
        self.__emails = emails
    def set_phones(self,phones):
        self.__phones = phones
    def set_birth_date(self,birth_date):
        self.__birth_date = birth_date
    def set_accept_date(self,accept_date):
        self.__accept_date = accept_date
    def set_semester(self,semester):
        self.__semester = semester
    def set_major(self,major):
        self.__major = major


if __name__ == '__main__': #Quick test for printing methods, use for debug
    michael_address = MailingAddress("50 Somewhere Ln.","Philly","PA",11111,"Home")
    michael_email = Email("notrealemail@spammail.com","Personal")
    michael_phone = Phone("123-45-6789","Cell")
    michael_birthday = Date("2001",1,1)
    michael_accept_date = Date("2002",1,1)
    michael = Student("Michael Franklin Phillips",23232,michael_address,[michael_email],[michael_phone],michael_birthday,michael_accept_date,"Spring 2026","Comp Sci")
    print(michael)