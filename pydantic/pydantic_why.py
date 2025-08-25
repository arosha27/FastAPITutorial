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
#for data validation we will use the Field

#1 Filed for data validation and filed for metadatas

#Fiel Function is used for data validation , default value setting , adding description 
from pydantic import BaseModel , Field  , EmailStr , AnyUrl
from typing import List , Dict , Optional , Annotated

#################### 1- Build the class ###################
class Patient(BaseModel):
    
    name : Annotated[str , Field(max_length=50 , description="Enter your name under 50 characters.")] #by default all values are required
    age: Annotated[int , Field(gt=0 , lt=120 , strict=True)]
    email : EmailStr
    linked_In : AnyUrl
    weight : Annotated[float , Field(strict=True , get=0)]
    married : Annotated[bool , Field(default=False , description = "Are you married or not?")] #setting the default value of married variable to False
    allergies : Annotated[Optional[List[str]] , Field(default=None , max_length = 5)] #making it optional 
    contact : Dict[str , str]
    
#################### 2. Create an object for the class ###################
detail = {"name" : "Arosha Bakhtawar" , "age": 22, "email":"aroshaamin0@gmail.com" ,"linked_In":"https://www.linkedin.com/in/arosha-amin","weight":55.0 , "allergies":["pollens" , "dust"], "contact": {"ph#" : "0302-0000000"}}

patient1 = Patient(**detail)


############### 3. use that object in function that will take the validated data ###########
#Insertion 
def add_data(patient:Patient):
    name=patient.name
    age = patient.age
    email = patient.email
    married = patient.married
    weight = patient.weight
    linked_url = patient.linked_In
    allergies = patient.allergies
    contact = patient.contact
    print(f"Information Inserted!\nName : {name}\nAge: {age}\nWeight : {weight}\nmarried: {married}\nAllergies: {allergies}\ncontact:{contact}\nemail: {email}\nLinkedin_URL :{linked_url}")
    
add_data(patient1)


#Updation     
def update_data(patient:Patient):
    name=patient.name
    age = patient.age
    print(f"Information Updated!\nName : {name}\nAge: {age}")
    
