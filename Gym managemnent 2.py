
class Gym:
    def __init__(self):
       self.Membership={}
       self.Active={}
       self.Enquiry={}
    def Member(self):
        mem=input("Enter the Name :")
        if mem.isdigit():
            print("Please Re Enter the Name")
        else:
            Age=int(input("Enter The Age :"))
            if Age<15:
                print("*****Incorrect Age*****")
            else:
                Gender=input("Enter the Gender :")
                Mobile=input("Enter the Mob.No. :")
                ID=input("ASSIGN ID :")
                Email=input("Enter the Email :") 
                if "@gmail.com" in  Email:
                    print("Thanks For Joining")
                    self.Active.update({ID:[mem,Age,Gender,Mobile,Email]}) 
                else:
                  print("xx-xx-xx-xx-xxx-xx-xx-Invalid to Registered-xx-xx-xx-xx-xxx-xx-xx")
    def Package(self):
        while(True):
           print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
           print("Please Choose The Package")
           print("1:Gold \n2:Silver \n3:Bronze \n4:Exit") 
           print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
           Choice=input("Enter the Choice :")
           if Choice in["1","2","3","4"]:
               if Choice=="1":
                  print("Consist of 1.5 year membership with Personal Trainer")
                  Y=input("Would You Like Active The Package YES/NO :")
                  if "Yes" or "yes" in Y:
                        print("Your Package Has Been Activate")
                        self.Membership.update({"Package":"Gold"})
                  elif "No" or "no" in Y:
                                    print("Thank you")
                                    break
                  else:
                      print("xx-xx-xx-xx-xxx-xx-xx-Invalid Choice-xx-xx-xx-xx-xxx-xx-xx")
               elif Choice=="2":
                       print("Consist Of 1 year membership with personal trainer for 6 months")
                       W=input("Would You Like Active The Package YES/NO :")
                       if "Yes" or "yes" in W:
                                    print("Your Package Has Been Activate")
                                    self.Membership.update({"Package":"Silver"})
                       elif "No" or "no" in W:
                                    print("Thank You")
                                    break
                       else:
                         print("Invalid Choice")
               elif Choice=="3":
                     print("Consist of 1 year membership and with personal trainer for One month ")
                     N=input("Would You Like Active The Package YES/NO :")
                     if "Yes" or "yes" in N:
                              print("Your Package Has Been Activate")
                              self.Membership.update({"Package":"Bronze"})
                     elif "No" or "no" in N:
                               print("Thank You")
                               break
                     else:
                       print("xx-xx-xx-xx-xxx-xx-xx-Invalid Choice-xx-xx-xx-xx-xxx-xx-xx") 
               elif Choice=="4":
                   break
           else:
               print("**** INVAILD CHOICE ****")
        #    self.Membership.update({"Package":__package__})
    def Workout(self):
        print(">>>>>>>>>>>>>>>>>>>>NO PAIN NO GAIN<<<<<<<<<<<<<<<<<<<<<<")
        while(True):
            print("1:Push Pull Leg \n2:Bro Split \n3:BEGINNER \n4:EXIT")
            print(">>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<")
            Choice=input("WHAT WOULD YOU LIKE TO DO IN THIS WEEK  :")
            if Choice in ["1","2","3","4"]:
                if Choice=="1":
                    print("1:MONDAY \n2:TUESDAY \n3:WEDNESDAY \n4:THURSDAY \n5:FRIDAY \n6:SATURDAY \n7:EXIT")
                    choice=input("Enter the choice to show the workout")
                    if choice in ["1","2","3","4","5","6","7"]:
                        if choice=="1":
                               print("->BENCH PRESS \n->CHEST PRESS  \n->TRICEP EXTENSTION  \n->PULL DOWN")
                               print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                        elif choice=="2":
                               print("->LATSPULLDOWN \n->BACKROWING \n->BICEPS CURL \n->PREACHED CURLS")
                               print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                        elif choice=="3":
                               print("->SQUATS \n->LEGPRESS \n->CRUNCHES")
                               print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                        elif choice=="4":
                               print("->BENCH PRESS \n->CHEST PRESS  \n->TRICEP EXTENSTION  \n->PULL DOWN \n->SHOULDER PRESS")
                               print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                        elif choice=="5":
                               print("->LATSPULLDOWN \n->BACKROWING \n->BICEPS CURL \n->PREACHED CURLS \n->DEADLIFT")
                               print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                        elif choice=="6":
                               print("->CARDIO \n->YOGA")
                               print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                               break
                    else:
                        print("Invalid Choice")
                        print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                elif Choice=="2":
                    print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                    print("MONDAY: BACK \nTUESDAY: CHEST \nWEDNESDAY: TRICEPS \nTHURSDAY: BICEPS \nFRIDAY: SHOULDERS \nSATURDAY: LEGS \nSUNDAY: REST")
                    print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                elif Choice=="3":
                     print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X") 
                     print("MONDAY: 15 MINUTES RUNNING \nJUMPING JACKS FOR 30 SEC \n30 BURPEES")  
                     print("TUESDAY: 15 MINUTES RUNNING \nJUMPING JACKS FOR 30 SEC \n30 BURPEES")
                     print("WEDNESDAY: 15 MINUTES RUNNING \nJUMPING JACKS FOR 30 SEC \n30 BURPEES")
                     print("THURSDAY: 15 MINUTES RUNNING \nJUMPING JACKS FOR 45 SEC \n30 BURPEES")
                     print("FRIDAY: 15 MINUTES RUNNING \nJUMPING JACKS FOR 60 SEC \n30 BURPEES")
                     print("SATURDAY: 15 MINUTES RUNNING \nJUMPING JACKS FOR 90 SEC \n30 BURPEES")
                     print("X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X")
                elif Choice=="4":
                    break
            else:
                print("xx-xx-xx-xx-xxx-xx-xx-INVAILD CHOICE-xx-xx-xx-xx-xxx-xx-xx")
    def BMI(self):
           print("CHECK YOUR BODY MASS INDEX")
           weight=int(input("ENTER THE WEIGHT IN LBS :"))
           height=float(input("ENTER THE HEIGHT IN INCHES :"))
           BMI=(weight/(height)**2)*703        
           print("BMI=",BMI)
    def GYMManager(self):
        self.manager_id=input("ENTER THE NAME :")
        if self.manager_id=="Sahil Ayare":
              Password=input("ENTER THE PASSWORD :")
              if Password=="0601":
                   print("X-X-X-X-X-X-X-X- ACCESS GRANTED -X-X-X-X-X-X-X-X")
                   print("\n>>>>>>>>WELCOME MANAGER<<<<<<<<<<")
                   while(True):
                        print("1:ADD MEMBER \n2:PACKAGE \n3:VIEW MEMBER \n4:ENQUIRES \n5:EXIT ")
                        print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
                        choice1=input("ENTER THE CHOICE :")
                        if choice1 in ["1","2","3","4","5"]:
                            if choice1=="1":
                                self.Member()
                            elif choice1=="2":
                                 self.Package()
                            elif choice1=="3":
                                self.Active.update(self.Membership)
                                for i in self.Active.items():
                                      print(i)
                            elif choice1=="4":
                                self.Active.update()
                                for j in self.Enquiry.items():
                                 print(j)
                            elif choice1=="5":
                                break
                        else:
                            print("INVALID CHOICE")
                            
              else:
                   print("xx-xx-xx-xx-xxx-xx-xx-INVALID PASSWORD-xx-xx-xx-xx-xx-xx-xx")
        else:
          print("xx-xx-xx-xx-xxx-xx-xx-INVAILD I'D-xx-xx-xx-xx-xxx-xx-xx")
    def Client(self):
         mem2=input("Enter the I'd :")
         if mem2 in self.Active.keys():
            while(True):
                print("<<<<<<<<<<<<<<<<<<<WELCOME>>>>>>>>>>>>>>>>>>>")
                print("\n1:BMI \n2:WORKOUT PLANS \n3:Exit")
                print("\n<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>")
                choice2=input("Enter the choice :")
                if choice2 in ["1","2","3"]:
                   if choice2=="1":
                        self.BMI()
                   elif choice2=="2":
                        self.Workout()
                   elif choice2=="3":
                        print("THANKS FOR VISITING")
                        break
                else:
                   print("INVALID CHOICE")
         else:
            print("Valid Name")
            print("xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx")
    def enquiry(self):
        while(True):
         print("*****************Welcome To PROADDICTS GYM*********************")
         print("1:REGISTER \n2:SHOW PACKAGES \n3:EXIT")
         print("***************************************************************")
         choice2=input("ENTER THE CHOICE :")
         if choice2 in ["1","2","3"]:
            if choice2=="1":
                print(">>>>>Please Enter INFROMATION<<<<<")
                mem1=input("Enter the Name :")
                if mem1.isdigit():
                  print("Please Re Enter the Name")
                else:
                 Age1=int(input("Enter The Age :"))
                 if Age1<15:
                  print("*****Incorrect Age*****")
                 else:
                  Gender1=input("Enter the Gender :")
                  Email1=input("Enter the Email :") 
                  if "@gmail.com" in  Email1:
                    print("Thanks For Joining")
                    self.Enquiry.update({mem1:[Age1,Gender1,Email1]})
                  else:
                   print("Invalid to Registered")
            elif choice2=="2":
               self.Package()
            elif choice2=="3":
                 break
         else:
          print("********INVALID CHOICE**********")
    def Manager(Self):
        print("xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx")
        while(True):
            print("1:MANAGER \n2:CLIENT \n3:REGISTER \n4:Exit")
            print("xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx-xx-xx-xx-xx-xxx-xx-xx")
            choice=input("Enter the Choice :")
            if choice in ["1","2","3","4"]:
              if choice=="1":
                   Self.GYMManager()
              elif choice=="2":
                   Self.Client()
              elif choice=="3":
                    Self.enquiry()
              elif choice=="4":
                   break
            else:
                print("invalid")
        
s=Gym()
s.Manager()


        
               

  
            