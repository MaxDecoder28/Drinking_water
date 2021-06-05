import time
from plyer import notification

if __name__ == "__main__":
    # while(True):
        notification.notify(
            title = "Please drink water Now!!",
            message = "The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men About 11.5 cups (2.7 liters) of fluids a day for women These recommendations cover fluids from water, other beverages and food.",
            app_icon = ('C:\\Users\\user1\\Desktop\\MyPYTHON\\Practice Python\\drinking water\\icon.ico') ,
            timeout = 5
        )
        
        # time.sleep(6)
        # time.sleep(60*60)