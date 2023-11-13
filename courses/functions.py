# from PIL import Image, ImageDraw, ImageFont

# def create_certificate_image(user, course, certificate, qr_code_image):
#     background_image = Image.open('media/certificate_template.png')

#     draw = ImageDraw.Draw(background_image)

#     font = ImageFont.load_default()
#     user_name = user.get_full_name()
#     user_name_position = (100, 200)

#     course_title = course.title
#     course_title_position = (100, 250)

#     certificate_identifier = certificate.certificate_identifier
#     certificate_identifier_position = (100, 300)

#     background_image.paste(qr_code_image, (400, 200))

#     draw.text(user_name_position, user_name, fill="black", font=font)
#     draw.text(course_title_position, course_title, fill="black", font=font)
#     draw.text(certificate_identifier_position, certificate_identifier, fill="black", font=font)


#     return background_image