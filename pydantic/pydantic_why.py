#Pydantic is a most important python data and type vlaiadation libraray.
#It provides : Type validation and data validation
#Without pydantic , we have to write a lot of boiler plate code for managing the data type and data shape.

################Pydantic majorly works in three main steps######################
#1 .Build a pydantic model (class) and in this class specify the ideal schema of the class like  data fields , their types and any validation contraints(like age should never be negative or zero)
#2. Instantitiate the class with passing the raw inputs (a dictionary) . this object will check the validation .
#3. pass this validated object to the function or to use.



# #A basic pydantic introduction showcasing how it is showing type and data validation
# from pydantic import BaseModel

# #################### 1- Build the class ###################
# class Patient(BaseModel):
#     name : str
#     age: int
    
# #################### 2. Create an object for the class ###################
# detail = {"name" : "Arosha Bakhtawar" , "age": 22}
# patient1 = Patient(**detail)


# ############### 3. use that object in function that will take the validated data ###########
# #Insertion 
# def add_data(patient:Patient):
#     name=patient.name
#     age = patient.age
#     print(f"Information Inserted!\nName : {name}\nAge: {age}")
    
# add_data(patient1)


# #Updation     
# def update_data(patient:Patient):
#     name=patient.name
#     age = patient.age
#     print(f"Information Updated!\nName : {name}\nAge: {age}")
    
# update_data(patient1)




#An advance pydantic Model
from pydantic import BaseModel
from typing import List , Dict , Optional

#################### 1- Build the class ###################
class Patient(BaseModel):
    
    name : str #by default all values are required
    age: int
    weight : float
    married : bool = False #setting the default value of married variable to False
    allergies : Optional[List[str]] = None #making it optional 
    contact : Dict[str , str]
    
#################### 2. Create an object for the class ###################
detail = {"name" : "Arosha Bakhtawar" , "age": 22 , "weight":55 , "contact": {"ph#" : "0302-0000000" , "email": "aroshaamin0@gmail.com"}}

patient1 = Patient(**detail)


############### 3. use that object in function that will take the validated data ###########
#Insertion 
def add_data(patient:Patient):
    name=patient.name
    age = patient.age
    married = patient.married
    allergies = patient.allergies
    contact = patient.contact
    print(f"Information Inserted!\nName : {name}\nAge: {age}\nmarried: {married}\nAllergies: {allergies}\ncontact:{contact}")
    
add_data(patient1)


#Updation     
def update_data(patient:Patient):
    name=patient.name
    age = patient.age
    print(f"Information Updated!\nName : {name}\nAge: {age}")
    
update_data(patient1)