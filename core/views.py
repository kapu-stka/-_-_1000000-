from django.shortcuts import render
def main(request):
    path=request.path
    path=path.replace('/','')
    if path=="":
        path='main'
    cities = ['Москва', 'Санкт-Петербург', 'Екатеринбург', 'Анадырь', 'Воронеж', 'Кострома']

    return render(request,f'{path}.html', {'cities': cities})
def kos(request):
    g1="Кострома-город в России на веке Волге, основан в 1152 году."
    return render(request, 'kos.html', {'g1':g1})
# Create your views here.
