This is my Journey through the Development of this Board,

![thumbnail_1000082597](https://github.com/user-attachments/assets/92e8ad54-e1f6-484d-a9cf-a4f11859e17e)

The First phase of this project was looking for an API for this to work with, I found this API ("https://openweathermap.org/current") which looked easy enough to use which was good as i had never used an API before, so this was a good opportunity to conduct some research into it,

Once this was one i then got to trying to get results out of it, which was more difficult then i imagined, this is because it was in a nested Python Object, once i had figured this out, i got the following result

![image](https://github.com/user-attachments/assets/e0240f59-168b-4645-ad00-7334e47b8f1a)

I then got to having user Input accepted into the code for 2 reasons, the first is becasue it allows for more interactivity with the software, and the second is because it allow for me to test that the output is changing and not staying the same

![thumbnail_image](https://github.com/user-attachments/assets/0f1bd3b0-2875-4690-b5e9-03bd7480ec1c)


I then decided to try and put it on the WaveShare P3, This was a oppertunity for me to learn how to do this as i had 0 experience before with anything like this. When i first got the WaveShare P3, it was messing up and not displaying properly. After doing alot of resetting and troubleshooting, I found out that this error is because a plastic piece had snapped off which meant the matrix portal S3 was not aligning properly on the Waveshare P3, this was resolved by switching out one WaveShare P3 for another

The next step was just getting some basic output board and check i could get some working, i did this with 3 different coloured triangles, as this seemed like a smart first step to getting me familiar with the coding structure of the board

![thumbnail_1000082596](https://github.com/user-attachments/assets/0dd0abf5-bdbd-4f82-b64f-5ab175087973)

The next step was working out how to get text onto the board and put where i wanted it, this was fun as i had to look into the "from adafruit_display_text" library, From there i got the general names for all the information i wanted displayed to show up on the board and tested to see if there was layers to this which i did via a red rectangle

![thumbnail_1000082890](https://github.com/user-attachments/assets/32440518-6911-4380-9c3f-87c26a8e800a)

I then merged the API which i had worked on in the beginning and the board in order to display, this was easy however did not work straight way due to me not having included the WiFi connectivity library withing the code so whilst the code was working, it had no ability to call due to this, Once i did this, it worked however didnt look nice

![thumbnail_1000082367](https://github.com/user-attachments/assets/aabbab57-860e-4087-afde-ed3decf82724)

so i then decided to add what each line was and then tested with changing font colours as well as the shapes fill and outlines, whilst i was happy with the fact it was working, i still didnt like the design

![thumbnail_1000082422](https://github.com/user-attachments/assets/d76beb38-e8f5-4e18-92c6-9746aba83752)

So i then decided to change the design to a sun in a blue sky, to further this i tried to see if there was a time API in which i could try to link with the design to see if i could make it change more dynamically, however i could not find one that showed the exact time, so i decided to leave this, I also decided to remove the humidity, longitude and latitude as this was not critial information in my opinion to be shown, also decided to turn the font to white whilst i get the design right

![thumbnail_1000082892](https://github.com/user-attachments/assets/ef172730-6cf8-40ad-8404-dfaf8e47b727)

I then tried to find a way to outline the text in order to make it pop out more, i could not find a way of doing involving a libary so i tried different colours which did not work as they were too hard to see, so in the end i decided to just dupilcate the code and off set it by one in the X and Y coordinate and also make it black in order to have it pop out 

![thumbnail_1000082597](https://github.com/user-attachments/assets/92e8ad54-e1f6-484d-a9cf-a4f11859e17e)

i then went onto the user input which was more difficult then i thought it would be, this is because since the code is running on the board, i cant use the serial monitor for input, so i first decided to test to see if i can have it read in from a text file, this worked incredebly well as i only had to add the following code

![image](https://github.com/user-attachments/assets/f78fdf2d-afa9-4a16-b6ad-9f10aca11a5f)

from there it was just about making a GUI that didnt run on the board but could write to the "city.txt" file on it. this i did by using a library called TKinter and since i had a decent amount of experience i had got it working pretty quickly.

![image](https://github.com/user-attachments/assets/97202e13-e324-4d95-bebd-946f20a6de72)



