from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	'my_list': [
    		{
    			'restaurant_name': 'Kofe',
    			'food_type': 'Coffee'
    		},
    		{
    			'restaurant_name': 'McDonalds',
    			'food_type': 'Junk Food'
    		},
    		{
    			'restaurant_name': 'Joa',
    			'food_type': 'Sushi'
    		},

    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object':{
    	'restaurant_name': 'Joa',
    	'food_type': 'Sushi',
    	}

    }
    return render(request, 'detail.html', context)
