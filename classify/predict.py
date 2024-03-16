PAT = '2cb9f0ee30f7447d804a0d4bad28a988'

USER_ID = 'openai'
APP_ID = 'chat-completion'

MODEL_ID = 'openai-gpt-4-vision'
MODEL_VERSION_ID = '266df29bc09843e0aee9b7bf723c03c2'


RAW_TEXT = '''tell me if there is a map in this image or not, if yes show me 
"True" if no show me "False"'''


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)

metadata = (('authorization', 'Key ' + PAT),)

userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)


def is_map(image_path):

    with open(image_path, "rb") as f:
            file_bytes = f.read()
    
    print("Checking if Map...")

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID, 
            inputs=[
                 resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw=RAW_TEXT
                        ), image=resources_pb2.Image(
                            base64=file_bytes
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception(f"Post model outputs failed, status: {post_model_outputs_response.status.description}")

    if post_model_outputs_response.outputs[0].data.text.raw == "True":
         print("Found map")
         return True
    return False
