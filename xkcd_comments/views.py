from django.shortcuts import render_to_response
from urllib2 import urlopen
from bs4 import BeautifulSoup
from xkcd_comments.models import Comments
from django.http import HttpResponseRedirect
from django.template import RequestContext

def get_comic(page_id):
	BASE_URL = 'http://xkcd.com/'
	url = BASE_URL + str(page_id)
	soup = BeautifulSoup(urlopen(url).read())
	comic_image = soup.find('div', {'id' : 'comic'}).contents[1]
	comments = Comments.objects.filter(page_id=page_id)
	comic = {
                'id' : page_id,
		'link' : comic_image['src'],
		'altext' : comic_image['title'],
		'title' : comic_image['alt'],
		'comments': comments,
	}
	return comic


# Create your views here.
def view_page(request, page_id):
	"""to view a page based on page_id"""

	page_data = get_comic(page_id)

	page_data['user'] = request.user.username if request.user.is_authenticated() else None

	return render_to_response(
                "view.html",
                page_data,
                context_instance=RequestContext(request),
	)

def save_comment(request, page_id):
	name = request.POST["name"]
	comment = request.POST["comment"]
	page = Comments(name=name, comment=comment, page_id=page_id)
	page.save()
	return HttpResponseRedirect("/xkcd_social/"+str(page_id)+"/")
