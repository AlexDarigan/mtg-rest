# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn, options
from firebase_admin import initialize_app

app = initialize_app()


@https_fn.on_request(cors=options.CorsOptions(cors_origins="*", cors_methods=["get", "post"]))
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    # number = req.data["number"]
    # print(req.data)
    # length = str(len(number))
    print(req)
    return {"message": "We got your msg chars"}

