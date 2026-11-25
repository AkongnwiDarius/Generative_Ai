from PIL import Image
import numpy as np 
import tensorflow as tf 

# Loading the model
model_path = "best_pneumonia_model.keras"
model = tf.keras.models.load_model(model_path)

# Loading the image 
image = Image.open('pneumonia.png')

# Converting to grayscale 
image = image.convert('L')

# Resize to 28 x 28
image = image.resize((28,28))

# Convert to numpy array
image = np.array(image)

# Normalizing pixels
# image = image / 255.0

# Adding channel dimension
image = np.expand_dims(image, axis=-1)

# Adding batch dimension
image = np.expand_dims(image, axis=0)

print(image.shape)

# Model prediction
prediction = model.predict(image, verbose=0)

# Proability result
probability = float(prediction[0][0])

# Class Probability
if probability >= 0.1:
    print('Prediction: Pneumonia')
else:
    print('Prediction: Normal')

# Pneumonia prbaility
print(f'Pneumonia probaility: {probability:.2f}%')

# Normal Probability
print(f'Normal probability: {(1 - probability) * 100:.2f}%')
