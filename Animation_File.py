####################################################################################################################

# Made by: Emre Cenk
# Date started: October 25, 2020
# Last Updated: October 30, 2020

####################################################################################################################
from time import sleep
from tkinter import *
from random import *
from math import *
from Background import builder #The background file is in the other document in the same directory

integer_answer=False
while integer_answer==False:
    try:
        firework_num=int(input("How many fireworks would you like to watch? "))
        integer_answer=True
    except:
        pass



windowy = 600
windowx = 800
interface = Tk()

screen = Canvas(interface, width=windowx, height=windowy, background="black")
screen.pack()


#The following functions pushes the window above all other tabs
interface.lift()
interface.attributes('-topmost',True)

# I will be creating a builder class ( the code for the builder is in the other python document)
# The reason I used classes and functions is because: a) This way I can create buildings in any of my projects. And
# b) The syntax is extremely clean. I find that this way the code is much easier to read and write.
builder = builder(screen=screen) #Creaiting the class

#Drawing the background images: (variables a,b,c,d and e are the buildings and houses in the background of the
# animation):

a = builder.build_classical_building(100, 75, 600, 200,building_color="gray20")
b = builder.build_classical_building(200, 50, 600, 125,building_color="gray20")
c = builder.build_classical_building(300, 60, 600, 180,building_color="gray20")
d= builder.build_classical_building(500,80,600,160,building_color="gray20")
e = builder.build_house(650,100,600,80)


#List of colors for fireworks:
fena_degil=["plum2","plum","plum1","light yellow","snow1","snow2","snow",
            'LightCyan1',"LightCyan2","cyan","yellow", "red",'turquoise', 'violet red',"deep pink",
            "deep pink2"]

fena_degil.append("blanched almond") # This one's for you Mr.Schattman (also it turns out blanched almond is an amazing
# color for fireworks)

#We have a main for loop that constantly generates fireworks until enough fireworks are generated
#Due to this while loop, the code keeps recycling old variables. Therefore we don't have to worry about the animation
# lagging or memory management. If the person asks for 10^9999999 fireworks, we don't generate them all at once. We
# generate 10 fireworks at a time so we don't get any errors because the person asked for an absurd amount of fireworks.

#Calculating how many loops
remainder=int(firework_num%10)
main_loop_times=int((firework_num-remainder)/10)
for main_loop_number in range(main_loop_times+1):

    # Since we want to automate the process of creating firework types, we will be having arrays store the arrays needed
    # for the fireworks. For instance, instead of storing the velocities of different particles in an array [v1,v2,v3,
    # v4...], we will be storing [ [velocities_of_first_firework1,velocities_of_first_firework2...],
    # [velocities_of_second_firework1...] ...].
    # Basically, it will be arrays inside of arrays storing the necessary values


    # Note: if the variable name has _fireworks as the last word, that means that array is storing different arrays for
    # each firework. If the variable does not end with _fireworks, that means that array stores values.

    ball_objects_fireworks = []  # Will store the particle objects in each firework in different arrays
    angles_fireworks = [] # Will store the angles of each particles in each firework
    radii_of_particles_fireworks = []  #Will store the radius of each particle in each firework

    vx_fireworks = []   #Will store the x velocity of each particle in each firework
    vy_fireworks = []   #Will store the y velocity of each particle in each firework
    frame_number = []  # How many frames each firework will stay on screen
    frames_seen=[] #How many frames each firework has been seen for (the initial value will be 0 for all fireworks)

    firework_color=[] #Will store which colour each firework is going to be
    ball_numbers = []  # Will store the amount of balls needed for each firework

    glide_time=[] #How long the firework particles will glide for after fully exploding
    xcenters_fireworks = []  # Will store each particle's center x coordinate
    ycenters_fireworks = []  # Will store each particle's center y coordinate (the initial value for all particles in a
    # given firework will equal to the center of the explosion)

    interval_v = 2 # The velocity interval

    if main_loop_number==0:
        number_of_fireworks=remainder#This is how many fireworks are in THIS loop, not overall fireworks number
    else:
        number_of_fireworks = 10 #This is how many fireworks are in THIS loop, not overall fireworks number

    xcenter = 100
    ycenter = 100

    # Generating as many fireworks as needed:
    for j in range(number_of_fireworks):
        ball_num = randint(30,95) #interval of number of particles on each firework

        #The following arrays are going to be appended onto the main arrays:
        balls = []
        angles = []
        r = []
        xs = []
        ys = []
        vx = []
        vy = []

        #Updating the coordinates so that all fireworks are in different locations:
        xcenter += (windowx-200)/number_of_fireworks
        ycenter = ycenter + randint(-5,10)


        # Filling the place-holder arrays in:
        for i in range(ball_num):
            # In this nested for loop, we are generating the arrays that will go inside of arrays
            a=[]

            balls.append(0)
            angles.append(uniform(0, 2 * pi))
            r.append(randint(4,5))
            xs.append(xcenter)
            ys.append(ycenter)
            vx.append(uniform(-interval_v*1.1, interval_v*1.1))
            vy.append(uniform(-interval_v, interval_v))

        #Now, we will append the arrays created in the nested for loop above into the main variables:
        #If the array requires integers and not arrays, the values will be appended accordingly.
        ball_objects_fireworks.append(balls)
        angles_fireworks.append(angles)
        radii_of_particles_fireworks.append(r)
        xcenters_fireworks.append(xs)
        ycenters_fireworks.append(ys)
        vx_fireworks.append(vx)
        vy_fireworks.append(vy)

        #These arrays will not have arrays inside them:
        frame_number.append(randint(17,34)) #Random duration
        glide_time.append(randint(0,12)) #random glide time

        firework_color.append(fena_degil[randint(0,len(fena_degil)-1)]) #random color 1 color





    # Each firework will have a rocket that launches it up into the sky. We will now create the neccesary arrays for
    # those rockets:

    rocketsx = []  # Rocket x coordinates
    rocketsy = []  # Rocket y coordinates
    rocketsv = []  # Rocket velocities
    rocket_body_objects = []  # Will be storing the rocket's body as objects
    rocket_radii = []  # Stores the radius of rockets
    rocket_start_frame = [] #Which frame the rocket will start to fly
    rocket_n = []   # Rocket coefficient. Each rocket's coefficient will slightly slow the rocket down as the rocket
    # flies up. This will create a very slight illusion that the rockets weights are different.

    rocket_tail_objects=[] #Stores the tails objects of the rockets
    rocket_head_object=[] #Stores the head objects of the rocket
    animate_firework = []  # Keeping track of if we are animating the firework or rocket. If it has True, that means we are
    # animating the firework. If it is false, that means we are animating the rocket. The initial value will be False
    # since we will be starting out by animating the rocket

    initial_start=30
    # Filling the rocket arrays with either place holders or values :
    for i in range(number_of_fireworks):

        rocketsx.append(xcenters_fireworks[i])
        rocketsy.append(windowy - 100)
        rocketsv.append(uniform(14, 18))

        rocket_body_objects.append(0)
        rocket_tail_objects.append(0)
        rocket_head_object.append(0)

        rocket_radii.append(randint(4, 7))
        animate_firework.append(False)
        rocket_start_frame.append(initial_start)
        initial_start+=randint(20,40)
        rocket_n.append(0)
        frames_seen.append(0)




    shuffle(rocket_start_frame) #Shuffling the starting frames of each rocket so they go off in random order:



    setoff=[] #This will store which fireworks have fully exploded. It needs to be an array to avoid counting the same
    # firework each time

    # Starting the main loop:
    frame=0 #Which frame number we are on. We will add 1 to it at the end of the loop
    while len(setoff)<number_of_fireworks: #This is to make sure the loop ends when all fireworks fully explode and glide

        # Going through each firework and rocket:
        for i in range(number_of_fireworks):
            # i here is the index for each firework

            # Checking if the rocket is at the desired height (I.e are we animating the rocket or firework):
            if animate_firework[i] == False:

                if rocket_start_frame[i] <= frame:
                    # At this point the rocket is still under the desired height

                    # Updating the coordinates and coefficient of the rocket
                    rocketsy[i] -= rocketsv[i] - rocket_n[i] ** 2
                    rocket_n[i] += 0.009

                    #The coordinates for the rocket will be in rc:
                    rc=[rocketsx[i][0] - rocket_radii[i], rocketsy[i] - rocket_radii[i],rocketsx[i][0] + rocket_radii[i],
                       rocketsy[i] + rocket_radii[i],]
                    rocket_body_objects[i] = screen.create_oval(rc[0], rc[1], rc[2], rc[3],
                                                                fill="light green")

                # Checking if rocket is ready to explode:
                if rocketsy[i] < ycenters_fireworks[i][0]:
                    # At this point, the rocket is at the height that is desired, in order to start animating the
                    # firework when the loop repeats, we set the animate_firework variable to true
                    animate_firework[i] = True
                    screen.delete(rocket_body_objects[i])

                    # Since at this point we know we will never need to animate the rocket with index i again, we might as
                    # well entirely clear it out of memory after deleting it
                    rocketsx[i] = 0
                    rocketsy[i] = 0
                    rocketsv[i] = 0
                    rocket_body_objects[i] = 0
                    rocket_radii[i] = 0
                    rocket_start_frame[i] = 0
                    rocket_n[i] = 0

            elif frames_seen[i]<=frame_number[i]:
                # At this point, we know the rocket has exploded, we will be animating the fireworks (the firework is
                # still in the air, it has not started the gliding process yet)

                #ball_num[i] is the same thing as len(radii_of_particles_fireworks[i])
                for k in range(len(radii_of_particles_fireworks[i])):
                    # k is the particle index
                    # I will be using [i][k] to refer to the current particle since we are on the i indexed fireworks k
                    # indexed particle.
                    radii_of_particles_fireworks[i][k] = radii_of_particles_fireworks[i][k] - 4 / frame_number[i]

                    # Updating the x coordinates for each particle:
                    xcenters_fireworks[i][k] = xcenters_fireworks[i][k] + radii_of_particles_fireworks[i][k] * cos(
                        angles_fireworks[i][k]) + vx_fireworks[i][k]

                    # Updating the y coordinates for each particle:
                    ycenters_fireworks[i][k] = ycenters_fireworks[i][k] - radii_of_particles_fireworks[i][k] * sin(
                        angles_fireworks[i][k]) + vy_fireworks[i][k] + 0.005*frames_seen[i]**2

                    #Drawing the particle (xcenter_fireworks[i][k] and ycenter_fireworks[i][k] are the coordinates of the
                    # center of the particle, all we need to do at this point is just plug in the values x-radius,y-radius,
                    # x+radius,y+radius in as coordinates:
                    ball_objects_fireworks[i][k] = screen.create_oval(
                        xcenters_fireworks[i][k] - radii_of_particles_fireworks[i][k],
                        ycenters_fireworks[i][k] - radii_of_particles_fireworks[i][k],
                        xcenters_fireworks[i][k] + radii_of_particles_fireworks[i][k],
                        ycenters_fireworks[i][k] + radii_of_particles_fireworks[i][k]
                        , fill=firework_color[i],outline=firework_color[i])


                frames_seen[i]+=1
            elif frames_seen[i]-glide_time[i] <= frame_number[i]:
                # At this point, the fireworks are about to burn out, their particles are as thin as possible.
                # Due to this reason, we will not be updating the radius of the particles. We will simply let the
                # particles glide freely in the air for a while before deleting the animated firework
                for k in range(len(radii_of_particles_fireworks[i])):
                    # Updating the x coordinates for each particle::
                    xcenters_fireworks[i][k] = xcenters_fireworks[i][k] + radii_of_particles_fireworks[i][k] * cos(
                        angles_fireworks[i][k]) + vx_fireworks[i][k]/2

                    ycenters_fireworks[i][k] = ycenters_fireworks[i][k] - radii_of_particles_fireworks[i][k] * sin(
                        angles_fireworks[i][k]) + vy_fireworks[i][k]/2 + 0.005*frames_seen[i]**2

                    ball_objects_fireworks[i][k] = screen.create_oval(
                        xcenters_fireworks[i][k] - radii_of_particles_fireworks[i][k],
                        ycenters_fireworks[i][k] - radii_of_particles_fireworks[i][k],
                        xcenters_fireworks[i][k] + radii_of_particles_fireworks[i][k],
                        ycenters_fireworks[i][k] + radii_of_particles_fireworks[i][k]
                        , fill=firework_color[i],outline=firework_color[i])


                frames_seen[i]+=1


            else:
                #At this point, the firework has burnt out, we will check if it is in the list of burnt out fireworks.
                # This is to ensure that when all fireworks are burnt out, the animation stops
                if i not in setoff:
                    setoff.append(i)



        screen.update()
        sleep(0.03)

        #Deleting fireworks and rockets from the screen:
        for i in range(number_of_fireworks):
            if animate_firework[i] == False:
                screen.delete(rocket_body_objects[i])
            else:
                for particle in ball_objects_fireworks[i]:
                    screen.delete(particle)


        frame+=1

