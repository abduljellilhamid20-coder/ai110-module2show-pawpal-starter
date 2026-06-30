# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
I designed four classes for PawPal+. The Task class holds one activity like a walk or feeding, with a time, duration, priority, and frequency.
The Pet class stores a pet's name and breed and holds a list of tasks. The Owner class stores the owner's name and manages multiple pets. 
The Scheduler class is the brain as it takes the owner's data and organizes all tasks by sorting, filtering, and detecting conflicts.

**b. Design changes**
My design did not change much overall, but I did add some logic that was not in my first plan. When I first sketched the classes, the methods like mark_complete and add_task were empty placeholders. 
As I built the project with AI help, I added the actual logic inside those methods, like making mark_complete also create a new task for the next day if it repeats. 
I also added the conflict detection logic to the Scheduler after I had already tested the basic schedule and noticed two tasks could be set at the same time.
 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**
My scheduler mainly looks at time to put tasks in order from morning to night. It can also filter tasks by which pet they belong to or whether they are done or not. 
It checks if two tasks have the same time and warns about it. 
I decided time was the most important thing to look at because a pet owner needs to know what to do first.

**b. Tradeoffs**
One tradeoff my scheduler makes is that it only checks if two tasks have the exact same time, not if they overlap. 
For example, if one task is at 08:00 for 30 minutes and another task is at 08:15, my scheduler will not catch that as a conflict even though they actually overlap.
I think this is okay for now because checking for exact time matches was simpler to build and still catches the most obvious problem, which is two tasks scheduled at the same start time.

---

## 3. AI Collaboration

**a. How you used AI**
I used Claude as my main AI tool throughout this project. I used it to help me design the classes, point out the errors, and understand what each part of the code was doing.
The most helpful questions were specific ones like asking Claude to explain what a certain class does or asking it to help me find bugs after I have stayed a long time on finding a bug.

**b. Judgment and verification**
One moment I realized what Claude pointed out as a mistake was actually not a mistake, so I had to take time and read through the code myself before asking Claude again to check where the real problem was. 
I had to ask Claude where the code was wrong, debug those parts myself, and replace the issues I found with real working code that used my Owner, Pet, Task, and Scheduler classes. 
I verified it worked by running the app in my browser and testing each button myself.

---

## 4. Testing and Verification

**a. What you tested**
I tested five things in my project. I checked that marking a task complete mostly changes its status to done. I checked that adding a task to a pet increases the number of tasks that pet has. 
I checked that tasks come out in the right time order when sorted. 
I also checked that the scheduler catches two tasks at the same time as a conflict. 
I also checked that a daily task creates a new one for the next day when marked complete. 
These tests were important because they cover the main things the app is supposed to do which is very necessary.



**b. Confidence**

I am pretty confident my scheduler works correctly because all five tests passed. 
If I had more time I would test what happens when a pet has no tasks at all, 
and what happens if someone types a time in the wrong format like "8am" instead of "08:00".

---

## 5. Reflection

**a. What went well**
I am most satisfied with how the scheduler actually works in the app. 
When I clicked "Generate Schedule" and saw the tasks show up in order with a conflict warning, it felt good because I understood what was happening and why. 
Setting up the classes and connecting them to the Streamlit UI was something I did not think I could do at the start.


**b. What you would improve**
If I had another chance I would make the app remember the pets and tasks even after you close the browser. Right now everything resets when you refresh the page.
I would also make the UI look nicer and add a way to mark tasks as done directly in the app instead of just in the code.

**c. Key takeaway**
The biggest thing I learned is that AI generated code is not always complete or correct. You have to test it yourself and understand what each part does. 
I also learned that designing the system first with a UML diagram before writing any code makes everything easier because you already know what you are building.

