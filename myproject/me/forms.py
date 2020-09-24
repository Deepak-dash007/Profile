from django import forms
from .models import message


class MessageForm(forms.ModelForm):
	class Meta:
		model = message
		fields = ['name','email','contact','message']

		widgets = {
			'name' : forms.TextInput(attrs={"placeholder":"Name", "onfocus":"this.value = '';","onblur":"if (this.value=='') this.value = this.defaultValue","required":""}),
			'email' : forms.TextInput(attrs={"placeholder":"Email", "onfocus":"this.value = '';","onblur":"if (this.value=='') this.value = this.defaultValue","required":""}),
			'contact' : forms.TextInput(attrs={"placeholder":"Contact","onfocus":"this.value = '';","onblur":"if (this.value=='') this.value = this.defaultValue","required":""}),
			'message' : forms.Textarea(attrs={"placeholder":"Message","onfocus":"this.value = '';","onblur":"if (this.value=='') this.value = 'Message'","required":""})
		}