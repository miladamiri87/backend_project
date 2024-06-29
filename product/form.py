from django import forms

from product.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'body')

    title = forms.CharField(label='Title ', widget=forms.TextInput(attrs={'class': 'label_title_form',
                                                                          'placeholder': 'Write a summary of your experience in one sentence, and would be helpful to others.'}))
    body = forms.CharField(label='Content ', widget=forms.Textarea(attrs={'class': 'label_title_form',
                                                                          'placeholder': 'When writing a review please add information that you felt was missing and you would '
                                                                                         'have liked to have seen when you were considering your purchase.'
                                                                                         ' Tell us your thoughts.'}))


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'id': 'search_form',
                                                           'placeholder': 'What are you looking for?'}))
