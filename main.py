#import the fastapi 
from fastapi import FastAPI , Path , HTTPException , Query
import json



#function to load the data so that i could be send to the client

def load_data():
    with open("patients.json" , "r") as f:
        data = json.load(f)
        
    return data

#we are going to create an end point . On hitting that end-point the user will see "Hello world"

#creating an object of the Fastapi 
app = FastAPI()

#if we want to see some data by fetching it from the server we will do a get request.
#if we want to send some data to server , we will do a post request

#after creating the object , we will specify the end points :

############## First Endpoint #################
@app.get("/")  #in parenthesis , we define the route or path , mean if we write the /after our website name , we will hit at that 
#on hitting that endpoint , what we will get will be specified here 
def showhello():
    return {"message" :"Patients Management System API"}


##############Second Endpoint #################
@app.get("/about")
def about():
    return {"about" : "A fully functional API to manage patients records"}

###############Third Endpoint to view the patients records ##################
@app.get("/view")
def view():
    data = load_data()
    return data

############ Forth endpoint #####################
#view only the specific patient's records
#Here comes the concept of path parameters : which can be added to the address as the dynamic parameters

#Logic : create an endpoint , on that hitting that end point the client entered the required patient ID and get its record

@app.get("/patient/{patient_id}")
def get_patient(patient_id:str = Path(description = "Patient ID is required to get the patient data" , example="P002")):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404 , detail = "Patient Not Found")


################# 5th EndPoint ################
#want to sort all the patients records on some key either height , weight and bmi 
#here comes the concept of Query parameters which are used to perform the operations like sorting paging etc

@app.get("/sort")

def sort_patients(sort_by :str = Query(..., description = "Enter any option you wnat to sort the patients [height , weight , bmi] ") , order : str = Query("asc" , description = "specify the order you want to sort on either asc and desc")):
    
    valid_fields = ["height" , "weight" , "bmi"]
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400 , detail=f"Invalid field. Select any field from {valid_fields}")
    if order not in ["asc" , "desc"]:
        raise HTTPException(status_code=400 , detail= "Invalid Order . Select either asc or desc")
    
    data = load_data()
    sort_order = True if order == "desc" else False
    
    sorted_data = sorted(data.values() , key = lambda x : x.get(sort_by , 0) , reverse = sort_order) 
    
    return sorted_data
        
        
        
