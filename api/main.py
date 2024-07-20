from fastapi import FastAPI,UploadFile,File
import uvicorn
import numpy as np
from io import BytesIO
import io
from PIL import Image
import tensorflow as tf
import cv2
import json

app=FastAPI()

@app.get("/ping")
async def ping():
    return "Hello"

# artifacts\training\model_epoch_50.h5
MODEL=tf.keras.models.load_model("model.h5")
CLASS_NAMES=['Aloevera','Amla','Amruta_Balli','Arali','Ashoka','Ashwagandha','Avacado','Bamboo','Basale','Betel','Betel_Nut','Brahmi','Castor','Curry_Leaf','Doddapatre','Ekka','Ganike','Gauva','Geranium','Henna','Hibiscus','Honge','Insulin','Jasmine','Lemon','Lemon_grass','Mango','Mint','Nagadali','Neem','Nithyapushpa','Nooni','Pappaya','Pepper','Pomegranate','Raktachandini','Rose','Sapota','Tulasi','Wood_sorel']
@app.get("/ping")
async def ping():
    return "hello , i am alive"

def read_file_as_image(data) ->np.ndarray:
    image=np.array( Image.open(io.BytesIO(data) ) )
    image_resize=cv2.resize(image,(224,224))
    return image_resize
    # print(BytesIO(data))
    # print("x")
#     # print(image)


@app.post("/predict")
async def predict( 
    file:UploadFile=File(...)
):
   image=read_file_as_image( await file.read()) 
#    print(bytes)
   img_batch=np.expand_dims(image,0)

   prediction=MODEL.predict(img_batch)

   predicted_class= CLASS_NAMES[np.argmax( prediction[0] ) ]
   confidense=np.max(prediction[0])

#    print(predicted_class)
#    print(confidense)


   
   data=[predicted_class,float(confidense)]
   return predicted_class

  

   
# #    return {
# #        'class':predicted_class,
# #        'confidence':float(confidense)
# #    }
# #    data={
# #        "class":predicted_class,
# #        "confidence":float(confidense)
# #    }
# #    json_res=json.dumps(data)
# #    return json_res
   

    

if __name__=="__main__":
    uvicorn.run(app,host='localhost' , port=8000)