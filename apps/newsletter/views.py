from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from apps.likes.models import UserLike
from apps.matches.models import Match, PositionMatch, EmployerMatch, LocationMatch
from apps.questions.models import Question
from .forms import ContactForm, SignUpForm


def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you"
		}

	if request.user.is_authenticated():

		#PositionMatch.objects.update_top_suggestions(request.user, 20)
		matches = Match.objects.get_matches_with_percent(request.user)[:6]
		positions = PositionMatch.objects.filter(user=request.user)[:6]

		if positions.count() > 0:
			positions[0].check_update(20) #20 matches total
		locations = LocationMatch.objects.filter(user=request.user)[:6]
		employers = EmployerMatch.objects.filter(user=request.user)[:6]
		mutual_likes = UserLike.objects.get_all_mutual_likes(request.user)[:4]

		queryset = Question.objects.all().order_by('-timestamp') 
		context = {
			"queryset": queryset,
			"matches": matches,
			"positions": positions,
			"locations": locations,
			"employers": employers,
			"mutual_likes": mutual_likes
		}
		return render(request, "questions/home.html", context)

	return render(request, "home.html", context)


def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)
