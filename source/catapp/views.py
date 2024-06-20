from django.shortcuts import render, redirect
from .cat import Cat

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        cat_name = request.POST.get('catName')
        if cat_name:
            cat = Cat(name=cat_name)
            request.session['cat'] = cat.to_dict()
            return redirect('cat_details', cat_name=cat_name)
    return render(request, 'index.html')

def cat_details(request, cat_name):
    cat_data = request.session.get('cat')
    if cat_data:
        cat = Cat.from_dict(cat_data)
        context = cat.to_dict()
        return render(request, 'cat_info.html', context)
    return redirect('index')

def cat_action(request, cat_name):
    if request.method == 'POST':
        cat_data = request.session.get('cat')
        if cat_data:
            cat = Cat.from_dict(cat_data)
            action = request.POST.get('catAction')

            if action == 'play_with_cat':
                cat.play()
            elif action == 'feed_the_cat':
                cat.feed()
            elif action == 'get_cat_sleep':
                cat.sleep()
            elif action == 'wake_up_cat':  # I have added one more option to wake the cat up, otherwise it was a bit hard to implement the logic
                cat.wake_up()

            request.session['cat'] = cat.to_dict()
            context = cat.to_dict()
            return render(request, 'cat_info.html', context)
    return redirect('cat_details', cat_name=cat_name)