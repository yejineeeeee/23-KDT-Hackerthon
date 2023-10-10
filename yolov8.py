from ultralytics import YOLO
import torch

model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data=r"C:\Users\nicho\Desktop\해커톤\Data\tree.yaml", epochs=100, patience = 30, batch = 64)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model(r"C:\Users\nicho\Desktop\해커톤\Data\Tree_valid\images\나무_7_남_02139.jpg")  # predict on an image
#path = model.export(format="onnx")  # export the model to ONNX format
torch.save(model.state_dict(), 'model.pt')