from django.shortcuts import render

posts = [
{
    'author': 'Team König',
    'title': 'Raum A',
    'content': 'Private Lernguppe',
    'date_posted': 'April 14,2020',
},
{
    'author': 'Vorlesung Info und Kommu',
    'title': 'Raum B',
    'content': '2.Vorlesung SS 20 MWI',
    'date_posted': 'April 15 2020',
}
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context) #Das wird auf der Website angezeigt --> Blog-Home

def about(request): 
     return render(request,'blog/about.html', {'title':'About'})#Das wird unter/about angezeigt
