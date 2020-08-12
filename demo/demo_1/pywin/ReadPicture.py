import pytesseract
from PIL import Image





# im_en = Image.open('115.png')
im_ch = Image.open('456.png')
print('========识别字母========')
# print(pytesseract.image_to_string(im_en), '\n\n')
print(im_ch)

print('========识别中文========')
print(pytesseract.image_to_string(im_ch, lang='chi_sim'))