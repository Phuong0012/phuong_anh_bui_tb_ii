# Report
    Introduction
The main idea behind the creation of this application was to have a "study buddy" that would cheer student on as they study for their exams. This idea was heavilly inspired by the Japanese illustrated short-comics of Koupenchan, a baby emperror penguin that cheers the readers on throghout theur daily life. I wanted to create something simple that would be functional and bring a little more happiness into the user's lives.
The application mainly works as a timer and a to-do list which its users can input their to-dos for that session and set their study break timers, to help them keep track of time and not skip breaks. Lastly each tiem the user checks off a to-do off his list he recieves some cheerful words of praise from his buddy.

    Methodology
The code for this application is a combination of code used in class and code outsourced from the internet. The UI portions of the application, such as the individual pages, widgets such as buttons, input fields and text labels use code from our classes.The first section that uses outsourced code is the timer function. It is based on the code of “Parvat Computer Technolo” on youtube. The code can be found in the “Break_Timer” and “Work_Timer” definitions. These definitions use the user input to count down time. The code itself is responsible for the action of counting down and updating the numbers displayed to the user. The two definitions are identical with one difference. That difference being that at the end of the Break_Timer it destroys the timer window, sending the user back to the main page with his study buddy. It also activates the “choice_window” pop-up that gives the user the choice to either restart the timer or to open his to-do list to mark his task as “done”.
The second section that uses outsourced code is the to-do list. It can be found in the “to_do”, “to_doNewWindow”, “open_task_file”, “deleteTask”, “taskDone” and “add_task” definitions. The code in these definitions is an amalgamation of the code from “codemy.com”, “CODE ROOM” and “Parvat Computer Technolo” on youtube. These definitions are responsible for the saving of the user input (to-dos) into a list, their display and the possibility to further work with them – mark them as done or delete them.

    Limitations
The main limitation I have encountered during the development of this MVP was within the timer. After the “Work_Timer” finishes its run there seems to be a slight delay before the “Break_Timer” starts. This seems to be a limitation of the currently used method for the display of the numbers. So far, I have unfortunately not been able to find a method that would allow a smoother run of the timer.
Additionally, when using the custom timer, the user has to first set the work timer, after that finishes they are given the chance to set their break timer. I had initially planned for the user to be able to set both their timers before starting the session in order to avoid wasting time. However, it was not possible to for both timers to run smoothly, as the second one could not update the timer shown to the user. After attempting to debug this issue, I have learned that this was a limitation of tkinkter and that it could not run 2 functions such as these at the same time.
Lastly, I was planning on adding small movements to the Study Buddy, small jumps or shakes based on user interactions. However, I have encountered the problem of not being able to scale down the movement. The image would often move too much and when I was able to contain it to a smaller space, the movements were too fast and erratic. This did not fit the image I had planned as it seemed rather stressful and not calming and cute. Therefore, I had to give up on this idea for now and focus purely on the functionality of this app rather than the visuals.