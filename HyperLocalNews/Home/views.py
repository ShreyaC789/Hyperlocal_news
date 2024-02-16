from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("HELLO--home")
    '''scrape = {} Pass your scraped content here and make it appear in the webpage!
    remember render takes three arguemenets!
    test-1 below
    '''
    file_path = 'C:\\Users\\santh\\PythonProgramming\\HyperLocalNews\\Textfiles\\superawesometextfile.txt'
    try:
        with open(file_path,'r')as file:
            contents = file.read()
    except FileNotFoundError:
        contents = "File Not Fount."
    return render(request, 'home.html',{'file_contents':contents})

def about(request):
    #return HttpResponse("HELLO--about")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("HELLO--contact")
    return render(request, 'contact.html')