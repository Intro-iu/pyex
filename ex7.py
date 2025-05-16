from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

# 1. 使用 Pillow 库来打开、调整图像尺寸并保存图像
img = Image.open("image.png")
img = img.resize((100, 100))
img.save("image_resized.png")
# 2. 使用 Pillow 获取图像的基本信息，如尺寸和格式。并调整图像的尺寸
print(img.size)
print(img.format)
# 3. 使用 Pillow 库对图像进行滤波处理，（轮廓、边界加强、浮雕）
img = Image.open("image.png")
img = img.filter(ImageFilter.CONTOUR)
img.save("image_filtered.png")
# 4. 使用 Pillow 库完成图像增强效果。(对比度、亮度、锐度)
img = Image.open("image.png")
img = ImageEnhance.Contrast(img).enhance(2.0)
img = ImageEnhance.Brightness(img).enhance(2.0)
img = ImageEnhance.Sharpness(img).enhance(2.0)
img.save("image_enhanced.png")