import gradio as gr
from PIL import Image
from ultralytics import YOLO


source = "best.pt"
model = YOLO('best.pt')

def obejct_detection(image, conf, iou):
    results = model(image, conf=conf, iou=iou)

    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])
    
    return im


interface = gr.Interface(
    obejct_detection,
    [gr.Image(type="pil"),
    gr.Slider(0.1, 0.9, value=0.5, step=0.05, label="confidence"),
    gr.Slider(0.1, 0.9, value=0.25, step=0.05, label="iou")],
    'image'
)

interface.launch(share=True)

