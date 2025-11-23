from transformers import AutoImageProcessor, Mask2FormerForUniversalSegmentation
print('Imported')
processor = AutoImageProcessor.from_pretrained("facebook/mask2former-swin-large-mapillary-vistas-semantic")
model = Mask2FormerForUniversalSegmentation.from_pretrained("facebook/mask2former-swin-large-mapillary-vistas-semantic")
print('Model loaded')
print('Hola')