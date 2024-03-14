# lets make some change to merge on github page
import torch
from PIL import Image
import torchvision.transforms as transform

class Generetive_NN:
    def __init__(self, type = "GANs"):
        self.type = type
        self.encoder = None
        self.decoder = None

    def forward(self,image):
        return



class Image_Loader:
    def __init__(self,path):
        self.path = path
        self.images = []

    def get_next_image(self,i):
       next_image = self.images[i]

       transform = transforms.Compose([
           transforms.PILToTensor()
       ])
       next_image = transform(next_image)
       return next_image


def A_Function(arg):
    print(arg)

def Tensor_Gen(*args):
    return torch.rand(args[0],args[1],args[2])

if __name__ == "__main__":

   random_image_tensor = Tensor_Gen(3,8,8)
   A_Function("it is just a function")
   Image_generator = Generetive_NN()








