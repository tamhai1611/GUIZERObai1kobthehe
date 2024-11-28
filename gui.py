from guizero import App,Text,Picture,PushButton
app = App()
count = 1
def switch():
    global count
    count += 1
    picture.image = f"images/beluga{count}.gif"
app.bg = "yellow"

text = Text(app, text="Wanted", size=60)

picture = Picture(app, image= "images/beluga1.gif")

button = PushButton(app, text= "click here",command= switch)

app.display()