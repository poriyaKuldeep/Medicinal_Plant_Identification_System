from fastapi import FastAPI,UploadFile,File
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import cv2

app=FastAPI()


MODEL=tf.keras.models.load_model("save_models/1")
CLASS_NAMES=['Aloevera','Amla','Amruta_Balli','Arali','Ashoka','Ashwagandha','Avacado','Bamboo','Basale','Betel','Betel_Nut','Brahmi','Castor','Curry_Leaf','Doddapatre','Ekka','Ganike','Gauva','Geranium','Henna','Hibiscus','Honge','Insulin','Jasmine','Lemon','Lemon_grass','Mango','Mint','Nagadali','Neem','Nithyapushpa','Nooni','Pappaya','Pepper','Pomegranate','Raktachandini','Rose','Sapota','Tulasi','Wood_sorel']
@app.get("/ping")
async def ping():
    return "hello , i am alive"

def read_file_as_image(data) ->np.ndarray:
    image=np.array( Image.open(BytesIO(data) ) )
    image_resize=cv2.resize(image,(256,600))
    return image_resize
    # print(BytesIO(data))
    # print("x")
    # print(image)
    

@app.post("/predict")
async def predict(
    file:UploadFile=File(...)
):
   image=read_file_as_image( await file.read()) 
   print(image.shape)
#    print(bytes)
#    img_batch=np.expand_dims(image,0)

#    prediction=MODEL.predict(img_batch)

#    predicted_class= CLASS_NAMES[np.argmax( prediction[0] ) ]
#    confidense=np.max(prediction[0])
   
#    return {
#        'class':predicted_class,
#        'confidence':float(confidense)
#    }
    

if __name__=="__main__":
    uvicorn.run(app,host='localhost' , port=8000)