from django import forms
from .models import maha

class mahaform(forms.ModelForm):

    class Meta:
        model = maha
        fields = ('nama','NIM','kelas','jkelamin')
        labels = {
            'nama' : 'Nama',
            'NIM' : 'NIM',
            'kelas' : 'Kelas',
            'jkelamin' : 'Jenis Kelamin'
        }
    
    def __init__(self, *args, **kwargs):
        super(mahaform,self).__init__(*args, **kwargs)
        self.fields['jkelamin'].empty_label ="Pilih"
        #self.fields['NIM'].required = False