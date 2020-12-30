
class builder:

    def __init__(self, screen):
        # We declare the self.screen variable once to not have to have it as an input every single time.
        self.screen = screen

    def serial_windows(self, basevalue_x, width, basevalue_y, height,
                       building_light_color, building_color):
        objects=[]
        door_height=width/3
        window_number = round((height - door_height) / 15)  # Approximately this many windows will fit into the building
        spacing = (height) / window_number
        margin = round(width / 5.5)
        for i in range(1, window_number - 2):
            # Instead of building windows, we build horizontal lines.
            # In order to make them look like windows, we will have perpendicular line(s) cut through
            objects.append(self.screen.create_line(basevalue_x + margin, basevalue_y - door_height - spacing * i - 4,
                                                   basevalue_x + width - margin,
                                                   basevalue_y - door_height - spacing * i - 4,
                                                   fill=building_light_color, width=6))

        # Drawing the straight line, creating the illusion of windows.
        objects.append(self.screen.create_line(
            basevalue_x + width / 2,
            basevalue_y - height,
            basevalue_x + width / 2,
            basevalue_y - door_height,
            fill=building_color,
            width=width / 3.5))


        return objects

    def build_classical_building(self, basevalue_x, width, basevalue_y, height, door_color="brown",
                                 building_color="gray1", building_light_color="white"):
        # Drawing the building core (the rectangle):

        objects = [self.screen.create_rectangle(basevalue_x, basevalue_y, width + basevalue_x, basevalue_y - height,
                                                fill=building_color, outline=building_color)]

        # Drawing the door:
        door_width = width / 3
        door_height = door_width

        objects.append(
            self.screen.create_rectangle(basevalue_x + door_width, basevalue_y, basevalue_x + door_width * 3 / 2,
                                         basevalue_y - door_height, fill=door_color))

        objects.append(
            self.screen.create_rectangle(basevalue_x + door_width * 3 / 2, basevalue_y, basevalue_x + door_width * 2,
                                         basevalue_y - door_height, fill=door_color))


        windows=self.serial_windows(basevalue_x, width, basevalue_y, height,
                                    building_light_color, building_color)

        #Appending all of the objects from the windows function to our general objects list
        for window in windows:
            objects.append(window)


        return objects

    def build_triangle_head_skyscraper(self, basevalue_x, width, basevalue_y, height, door_color="brown",
                                       building_color="gray1", building_light_color="white"):

        #Drawing the rectangle part of the building:
        body_height=height*9/10
        head_height=height/10
        objects = [self.screen.create_rectangle(basevalue_x, basevalue_y, width + basevalue_x, basevalue_y - body_height,
                                                fill=building_color, outline=building_color)]

        #Drawing the triangle head:
        objects.append(

            self.screen.create_polygon(basevalue_x,basevalue_y-height,
                                      basevalue_x+width,basevalue_y-body_height,
                                      basevalue_x,basevalue_y-body_height,
                                      fill=building_color)
        )

        windows=self.serial_windows(basevalue_x, width, basevalue_y, body_height * 0.96,
                                    building_light_color, building_color)

        for window in windows:
            objects.append(window)

        return windows

    def build_house(self,basevalue_x,width,basevalue_y,height,building_color="gray20",building_light="white",
                    roof_color="indianred3",door_color="brown",door_knob_color="black"):

        body_height=height*0.6

        #Drawing the rectangle part of the house:
        objects = [self.screen.create_rectangle(basevalue_x, basevalue_y, width + basevalue_x, basevalue_y - body_height,
                                                fill=building_color, outline=building_color)]

        #Drawing the roof of the house
        objects.append(self.screen.create_polygon(basevalue_x,basevalue_y-body_height,
                                                  basevalue_x+width,basevalue_y-body_height,
                                                  basevalue_x+(width/2),basevalue_y-height,
                                                  fill=roof_color


        )
        )
        dw=width/6 #Door width
        dh=body_height/2 #door height
        margin=(width-dw)/2 #margin space

        #Drawing the door:
        objects.append(
            self.screen.create_rectangle(
                basevalue_x+margin,basevalue_y,
                basevalue_x+width-margin, basevalue_y-dh,
                fill=door_color,
                outline=door_color ))

        #Drawing door knob
        radius=dh/8
        objects.append(
            self.screen.create_oval(
                basevalue_x + width-margin, basevalue_y-(dh/2),
                basevalue_x + width-margin-radius, basevalue_y+radius-(dh/2),
                fill=door_knob_color

            )
        )


        return objects









