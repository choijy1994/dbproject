from django import forms

class recommendForm(forms.Form):
    type_kind = forms.ChoiceField(label='음식 종류', required=False, widget=forms.Select(), choices=(
        (None, '선택안함'),
        ('치킨', '치킨'),
        ('중국집', '중국집'),
        ('피자/양식', '피자/양식'),
        ('한식', '한식'),
        ('분식', '분식'),
        ('카페/디저트', '카페/디저트'),
        ('족발/보쌈', '족발/보쌈'),
        ('일식/돈까스', '일식/돈까스'),
        ('야식', '야식')
    ))
    type_cost = forms.ChoiceField(label='가격', required=False, widget=forms.Select(), choices=(
        (None, '선택안함'),
        ('$', '5000원 이내'),
        ('$$', '10000원 이내')
    ))
    type_dist = forms.ChoiceField(label='거리(정문 기준)', required=False, widget=forms.Select(), choices=(
        (None, '선택안함'),
        (3, '3분 이내'),
        (5, '5분 이내'),
        (10, '10분 이내')
    ))
    type_rate = forms.ChoiceField(label='별점', required=False, widget=forms.Select(), choices=(
        (None, '선택안함'),
        (1.0, '1.0 이상'),
        (2.0, '2.0 이상'),
        (3.0, '3.0 이상'),
        (4.0, '4.0 이상')
    ))

