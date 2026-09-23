import os
import numpy as np
import tensorflow as tf
from PIL import Image


class ASLPredictor:
    def __init__(self, model_filename="asl_model.keras"):
        self.model_path = model_filename
        self.labels = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'del', 'nothing', 'space'
        ]

        self.model = self._load_model()

    def _load_model(self):
        if not os.path.isfile(self.model_path):
            print(f"Model not found: {self.model_path}")
            return None

        try:
            model = tf.keras.models.load_model(
                self.model_path,
                compile=False
            )

            print("Model loaded successfully.")
            print("Input shape:", model.input_shape)
            print("Output shape:", model.output_shape)

            return model

        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def preprocess_image(self, image):
        image = image.convert("RGB")
        image = image.resize((128, 128))

        img_array = np.array(
            image,
            dtype=np.float32
        ) / 255.0

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        return img_array

    def predict(self, image, top_k=5):
        if self.model is None:
            return None

        processed_image = self.preprocess_image(image)

        predictions = self.model.predict(
            processed_image,
            verbose=0
        )[0]

        top_indices = np.argsort(predictions)[::-1][:top_k]

        results = []

        for idx in top_indices:
            idx = int(idx)

            results.append({
                "label": self.labels[idx],
                "confidence": float(predictions[idx])
            })

        return results