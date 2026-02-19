from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

HF_TOKEN =(the token code) 
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base",
    token=HF_TOKEN)
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base",
    token=HF_TOKEN)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()


def generate_caption(image_path):
    from PIL import Image
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt").to(device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
