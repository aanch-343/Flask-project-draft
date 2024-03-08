from flask import Flask, request, jsonify
import os
import base64

app = Flask(__name__)

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "uploads")

@app.route("/receive-image", methods=["POST"])
def receive_image():
    try:
        image_data = request.json.get("image", None)
        image_name = request.json.get("imageName", None)

        if image_data is None or image_name is None:
            return jsonify({"error": "Invalid request, 'image' or 'imageName' missing"}), 400

        image_data = base64.b64decode(image_data)
        image_path = os.path.join(UPLOAD_DIR, image_name)

        with open(image_path, "wb") as f:
            f.write(image_data)

        print("Image received and saved successfully")
        return jsonify({"message": "Image received and saved"}), 200
    except Exception as e:
        print("Error receiving image:", str(e))
        return jsonify({"error": "Error receiving image"}), 500

if __name__ == "__main__":
    app.run(debug=True)
