from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from allAboutProjects.settings import DEFAULT_RESPONSE_DICT
import json


# Create your views here.
@csrf_exempt
def test_score(request):
	from fuzzywuzzy import fuzz 
	from fuzzywuzzy import process 
	result_dict = DEFAULT_RESPONSE_DICT.copy()
	try:
		if request.method == 'POST':
			data=json.loads(request.body)
			s_ans = data["student_answer"]
			i_ans = data["ideal_answer"]

			ratio_algorithm = fuzz.ratio(s_ans, i_ans)
			token_sort_ratio_algorithm = fuzz.token_sort_ratio(s_ans, i_ans)
			token_set_ratio_algorithm = fuzz.token_set_ratio(s_ans, i_ans)
			partial_ratio_algorithm = fuzz.partial_ratio(s_ans, i_ans)

			test_Score = {}
			test_Score["ratio_algorithm"] = ratio_algorithm
			test_Score["token_sort_ratio_algorithm"] = token_sort_ratio_algorithm
			test_Score["token_set_ratio_algorithm"] = token_set_ratio_algorithm
			test_Score["partial_ratio_algorithm"] = partial_ratio_algorithm

			result_dict["data"] = test_Score
			result_dict["status"] = True
			result_dict["message"] = "Success"
		else:
			result_dict["message"] = "Make a post request."
	except Exception as e:
		print(e)
		result_dict["message"] = repr(e)
	return JsonResponse(result_dict)
