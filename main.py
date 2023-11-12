from flask import Flask,render_template,make_response,jsonify,json,request

quotes_file = "QuoteData.json"

app = Flask (__name__)

#Displays the needed HTML file on screen
@app.route("/")
def home():
  
    return render_template('home.html')



  
#Adding data to the json file
@app.route("/api/sendData", methods=['GET'])
def processData():


  #Loads the entire file into 'data1' variable
  with open(quotes_file, "r") as file:
    data1 = json.load(file)
  
  
  #Pulls both inputs from the URL and sets them to variables
  input_quote = request.args.get("inputQuote")
  input_author = request.args.get("inputAuthor")

  print(input_quote)
  print(input_author)

  #Appends the URL variables to the 'quotes' dictionary in the JSON format 
  data1["quotes"].append({"Quote":input_quote,"Author":input_author})

  #Opens file in write mode and uses 'json.dump' to replace the data in the file with the new version      which includes the added entries
  with open (quotes_file, "w") as file:
    json.dump(data1, file)

  return make_response(jsonify({"Response":"ok"},200))



  
#Deleting Item at a specfic index within the 'quotes' list in the JSON file
@app.route("/api/updateData",methods=['POST'])
def deleteId():

  #Loads the entire file into 'data1' variable
  with open(quotes_file, "r") as file:
    data1 = json.load(file)

  #Pulls the entered ID from the URL, converts it from String to integer, sets that to 'int_id'
  input_id = request.args.get("inputIdToDelete")
  print(input_id)
  int_id = int(input_id)

  #Takes 'int_id' and subracts 1 so it correctly relates to the index of the quote to be deleted
  pos_val = int_id - 1
  print(pos_val)

  #Deletes the entry from 'data1' at the index set by 'pos_val'
  del data1["quotes"][pos_val]
  print("deleted at index", pos_val)

  #Updates the file with the updated version of 'data1'
  with open (quotes_file, "w") as file:
    json.dump(data1, file)
  
  return make_response(jsonify({"Response":"ok"},200))
  
  
  
  
#Opens the file in read mode with the current number of entries 
@app.route("/api/listData",methods =['GET'])
def listData():
  with open(quotes_file, "r") as file:
    data1 = json.load(file)
    print ("total length of file is",len(data1["quotes"]))
  return jsonify(data1)






if __name__ == "__main__":
    app.run("0.0.0.0", 8080)




  
 
  

  