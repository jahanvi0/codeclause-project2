from playsound import playsound
print("No. of avaliable songs\n1.tera hua\n2.mai woh chand\n3.dhadak\n4.ghar nahi jana\n5.janabe ali\n6.ajab si\n7.dil to bacccha hai\n8.paisa hai to\n9.sab farzi")
order = input('Enter the music which you want to play: ')
if "tera hua" in order:
    playsound('C:\\Users\\DELL\\Downloads\\tera hua.mp3')
elif "mai woh chand" in order:
    playsound('C:\\Users\\DELL\\Downloads\\mai woh chand.mp3')
elif "dhadak" in order:
    playsound('C:\\Users\\DELL\\Downloads\\dhadak.mp3')
elif "ghar nahi jana" in order:
    playsound('C:\\Users\\DELL\\Downloads\\ghar nahi jana.mp3')
elif "janabe ali" in order:
    playsound('C:\\Users\\DELL\\Downloads\\janabe ali.mp3')
elif "ajab si" in order:
    playsound('C:\\Users\\DELL\\Downloads\\ajab si.mp3')
elif "dil to baccha hai" in order:
    playsound('C:\\Users\\DELL\\Downloads\\dil to baccha hai.mp3')
elif "paisa hai to" in order:
    playsound('C:\\Users\\DELL\\Downloads\\paisa hai to.mp3')
elif "sab farzi" in order:
    playsound('C:\\Users\\DELL\\Downloads\\sab farzi.mp3')               
    