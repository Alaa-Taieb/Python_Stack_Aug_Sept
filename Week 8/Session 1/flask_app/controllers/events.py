from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask import jsonify
from flask_app.models.event import Event


@app.route('/')
def index():
    all_events = Event.get_all()
    return render_template("index.html", events=all_events)

@app.route('/events/create', methods=['POST'])
def create_event():
    Event.add(request.form)
    return redirect("/")

@app.route('/events/create/return_element', methods=['POST'])
def create_event_element():
    Event.add(request.form)
    return render_template("_event_element.html", title=request.form['title'])

@app.route('/events/create/return_json', methods=['POST'])
def create_event_json():
    Event.add(request.form)
    return jsonify(title=request.form['title'])


@app.route('/events/reset', methods=['POST'])
def reset_events():
    Event.reset()
    return redirect("/")





    # Create your views here.
# def index(request):
#     context = {
#         'events': Event.objects.all()
#     }
#     return render(request, 'index.html', context)

# def create_event(request):
#     Event.objects.create(title = request.POST['title'])
#     return redirect('/')

# def create_event_element(request):
#     print(request.POST)
#     new_event = Event.objects.create(title = request.POST['title'])
#     context = {
#         'event': new_event
#     }
#     return render(request, '_event_element.html', context)

# def create_event_json(request):
#     print(request.POST)
#     new_event = Event.objects.create(title = request.POST['title'])
#     return JsonResponse(new_event.return_JSON())