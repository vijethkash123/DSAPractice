#Print statements used here are for uour reference
#T1
import random
import sys
import numpy as np
from matplotlib import pyplot as plt
people_dict={}
patient_dict={}
people_list = []
patient_list=[]

def load_people():
    f = open("C:\\Users\\VIjeth Kashyap\\Desktop\\a2_sample_set.txt", "r") #Use os chdir later to give path before submitting
    content = f.readlines()
    for x in content:
        name, friends = x.split(':')
        fl=[]
        for friend in friends.split(','):
            fl.append(friend.strip())
        first_name, last_name = name.split(' ')
        #print(first_name,last_name)
    #Dynamically create Person object for each person in the file and call respective functions for Person to add his friends to list.

        people_dict[name]= Person(first_name,last_name)

        #Dynamically calling add_friends() for each person record using fl list
        people_dict[name].add_friend(fl)  

        print("------------------FRIENDS---------------------")
        print(people_dict[name].get_friends())
    for person in people_dict.values():
        people_list.append(person)
            #print(type(person)) #Checking if it is of type 'instance'

    print(people_dict['Alton Justis'].get_friends())  #indivisual check
    return people_list    #Returning List of objects as per your documentation standards

            




class Person :
    friend_list = []
    health_points=0 #Each person starts with 100 health points assumed, Can directly change this from set_health() as suggested in Task2

    def __init__(self,first_name, last_name):
        self.friend_list=[]   #Reinitialzing is important !!
        self.first_name = first_name
        self.last_name = last_name  


    def get_name(self):
        full_name = str(self.first_name)+" "+str(self.last_name)
        return full_name
    
    def add_friend(self,friend_person):
        self.friend_list.extend(friend_person);

    def get_friends(self):
        return self.friend_list


class Patient(Person):

    def __init__(self,first_name, last_name, initial_health):
        self.first_name = first_name
        self.last_name = last_name 
        self.health_points = initial_health
    
    def get_health(self):
        return self.health_points
    
    def set_health(self,new_health):
        self.health_points = new_health
    
    def is_contagious(self):
        if(self.health_points<50):
            return True
        return False
    def infect(self,viral_load):
        if self.health_points<1:
            self.health_points = 1
        if self.health_points>=100:
            self.health_points=100
        if self.health_points<=29:
            self.health_points=self.health_points-int((0.1*viral_load))
        if self.health_points >29 and self.health_points<50 :
            self.health_points=self.health_points-int((1.0*viral_load))
        if self.health_points>=50:
            self.health_points=self.health_points-int((2.0*viral_load))
        
    def sleep(self):
        self.health_points+=5


def load_patients(default_health):
    f = open("C:\\Users\\VIjeth Kashyap\\Desktop\\a2_sample_set.txt", "r") #Use os chdir later to give path before submitting
    content = f.readlines()
    for x in content:
        name, friends = x.split(':')
        fl=[]
        for friend in friends.split(','):
            fl.append(friend.strip())
        first_name, last_name = name.split(' ')
        patient_dict[name]= Patient(first_name,last_name,default_health)
        patient_dict[name].add_friend(fl)  

    #Sleep increases HP by 5

    for patient in patient_dict.values():
        patient_list.append(patient)
    return patient_list  

def run_simulation(days, meeting_probability, patient_zero_health):
    count_list=[]
    load_patients(75) #Default helath points = 75 , except for patient zero
    patient_list[0].set_health(patient_zero_health) #setting patient zero health manually 
    for i in range(0,days):
        counter=0
        for patient in patient_list:
            for friend in patient.get_friends():
                if patient.is_contagious() and random.uniform(0.0,1.0) <= meeting_probability and meeting_probability!=0.0:
                    viral_load = round(5+(((patient.get_health()-25)** 2)/62),2)
                    patient_dict[friend].infect(viral_load)
                    # break
                if patient_dict[friend].is_contagious():
                    if random.uniform(0.0,1.0) <= meeting_probability and meeting_probability!=0.0:
                        viral_load = round(5+(((patient_dict[friend].get_health()-25)** 2)/62),2)
                        patient.infect(viral_load)
                    break

        for patient in patient_list:
            # counter = 0
            if patient.is_contagious():
                counter+=1
            patient.sleep()
        count_list.append(counter)





                # viral_load = round(5+(((patient.get_health()-25)** 2)/62),2)
            #     patient_friends=patient.get_friends()
            #     for friend in patient_friends:
            #         if random.random(0.0,1.0) >= meeting_probability and meeting_probability!=0.0:
                        # if friend in patient_dict:
                        #     patient_dict[friend].infect(viral_load)
            
            # else:
            #     for friend in patient.get_friends():
            #         if friend in patient_dict:
            #             if patient_dict[friend].is_contagious():
            #                 if random.uniform(0.0,1.0) >= meeting_probability and meeting_probability!=0.0:
            #                     viral_load = round(5+(((patient.get_health()-25)** 2)/62),2)
            #                     patient.infect(viral_load)
            #                     break


    return count_list

             

print(run_simulation(15,0.33,45))
#print(run_simulation(60,0.25,49))
#print(run_simulation(90,0.18,40))




sys.exit()


     
