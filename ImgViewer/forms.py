from django import forms

from ImgViewer.models import MyImage


class ImageForm(forms.ModelForm):
    class Meta:
        model = MyImage
        fields = ('image',)
