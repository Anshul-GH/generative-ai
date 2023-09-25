import openai

# read the openai API key
OPENAI_API_KEY = r"sk-hY04lj6kRkUOjklj8J909UlksdfUeNxf69js96ay"
openai.api_key = OPENAI_API_KEY

# method to create an image from a text prompt provided as input
# uses the openai DALL-E API
def generate_image(prompt_text, number_of_images):

    result = openai.Image.create(
        prompt = prompt_text,
        n=number_of_images, # number of images to generate. Count of images (urls) depends on this value
        size="256x256" # size of the image
    )

    # the result is a JSON with "data" as the key containing 'url's as values (depending on the value of n)
    # extracting just the url
    # Example JSON strcuture:
    #     {
    #           "created": xxxxxxxxxxx,
    #           "data": [
    #                       {
    #                           "url": "https://<image_url>"
    #                       },
    #                       {
    #                           "url": "https://<image_url>"
    #                       },
    #                       {
    #                           "url": "https://<image_url>"
    #                       },
    #                   ]
    #     }
    
    # collect all image urls (based on the value of n)

    image_url_list = []

    for img_url in result["data"]:
        image_url_list.append(fr'{img_url["url"]}')

    
    return image_url_list


if __name__ == "__main__":
    prompt_text = "old man with a dog"
    number_of_images = 3
    image_url_list = generate_image(prompt_text, number_of_images)

    for img_url in image_url_list:
        print(img_url)
