from status import Status

class Menu:
    def __init__(self):
        self.status = Status()
        self.choices = {
            "1": self.show_ip,
            "2": self.show_page,
            "3": self.quit
        }

    
    def display(self):
        print("""
        Menu
        1. Show the ip address
        2. Show if pages of website are available""")


    def run(self):
        while True:
            self.display()

            choice = input("Enter your choice:")
            action = self.choices.get(choice)

            if action:
                action()

            else:
                print("Not a valid choice")


    def show_ip(self,ip=None):


        host = input(str("Enter the host name:"))


        
        if not ip:
            ip = self.status.get_ip(host)
            print(ip)


    def show_page(self):
        host = input(str("Enter the host name:"))
        self.status.page_information(host)


    def quit(self):
        print("Thank You")
        sys.exit(0)



if __name__ == "__main__":
    Menu().run()


