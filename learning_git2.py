# lets make some change to merge on github page
import torch
from PIL import Image
import torchvision.transforms as transform
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

def Tensor_Gen(*args):
    return torch.rand(args[0],args[1],args[2])

if __name__ == "__main__":

   # A_Function("it is just a function")
   random_image_tensor = Tensor_Gen(3,8,8)






