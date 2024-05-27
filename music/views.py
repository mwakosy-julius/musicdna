from django.shortcuts import render
from . import functions

def index(request):
    result = ''
    if request.method == 'POST':
        sequence = request.POST.get('sequence')  # Extract input data from request
        if sequence:
            sequence = functions.sequence_validator(sequence)
            if functions.is_dna(sequence):
                melody = functions.melody_maker(sequence)
                result = functions.play_melody(melody)  # Call the function with user input
        else:
            return HttpResponse("Invalid input data")

    context = {'result': result}
    return render(request, "index.html", context) 
