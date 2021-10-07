from PIL import Image, ImageDraw, ImageFont

class InformeWhats:
    @staticmethod
    def main(texto:str):
        
        imagem = Image.open('img_base\InformeLabs.png')
        desenho = ImageDraw.Draw(imagem)
        fonte = ImageFont.truetype("fontes\cour.ttf", 26)

        desenho.text( (40,80), texto, (0, 0, 0), font=fonte )
        imagem.save("Informe.png")