# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`


import numpy as np
from PIL import Image
from firebase_functions import https_fn, options
from firebase_admin import initialize_app
import torch
import torch.nn as nn


app = initialize_app()

class FeedForwardNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(FeedForwardNN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.activation = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # Two connected layers using relu
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x)
        return x


@https_fn.on_request(cors=options.CorsOptions(cors_origins="*", cors_methods=["get", "post"]))
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    raw = req.json["raw"]
    length = len(raw)
    print("Begin feed")
    feedforward(image=raw)
    print("End feed")
    return { "message": f"We got your {length} chars" }

def feedforward(image):
    input_size = 28 * 28
    hidden_size = 256
    output_size = 10
    trained_model = FeedForwardNN(input_size, hidden_size, output_size)
    trained_model.load_state_dict(torch.load('mnist_feed_forward_model.pth'))
    trained_model.eval()
    print("eval")
    images = np.array(image)
    with torch.no_grad():
        print("RESIZING")
        images = images.reshape(-1, input_size)
        outputs = trained_model(images)
        images = images.reshape(-1, input_size)
        _, predicted = torch.max(outputs.data, 1)
        print("PREDICTED: ", predicted)
