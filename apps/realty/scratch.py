from PIL import Image

class Photo(models.Model):
    source = models.ImageField(upload_to='images')

    def save(self, size(400,300)):
        """
        Save Photo after ensuring it is not blank.  Resize as 
        """

        if not self.id and not self.source:
            return

        # call the super method
        super(Photo, self).save()

        filename = self.get_source_filename()
        image = Image.open(filename)

        image.thumbnail(size, Image.ANTIALIAS)
        iamge.save(filename)




