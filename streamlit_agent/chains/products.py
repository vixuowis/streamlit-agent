import os
from langchain.tools import tool
import requests

from streamlit_agent.data.text_on_img import text_on_img


def get_image_url(image_file):
    url = "https://astute-dog-375.convex.site/sendImage?author=admin"

    payload = ""

    # open file
    with open(image_file, "rb") as file:
        payload = file.read()

    if payload == "":
        return ""

    # upload file
    response = requests.request("POST", url, headers={"Content-Type": "image/png"}, data=payload)

    if response.status_code != 200:
        return ""

    # delete file
    try:
        os.remove(image_file)
    except:
        pass

    # return file url
    image_url = "https://astute-dog-375.convex.cloud/api/storage/" + response.text
    return image_url


@tool("制作产品图")
def get_product_t2i(input: str) -> list[str]:
    """通过爆梗生成产品图, 获得 list[img_url]"""

    img_path_list = text_on_img(input.replace("#", ""))
    image_url_list = []
    for img_path in img_path_list:
        image_url_list.append(get_image_url(img_path))

    print("image_url_list = ", image_url_list)
    return image_url_list
