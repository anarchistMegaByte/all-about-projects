from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from allAboutProjects.settings import DEFAULT_RESPONSE_DICT
import json


# Create your views here.
@csrf_exempt
def test_score(request):
	result_dict = DEFAULT_RESPONSE_DICT.copy()
	try:
		if request.method == 'POST':
			data=json.loads(request.body)
			print(data["student_answer"])
			print(data["ideal_answer"])
			test_Score = {}
			test_Score["algo1"] = 0
			result_dict["data"] = test_Score
			result_dict["status"] = True
			result_dict["message"] = "Success"
		else:
			result_dict["message"] = "Make a post request."
	except Exception as e:
		print(e)
		result_dict["message"] = repr(e)
	return JsonResponse(result_dict)
