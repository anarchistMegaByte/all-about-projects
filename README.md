API: OCR string matching algorithms

Endpoint: "https://all-about-projects.herokuapp.com/ocr/test_score/"

Method: POST

INPUT JSON:

```json
{
	"student_answer": "Hello world",
	"ideal_answer": "okay world"
}
```

OUTPUT JSON:
```json
{
    "status": true,
    "message": "Success",
    "data": {
        "ratio_algorithm": 67,
        "token_sort_ratio_algorithm": 67,
        "token_set_ratio_algorithm": 67,
        "partial_ratio_algorithm": 70
    }
}
```
