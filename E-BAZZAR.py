from easygui import *
import sys
list=[]
sum=0
z=""
a=""

while 1:
    msgbox("Welcome to E-Bazaar!")

    msg ="In Which Category Do You Wish To Shop Today?"
    title = "Categories"
    choices = ["Appliances","Books", "Fashion","Laptops","Mobiles", "Watches"]
    choice = choicebox(msg, title, choices)
    
    if choice=="Appliances":
        msg ="Which Appliance/s Do You Wish To Shop?"
        title = "Types of Appliances"
        choices = ["Air Conditioners","Kitchen & Home Appliances","Refrigerators", "Washing Machines"]
        choice = choicebox(msg, title, choices)

        if choice=="Air Conditioners":
            msg ="Which Air Conditioner Do You Wish To Buy?"
            title = "Types of Air Conditioners"
            choices = ["Hitachi","LG","Samsung","Voltas","Whirlpool"]
            choice = choicebox(msg, title, choices)

            if choice=="Hitachi":
                msg ="Which Vendor do You Prefer?"
                title = "List Of Vendors"
                choices = [str(choice)+" Store->50000","Croma->80000","Reliance Digital->65000","Vijay Sales->75000"]
                choice = choicebox(msg, title, choices)
     
                if choice==str(choice)+" Store->50000":
                    x=50000
             
                elif choice=="Croma->80000":
                    x=80000

                elif choice=="Reliance Digital->65000":
                    x=65000

                elif choice=="Vijay Sales->75000":
                    x=75000

            elif  choice=="LG":
                msg ="Which Vendor do You Prefer?"
                title = "List Of Vendors"
                choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                choice = choicebox(msg, title, choices)
                    
                if choice==str(choice)+" Store->50000":
                    x=50000
             
                elif choice=="Croma->80000":
                    x=80000

                elif choice=="Reliance Digital->65000":
                    x=65000

                elif choice=="Vijay Sales->75000":
                    x=75000

            elif  choice=="Samsung":
                msg ="Which Vendor do You Prefer?"
                title = "List Of Vendors"
                choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                choice = choicebox(msg, title, choices)

                if choice==str(choice)+" Store->50000":
                    x=50000
             
                elif choice=="Croma->80000":
                    x=80000

                elif choice=="Reliance Digital->65000":
                    x=65000

                elif choice=="Vijay Sales->75000":
                    x=75000

            elif  choice=="Voltas":
                msg ="Which Vendor do You Prefer?"
                title = "List Of Vendors"
                choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                choice = choicebox(msg, title, choices)

                if choice==str(choice)+" Store->50000":
                    x=50000
             
                elif choice=="Croma->80000":
                    x=80000

                elif choice=="Reliance Digital->65000":
                    x=65000

                elif choice=="Vijay Sales->75000":
                    x=75000

            elif  choice=="Whirlpool":
                msg ="Which Vendor do You Prefer?"
                title = "List Of Vendors"
                choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                choice = choicebox(msg, title, choices)


        elif choice=="Kitchen & Home Appliances":
            msg ="Where Do Wish To Shop?"
            title = "Types of Appliances"
            choices = ["Kitchen","Home"]
            choice = buttonbox(msg, title, choices)

            if choice==str(choice)+" Store->50000":
                    x=50000
             
            elif choice=="Croma->80000":
                    x=80000

            elif choice=="Reliance Digital->65000":
                    x=65000

            elif choice=="Vijay Sales->75000":
                    x=75000

            if choice=="Kitchen":
                msg ="Which Kitchen Appliance  Do You Wish To Buy?"
                title = "Types of Kitchen Appliance"
                choices = ["Coffee Machines","Electric Kettles","Food Processors","Induction Cooktops","Juicers"]
                choice = choicebox(msg, title, choices)

                if choice=="Coffee Machines":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

                elif  choice=="Electric Kettles":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

                elif  choice=="Food Processors":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

                elif  choice=="Induction Cooktops":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)
 
                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

                elif  choice=="Juicers":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

            else:
                msg ="Which Home Appliance  Do You Wish To Buy?"
                title = "Types of Home Appliance"
                choices = ["Air Coolers","Iron","Sweing Machines","Vaccum Cleaners","Water Purifiers"]
                choice = choicebox(msg, title, choices)

                if choice=="Air Coolers":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

                elif  choice=="Iron":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

                elif  choice=="Sweing Machines":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

                elif  choice=="Vaccum Cleaners":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

                elif  choice=="Water Purifiers":
                    msg ="Which Vendor do You Prefer?"
                    title = "List Of Vendors"
                    choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                    choice = choicebox(msg, title, choices)

                    if choice==str(choice)+" Store->50000":
                        x=50000
             
                    elif choice=="Croma->80000":
                        x=80000

                    elif choice=="Reliance Digital->65000":
                        x=65000

                    elif choice=="Vijay Sales->75000":
                        x=75000

        if choice=="Refrigerators":
                    msg ="Which Refrigerators Do You Wish To Buy?"
                    title = "Types of Refrigerators"
                    choices = ["Godrej","LG","Panasonic","Samsung","Whirlpool"]
                    choice = choicebox(msg, title, choices)

                    if choice=="Godrej":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

                    elif  choice=="LG":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

                    elif  choice=="Panasonic":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

                    elif  choice=="Samsung":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

                    elif  choice=="Whirlpool":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

        if choice=="Washing Machines":
                    msg ="Which Washing Machines Do You Wish To Buy?"
                    title = "Types of Washing Machines"
                    choices = ["Godrej","LG","Panasonic","Sansui","Whirlpool"]
                    choice = choicebox(msg, title, choices)

                    if choice=="Godrej":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

                    elif  choice=="LG":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

                    elif  choice=="Panasonic":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

                    elif  choice=="Sansui":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

                    elif  choice=="Whirlpool":
                        msg ="Which Vendor do You Prefer?"
                        title = "List Of Vendors"
                        choices = [str(choice)+" Store","Croma","Reliance Digital","Vijay Sales"]
                        choice = choicebox(msg, title, choices)

                        if choice==str(choice)+" Store->50000":
                            x=50000
             
                        elif choice=="Croma->80000":
                            x=80000
 
                        elif choice=="Reliance Digital->65000":
                            x=65000

                        elif choice=="Vijay Sales->75000":
                            x=75000

       if choice=="Books":
          msg ="Which Book/s Do You Wish To Shop?"
          title = "Books By Genre"
          choices = ["Art","Biography","Children's", "Classics","Fiction","History","Horror","Mystery","Poetry","Psychology","Romance","Science","Science Fiction","Thriller","Travel"]
          choice = choicebox(msg, title, choices)

         if choice=="Art":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Biography":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Children's":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Classics":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Fiction":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        if choice=="History":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Horror":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Mystery":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Poetry":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Psychology":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        if choice=="Romance":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","Reliance Digital"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Science":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Science Fiction":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Thriller":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

        elif  choice=="Travel":
            msg ="Which Vendor do You Prefer?"
            title = "List Of Vendors"
            choices = ["Crossword","Library","The Book Store"]
            choice = choicebox(msg, title, choices)

            elif choice=="Crossword":
                x=80000
 
            elif choice=="Library":
                x=65000

            elif choice=="The Book Store":
                x=75000

    if choice=="Fashion":
        msg ="Where Do Wish To Shop?"
        title = "Shop For?"
        choices = ["Children's Fashion","Men's Fashion","Women's Fashion"]
        choice = buttonbox(msg, title, choices,image="Fashion.png")

        if choice=="Children's Fashion":
            msg ="Which Vendor do You Prefer?"
            title = "Sop From?"
            choices = ["Chicco","Cartoon Network","Ginni & Jony","Lilliput","Skip Hop"]
            choice = choicebox(msg, title, choices)

            if choice=="Chicco":
                x=80000
 
            elif choice=="Cartoon Network":
                x=65000

            elif choice=="Ginni & Jony":
                x=75000

            elif choice=="Lilliput":
                x=65000

            elif choice=="Skip Hop":
                x=75000

        elif  choice=="Men's Fashion":
            msg ="Which Vendor do You Prefer?"
            title = "Shop From?"
            choices = ["Allen Solly","Arrow","Benetton","Levi's","Park Avenue","Pepe Jeans","Raymond","Wrangler"]
            choice = choicebox(msg, title, choices)

            if choice=="Allen Solly":
                x=80000
 
            elif choice=="Arrow":
                x=65000

            elif choice=="Benetton":
                x=75000

            elif choice=="Levi's":
                x=65000

            elif choice=="Park Avenue":
                x=75000

            elif choice=="Pepe Jeans":
                x=75000

            elif choice=="Raymond":
                x=65000

            elif choice=="Wrangler":
                x=75000

        elif  choice=="Women's Fashion":
            msg ="Which Vendor do You Prefer?"
            title = "Shop From?"
            choices = ['Chanel', 'Dolce & Gabbana', 'Giorgio Armani', 'Gucci', 'Hugo Boss', 'Louis Viutton', 'Prada', 'Tiffany & Co.']
            choice = choicebox(msg, title, choices)

            if choice=="Chanel":
                x=80000
 
            elif choice=="Dolce & Gabbana":
                x=65000

            elif choice=="Giorgio Armani":
                x=75000

            elif choice=="Gucci":
                x=4000
                else:
    sys.exit()
