import os
import requests

def download_image(url, folder_path):
    # تحقق من وجود المجلد، وإذا لم يكن موجودًا قم بإنشائه
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # الحصول على اسم الملف من URL
    file_name = url.split("/")[-1]
    file_path = os.path.join(folder_path, file_name)

    # تنزيل الصورة وحفظها في المجلد
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded successfully: {file_path}")

# أخذ الرابط الأساسي واسم المجلد من المستخدم
base_url = input("Enter the base URL of the images (without the image number): ")
folder_path = input("Enter the folder path where you want to save the images: ")

# استخدام الكود لتنزيل الصور من 0 إلى 999999
for i in range(1000000):
    url = f'{base_url}{i}.jpg'
    download_image(url, folder_path)
